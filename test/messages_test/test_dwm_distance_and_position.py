import unittest

from decawave_1001_rjg.messages.dwm_distance_and_position import DwmDistanceAndPosition
from decawave_1001_rjg.messages.dwm_position import DwmPosition
from decawave_1001_rjg.messages.tlv_message import TlvMessage


class TestDwmDistanceAndPosition(unittest.TestCase):
    message = TlvMessage(bytes([
        0x49, 0x51, 0x04,
        0xAB, 0xCD,
        0x87, 0x65, 0x43, 0x21,
        0x10,
        0x79, 0x00, 0x00, 0x00, 0x32, 0x00, 0x00, 0x00, 0xfb, 0x00, 0x00, 0x00, 0x64]))

    def test_address(self):
        dp = DwmDistanceAndPosition(self.message, 3)
        self.assertEqual('CDAB', dp.address())

    def test_distance(self):
        dp = DwmDistanceAndPosition(self.message, 3)
        self.assertEqual(558065031, dp.distance())

    def test_quality_factor(self):
        dp = DwmDistanceAndPosition(self.message, 3)
        self.assertEqual(0x10, dp.quality_factor())

    def test_position(self):
        dp = DwmDistanceAndPosition(self.message, 3)
        self.assertEqual(100, dp.position().quality_factor())

    def test_from_properties(self):
        dp = DwmDistanceAndPosition(self.message, 3)
        new_pos = DwmPosition.from_properties(dp.position().position(), dp.position().quality_factor())
        built = DwmDistanceAndPosition.from_properties(dp.address(), dp.distance(), dp.quality_factor(), new_pos)
        self.assertEqual(dp.address(), built.address())
        self.assertEqual(dp.distance(), built.distance())
        self.assertEqual(dp.quality_factor(), built.quality_factor())
        self.assertEqual(dp.position().position(), built.position().position())
        self.assertEqual(dp.position().quality_factor(), built.position().quality_factor())
