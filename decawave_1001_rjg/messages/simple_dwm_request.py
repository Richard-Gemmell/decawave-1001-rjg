from .tlv_message import TlvMessage


class SimpleDwmRequest(TlvMessage):
    def __init__(self, type: int):
        super().__init__(bytes([type, 0]))
