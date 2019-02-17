import unittest

from decawave_1001_rjg.messages.dwm_position import DwmPosition
from decawave_1001_rjg.messages.tlv_message import TlvMessage


class TestDwmPosition(unittest.TestCase):

    message = TlvMessage(bytes([0x40, 0x01, 0x00, 0x41, 0x0D,
                          0x79, 0x00, 0x00, 0x00,
                          0x32, 0x00, 0x00, 0x00,
                          0xfb, 0x00, 0x00, 0x00,
                          0x64]))

    def test_get_position(self):
        dwm_pos = DwmPosition(self.message, 5)
        pos = dwm_pos.position()
        self.assertEqual([121, 50, 251], pos)

    def test_get_quality_factor(self):
        dwm_pos = DwmPosition(self.message, 5)
        self.assertEqual(100, dwm_pos.quality_factor())

    def test_from_properties(self):
        dwm_pos = DwmPosition(self.message, 5)
        built = DwmPosition.from_properties(dwm_pos.position(), dwm_pos.quality_factor())
        self.assertEqual(dwm_pos.position(), built.position())
        self.assertEqual(dwm_pos.quality_factor(), built.quality_factor())
