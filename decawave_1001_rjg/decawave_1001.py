import spidev
import time

from . import GPIOInterrupt
from .messages.dwm_interrupt_config_request import DwmInterruptConfigRequest
from .messages.dwm_config_response import DwmConfigResponse
from .messages.dwm_location_response import DwmLocationResponse
from .messages.dwm_position_response import DwmPositionResponse
from .messages.dwm_request import DwmRequests
from .messages.dwm_response import DwmResponse
from .messages.dwm_status_response import DwmStatusResponse
from .messages.dwm_version_response import DwmVersionResponse
from .messages.tlv_message import TlvMessage


class Decawave1001Driver:
    def __init__(self, ready_pin: int, spi_device: int):
        self.min_time_between_transfers = 0.0001
        self.min_time_before_requesting_size = 0.0001
        self.max_size_retry_count = 0.5 / self.min_time_before_requesting_size
        self.max_retry_count = 5    # Number of times to retry a failed message
        self.timestamp = time.time()
        self.spi = spidev.SpiDev()
        self.data_ready_interrupt = GPIOInterrupt(ready_pin)
        self._init_spi(spi_device)
        self._init_decawave()

    def _init_spi(self, spi_device: int):
        self.spi.open(0, spi_device)
        self.spi.mode = 0b00
        self.spi.max_speed_hz = 8000000

    def _init_decawave(self):
        self.soft_reset()
        self._enable_data_ready_pin()

    def _enable_data_ready_pin(self):
        request = DwmInterruptConfigRequest(True, False)
        self._send_and_get_response(request)

    def close(self):
        """Closes the SPI connection. This must be called on shutdown."""
        self.spi.close()
        self.data_ready_interrupt.close()

    def soft_reset(self):
        """Returns the DWM tag's state machine to Idle so it'll be ready for a new request.
        Use this to reset the tag when the message responses are out of sync."""
        # Simply send 0xFF 3 times in a row.
        self._request_response_size()
        self._request_response_size()
        self._request_response_size()

    def reset(self):
        """Reboots the Decawave module. This takes a couple of seconds."""
        self._safe_transfer(list(DwmRequests.dwm_reset), self.min_time_between_transfers)
        # It takes a good while for the reset to complete
        time.sleep(2.5)
        self._init_decawave()

    def data_ready(self, timeout: int) -> bool:
        """
        Returns true if there is a new position ready. Resets once the data is read
        by get_pos() or get_loc()
        :param timeout: time to wait for data to be ready in milliseconds
        :return: True if data is ready. False if it timed out.
        """
        return self.data_ready_interrupt.wait_for(timeout)

    def get_cfg(self) -> DwmConfigResponse:
        response = self._send_and_get_response(DwmRequests.dwm_cfg_get)
        return DwmConfigResponse(response)

    def get_ver(self) -> DwmVersionResponse:
        response = self._send_and_get_response(DwmRequests.dwm_ver_get)
        return DwmVersionResponse(response)

    def get_status(self) -> DwmStatusResponse:
        response = self._send_and_get_response(DwmRequests.dwm_status_get)
        return DwmStatusResponse(response)

    def get_pos(self) -> DwmPositionResponse:
        response = self._send_and_get_response(DwmRequests.dwm_pos_get)
        return DwmPositionResponse(response)

    def get_loc(self) -> DwmLocationResponse:
        response = self._send_and_get_response(DwmRequests.dwm_loc_get)
        return DwmLocationResponse(response)

    def _send_and_get_response(self, request: TlvMessage) -> bytes:
        retries = 0
        while retries < 5:
            try:
                return self._single_send_and_get_response(request)
            except RuntimeError as e:
                print('Error sending or receiving message to Decawave DWM 1001. Resetting.')
                print('  {}{}'.format(type(e).__name__, e.args))
                self.soft_reset()

    def _single_send_and_get_response(self, request: TlvMessage) -> bytes:
        response = self._safe_transfer(list(request.message), self.min_time_between_transfers)
        if not self._is_dummy_response(response):
            raise RuntimeError("Didn't get dummy response when sending request")
        count = 1
        size = self._request_response_size()
        while (size == 0) and count < self.max_size_retry_count:
            count = count + 1
            size = self._request_response_size()
        if size == 0:
            raise RuntimeError('Failed to get response size after {} attempts.'.format(count))
        elif size == 0xFF:
            raise RuntimeError('Got invalid response size {} after {} attempts.'.format(size, count))
        else:
            result = DwmResponse(self._safe_read_bytes(size))
        if not result.is_ok():
            raise RuntimeError('Invalid response. Type: {}, error code {}.'.format(result.type(), result.error_code()))
        return result.message

    def _request_response_size(self):
        return self._safe_transfer([0xFF], self.min_time_before_requesting_size)[0]

    def _is_dummy_response(self, response: [int]):
        for byte in response:
            if byte != 0xFF:
                return False
        return True

    def _safe_transfer(self, data: [int], min_gap_time: float) -> [int]:
        self._gap_transfers(min_gap_time)
        result = self.spi.xfer(data)
        self.timestamp = time.time()
        return result

    def _safe_read_bytes(self, size: int) -> [int]:
        self._gap_transfers(self.min_time_between_transfers)
        result = self.spi.readbytes(size)
        self.timestamp = time.time()
        return result

    def _gap_transfers(self, min_gap_time: float):
        new_timestamp = time.time()
        time_to_wait = (self.timestamp + min_gap_time) - new_timestamp
        if time_to_wait > 0:
            time.sleep(time_to_wait)
