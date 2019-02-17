from .dwm_response import DwmResponse


class DwmStatusResponse(DwmResponse):
    def __init__(self, message: bytes):
        super().__init__(message)

    @property
    def location_ready(self) -> bool:
        return (self[5] & 0x01) != 0

    @property
    def uwb_network_joined(self) -> bool:
        return (self[5] & 0x02) != 0
