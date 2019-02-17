import unittest

from decawave_1001_rjg.messages.dwm_position_response import DwmPositionResponse


class DwmPositionResponseTest(unittest.TestCase):
    def test_message_is_ok(self):
        message = DwmPositionResponse(bytes([0x40, 0x01, 0x00, 0x41, 0x0D,
                                      0x79, 0x00, 0x00, 0x00,
                                      0x32, 0x00, 0x00, 0x00,
                                      0xfb, 0x00, 0x00, 0x00,
                                      0x64]))
        self.assertTrue(message.is_ok())

    def test_get_position(self):
        message = DwmPositionResponse(bytes([0x40, 0x01, 0x00, 0x41, 0x0D,
                                      0x79, 0x00, 0x00, 0x00,
                                      0x32, 0x00, 0x00, 0x00,
                                      0xfb, 0x00, 0x00, 0x00,
                                      0x65]))
        position = message.get_position()
        self.assertEqual([121, 50, 251], position.position())
        self.assertEqual(101, position.quality_factor())