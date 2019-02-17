import unittest

from decawave_1001_rjg.messages.dwm_config_response import DwmConfigResponse


class TestDwmStatusResponse(unittest.TestCase):
    def test_all_zeros(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x00, 0x00]))
        self.assertFalse(response.anchor)
        self.assertTrue(response.tag)
        self.assertFalse(response.initiator)
        self.assertFalse(response.bridge)
        self.assertFalse(response.accelerometer_enabled)
        self.assertTrue(response.two_way_ranging)
        self.assertFalse(response.low_power_enabled)
        self.assertFalse(response.location_engine_enabled)
        self.assertFalse(response.led_enabled)
        self.assertFalse(response.ble_enabled)
        self.assertFalse(response.firmware_update_enabled)

    def test_anchor(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x00, 0x20]))
        self.assertTrue(response.anchor)
        self.assertFalse(response.tag)

    def test_tag(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x00, 0x00]))
        self.assertTrue(response.tag)
        self.assertFalse(response.anchor)

    def test_initiator(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x00, 0x10]))
        self.assertTrue(response.initiator)

    def test_bridge(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x00, 0x08]))
        self.assertTrue(response.bridge)

    def test_accelerometer_enabled(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x00, 0x04]))
        self.assertTrue(response.accelerometer_enabled)

    def test_two_way_ranging(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x00, 0x00]))
        self.assertTrue(response.two_way_ranging)

    def test_not_two_way_ranging(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x00, 0x03]))
        self.assertFalse(response.two_way_ranging)

    def test_low_power_enabled(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x80, 0x00]))
        self.assertTrue(response.low_power_enabled)

    def test_location_engine_enabled(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x40, 0x00]))
        self.assertTrue(response.location_engine_enabled)

    def test_led_enabled(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x10, 0x00]))
        self.assertTrue(response.led_enabled)

    def test_led_enabled2(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x5A, 0x00]))
        self.assertTrue(response.led_enabled)

    def test_ble_enabled(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x08, 0x00]))
        self.assertTrue(response.ble_enabled)

    def test_firmware_update_enabled(self):
        response = DwmConfigResponse(bytes([0x40, 0x01, 0x00, 0x46, 0x02, 0x04, 0x00]))
        self.assertTrue(response.firmware_update_enabled)

