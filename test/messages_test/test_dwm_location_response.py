import unittest

from decawave_1001_rjg.messages.dwm_location_response import DwmLocationResponse


class TestDwmLocationResponse(unittest.TestCase):
    data = [0x40, 0x01, 0x00, 0x41, 0x0D,
            0x01, 0x02, 0x00, 0x00,
            0x05, 0x00, 0x00, 0x00,
            0xFB, 0x00, 0x00, 0x00,
            0x0F,
            0x49, 0x51, 0x04,
            0x01, 0x0A, 0x05, 0x00, 0x00, 0x00, 0x64, 0x01, 0x02, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0xFB, 0x00, 0x00, 0x00, 0x0F,
            0x02, 0x0B, 0x05, 0x00, 0x00, 0x00, 0x64, 0x01, 0x02, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0xFB, 0x00, 0x00, 0x00, 0x0F,
            0x03, 0x0C, 0x05, 0x00, 0x00, 0x00, 0x64, 0x01, 0x02, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0xFB, 0x00, 0x00, 0x00, 0x0F,
            0x04, 0x0D, 0x05, 0x00, 0x00, 0x00, 0x64, 0x01, 0x02, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0xFB, 0x00, 0x00, 0x00, 0x0F
            ]

    def test_reject_result_for_anchor(self):
        with self.assertRaises(NotImplementedError):
            DwmLocationResponse(bytes([
                0x40, 0x01, 0x00, 0x41, 0x0D,
                0x01, 0x02, 0x00, 0x00,
                0x05, 0x00, 0x00, 0x00,
                0xFB, 0x00, 0x00, 0x00,
                0x0F,
                0x48, 0x01, 0x00,
                ]))

    def test_get_tag_position(self):
        message = DwmLocationResponse(bytes(self.data))
        self.assertEqual(0x0F, message.get_tag_position().quality_factor())

    def test_get_number_of_anchors(self):
        message = DwmLocationResponse(bytes(self.data))
        self.assertEqual(4, message.num_anchors)

    def test_get_anchor_positions(self):
        message = DwmLocationResponse(bytes(self.data))
        anchors = message.get_anchor_distances_and_positions()
        self.assertEqual(4, len(anchors))
        self.assertEqual('A01', anchors[0].address())
        self.assertEqual('B02', anchors[1].address())
        self.assertEqual('C03', anchors[2].address())
        self.assertEqual('D04', anchors[3].address())

    def test_from_properties(self):
        message = DwmLocationResponse(bytes(self.data))
        anchors = message.get_anchor_distances_and_positions()
        tag_position = message.get_tag_position()
        # Act
        built = DwmLocationResponse.from_properties(tag_position, anchors)
        # Assert
        self.assertEqual(tag_position.position(), built.get_tag_position().position())
        self.assertEqual(tag_position.quality_factor(), built.get_tag_position().quality_factor())
        built_anchors = built.get_anchor_distances_and_positions()
        self.assertEqual(4, len(built_anchors))
        self.assertEqual('A01', built_anchors[0].address())
        self.assertEqual('B02', built_anchors[1].address())
        self.assertEqual('C03', built_anchors[2].address())
        self.assertEqual('D04', built_anchors[3].address())
        self.assertEqual(anchors[0].position().position(), built_anchors[0].position().position())
