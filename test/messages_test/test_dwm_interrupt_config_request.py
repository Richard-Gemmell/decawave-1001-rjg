import unittest

from decawave_1001_rjg.messages.dwm_interrupt_config_request import DwmInterruptConfigRequest


class DwmInterruptConfigRequestTest(unittest.TestCase):
    def test_request_neither(self):
        message = DwmInterruptConfigRequest(False, False)
        self.assertEqual(bytes([0x34, 0x01, 0x00]), message.message)

    def test_request_loc_ready(self):
        message = DwmInterruptConfigRequest(True, False)
        self.assertEqual(bytes([0x34, 0x01, 0x01]), message.message)

    def test_request_spi_data_ready(self):
        message = DwmInterruptConfigRequest(False, True)
        self.assertEqual(bytes([0x34, 0x01, 0x02]), message.message)

    def test_request_both(self):
        message = DwmInterruptConfigRequest(True, True)
        self.assertEqual(bytes([0x34, 0x01, 0x03]), message.message)
