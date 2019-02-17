from typing import List

from .tlv_message import TlvMessage


class DwmPosition:
    def __init__(self, message: TlvMessage, start_index: int):
        self.message = message
        self.start_index = start_index

    @staticmethod
    def from_properties(position: List[int], quality_factor: int) -> 'DwmPosition':
        data = TlvMessage.from_int32(position[0]) + TlvMessage.from_int32(position[1]) + TlvMessage.from_int32(position[2]) + TlvMessage.from_int8(quality_factor, signed=False)
        return DwmPosition(TlvMessage(data), 0)

    def position(self) -> List[int]:
        start = self.start_index
        x = self.message.int32(start)
        y = self.message.int32(start + 4)
        z = self.message.int32(start + 8)
        return [x, y, z]

    def quality_factor(self) -> int:
        start = self.start_index + 12
        return self.message[start]
