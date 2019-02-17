from .dwm_position import DwmPosition
from .dwm_response import DwmResponse


class DwmPositionResponse(DwmResponse):
    def __init__(self, message: bytes):
        super().__init__(message)

    def get_position(self) -> DwmPosition:
        return DwmPosition(self, 5)
