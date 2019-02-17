import unittest

from decawave_1001_rjg.messages.dwm_response import DwmResponse


class TestDwmResponse(unittest.TestCase):
    def test_error_code(self):
        response = DwmResponse(bytes([0x40, 0x01, 0xF0]))
        self.assertEqual(0xF0, response.error_code())

    def test_is_ok(self):
        response = DwmResponse(bytes([0x40, 0x01, 0x00]))
        self.assertTrue(response.is_ok())
        self.assertFalse(response.error_bad_request())
        self.assertFalse(response.error_busy())
        self.assertFalse(response.error_internal_error())
        self.assertFalse(response.error_invalid_parameter())
        self.assertFalse(response.error_wrong_type())

    def test_error_bad_request(self):
        response = DwmResponse(bytes([0x40, 0x01, 0x01]))
        self.assertFalse(response.is_ok())
        self.assertTrue(response.error_bad_request())

    def test_error_internal_error(self):
        response = DwmResponse(bytes([0x40, 0x01, 0x02]))
        self.assertFalse(response.is_ok())
        self.assertTrue(response.error_internal_error())

    def test_error_invalid_parameter(self):
        response = DwmResponse(bytes([0x40, 0x01, 0x03]))
        self.assertFalse(response.is_ok())
        self.assertTrue(response.error_invalid_parameter())

    def test_error_busy(self):
        response = DwmResponse(bytes([0x40, 0x01, 0x04]))
        self.assertFalse(response.is_ok())
        self.assertTrue(response.error_busy())

    def test_error_invalid_response(self):
        response = DwmResponse(bytes([0x00, 0x00, 0x00]))
        self.assertFalse(response.is_ok())
        self.assertTrue(response.error_invalid_response())

    def test_error_wrong_type(self):
        response = DwmResponse(bytes([0x22, 0x01, 0x00]))
        self.assertFalse(response.is_ok())
        self.assertTrue(response.error_wrong_type())
