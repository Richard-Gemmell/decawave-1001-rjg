from .dwm_response import DwmResponse


class DwmVersionResponse(DwmResponse):
    """Returned by a dwm_ver_get request """

    def __init__(self, message: bytes):
        super().__init__(message)

    def get_firmware_version(self) -> str:
        return '{}.{}.{}.{}'.format(self.message[5], self.message[6], self.message[7], self.message[8] & 0x0F)

    def get_configuration_version(self) -> str:
        return self.int_to_hex_string(self.int32(11, False))

    def get_hardware_version(self) -> str:
        return self.int_to_hex_string(self.int32(17, False))
