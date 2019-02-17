import unittest

from decawave_1001_rjg.messages.dwm_status_response import DwmStatusResponse


class TestDwmStatusResponse(unittest.TestCase):
    def test_position_not_ready(self):
        response = DwmStatusResponse(bytes([0x40, 0x01, 0x00, 0x5A, 0x01, 0x00]))
        self.assertFalse(response.location_ready)

    def test_position_ready(self):
        response = DwmStatusResponse(bytes([0x40, 0x01, 0x00, 0x5A, 0x01, 0x01]))
        self.assertTrue(response.location_ready)

    def test_uwb_network_not_joined(self):
        response = DwmStatusResponse(bytes([0x40, 0x01, 0x00, 0x5A, 0x01, 0x00]))
        self.assertFalse(response.uwb_network_joined)

    def test_uwb_network_joined(self):
        response = DwmStatusResponse(bytes([0x40, 0x01, 0x00, 0x5A, 0x01, 0x02]))
        self.assertTrue(response.uwb_network_joined)
