class TlvMessage:
    def __init__(self, message: bytes):
        self.message = message

    def type(self) -> int:
        return self.message[0]

    def length(self) -> int:
        return self.message[1]

    def value(self) -> bytes:
        return self.message[2:]

    def __repr__(self):
        return self.message.__repr__()

    def __getitem__(self, item: int) -> int:
        """Returns the 8 bit integer value at the given index"""
        self._assert_range(item, item)
        return self.message[item]

    def int16(self, index: int, signed: bool = True) -> int:
        end = index + 2
        self._assert_range(index, end)
        return int.from_bytes(self.message[index:end], byteorder='little', signed=signed)

    @staticmethod
    def from_int8(value: int, signed: bool = True) -> bytes:
        return int.to_bytes(value, length=1, byteorder='little', signed=signed)

    @staticmethod
    def from_int16(value: int, signed: bool = True) -> bytes:
        return int.to_bytes(value, length=2, byteorder='little', signed=signed)

    def int32(self, index: int, signed: bool = True) -> int:
        end = index + 4
        self._assert_range(index, end)
        return int.from_bytes(self.message[index:end], byteorder='little', signed=signed)

    @staticmethod
    def from_int32(value: int, signed: bool = True) -> bytes:
        return int.to_bytes(value, length=4, byteorder='little', signed=signed)

    @staticmethod
    def int_to_hex_string(value: int) -> str:
        return '{:X}'.format(value)

    @staticmethod
    def hex_string_to_int(value: str) -> int:
        return int(value, base=16)

    def _assert_range(self, start: int, end: int):
        if start < 0 or end > len(self.message):
            raise IndexError
