from .dwm_response import DwmResponse


class DwmConfigResponse(DwmResponse):
    """Returned by a dwm_cfg_get request """
    def __init__(self, message: bytes):
        super().__init__(message)

    @property
    def anchor(self) -> bool:
        return (self[6] & 0x20) != 0

    @property
    def tag(self) -> bool:
        return not self.anchor

    @property
    def initiator(self) -> bool:
        return (self[6] & 0x10) != 0

    @property
    def bridge(self) -> bool:
        return (self[6] & 0x08) != 0

    @property
    def accelerometer_enabled(self) -> bool:
        return (self[6] & 0x04) != 0

    @property
    def two_way_ranging(self) -> bool:
        return (self[6] & 0x03) == 0

    @property
    def low_power_enabled(self) -> bool:
        return (self[5] & 0x80) != 0

    @property
    def location_engine_enabled(self) -> bool:
        return (self[5] & 0x40) != 0

    @property
    def led_enabled(self) -> bool:
        return (self[5] & 0x10) != 0

    @property
    def ble_enabled(self) -> bool:
        return (self[5] & 0x08) != 0

    @property
    def firmware_update_enabled(self) -> bool:
        return (self[5] & 0x04) != 0
