from .tlv_message import TlvMessage


class DwmInterruptConfigRequest(TlvMessage):
    def __init__(self, loc_ready: bool, spi_data_ready: bool):
        value = 0x00
        if loc_ready:
            value = value | 0x01
        if spi_data_ready:
            value = value | 0x02
        super().__init__(bytes([0x34, 1, value]))
