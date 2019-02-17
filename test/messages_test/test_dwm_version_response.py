import unittest

from decawave_1001_rjg.messages.dwm_version_response import DwmVersionResponse


class TestDwmVersionResponse(unittest.TestCase):

    message = bytes([0x40, 0x01, 0x00,
                     0x50, 0x04, 0x01, 0x05, 0x02, 0x18,
                     0x51, 0x04, 0x00, 0x07, 0x01, 0x00,
                     0x52, 0x04, 0x2A, 0x00, 0xCA, 0xDE])

    def test_get_firmware_version(self):
        response = DwmVersionResponse(self.message)
        version = response.get_firmware_version()
        self.assertEqual('1.5.2.8', version)

    def test_get_configuration_version(self):
        response = DwmVersionResponse(self.message)
        version = response.get_configuration_version()
        self.assertEqual('10700', version)

    def test_get_hardware_version(self):
        response = DwmVersionResponse(self.message)
        version = response.get_hardware_version()
        self.assertEqual('DECA002A', version)
