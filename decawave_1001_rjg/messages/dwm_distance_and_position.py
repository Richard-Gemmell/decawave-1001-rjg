from .dwm_position import DwmPosition
from .tlv_message import TlvMessage


class DwmDistanceAndPosition:
    def __init__(self, message: TlvMessage, start_index: int):
        self.message = message
        self.start_index = start_index

    @staticmethod
    def from_properties(address: str, distance: int, quality_factor: int, position: DwmPosition) -> 'DwmDistanceAndPosition':
        address_int = TlvMessage.hex_string_to_int(address)
        address_bytes = TlvMessage.from_int16(address_int, False)
        built_pos = DwmPosition.from_properties(position.position(), position.quality_factor())
        data = address_bytes + TlvMessage.from_int32(distance) + TlvMessage.from_int8(quality_factor) + built_pos.message.message
        return DwmDistanceAndPosition(TlvMessage(data), 0)

    def address(self) -> str:
        return self.message.int_to_hex_string(self.message.int16(self.start_index, False))

    def distance(self) -> int:
        return self.message.int32(self.start_index+2)

    def quality_factor(self) -> int:
        return self.message[self.start_index+6]

    def position(self) -> DwmPosition:
        return DwmPosition(self.message, self.start_index+7)


