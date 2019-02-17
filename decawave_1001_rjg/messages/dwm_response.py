from .tlv_message import TlvMessage


class DwmResponse(TlvMessage):
    def __init__(self, message: bytes):
        super().__init__(message)
        self.expected_type = 0x40

    def error_code(self):
        return self.message[2]

    def is_ok(self):
        return self.error_code() == 0x00 and \
               not self.error_invalid_response() and \
               not self.error_wrong_type()

    def error_bad_request(self):
        """Data sheet says: unknown command or broken TLV frame"""
        return self.error_code() == 0x01

    def error_internal_error(self):
        return self.error_code() == 0x02

    def error_invalid_parameter(self):
        return self.error_code() == 0x03

    def error_busy(self):
        return self.error_code() == 0x04

    def error_invalid_response(self):
        """The device may return a message consisting of all zeros or all
        0xFF if the DWM lifecycle is in an unexpected state. If this happens
        then the app should perform a reset and retry the API call."""
        return self.type() == 0x00

    def error_wrong_type(self):
        return self.expected_type != self.type()