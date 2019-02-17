import unittest

from decawave_1001_rjg.messages.tlv_message import TlvMessage


class TestTlvMessage(unittest.TestCase):
    def test_get_type(self):
        message = TlvMessage(bytes([0x02, 0x04, 0x01, 0x02, 0x03, 0x04]))
        self.assertEqual(0x02, message.type())

    def test_get_length(self):
        message = TlvMessage(bytes([0x02, 0x04, 0x01, 0x02, 0x03, 0x04]))
        self.assertEqual(0x04, message.length())

    def test_get_value(self):
        message = TlvMessage(bytes([0x02, 0x04, 0x01, 0x02, 0x03, 0x04]))
        self.assertEqual(bytes([0x01, 0x02, 0x03, 0x04]), message.value())

    def test_repr(self):
        message = TlvMessage(bytes([0x02, 0x04, 0x01, 0x02, 0x03, 0x04]))
        self.assertEqual(message.__repr__(), "b'\\x02\\x04\\x01\\x02\\x03\\x04'")

    def test_get_item(self):
        message = TlvMessage(bytes([0x02, 0x04, 0x01, 0x02, 0x03, 0x04]))
        self.assertEqual(0x03, message[4])

    def test_get_item_index_out_of_range(self):
        message = TlvMessage(b'\x02\x04\x01\x02\x03\x04')
        with self.assertRaises(IndexError):
            a = message[-1]
        with self.assertRaises(IndexError):
            a = message[6]

    def test_from_int8(self):
        expected = bytes([0x80])
        self.assertEqual(expected, TlvMessage.from_int8(-128))

    def test_from_negative_int8(self):
        expected = bytes([0x7F])
        self.assertEqual(expected, TlvMessage.from_int8(127))

    def test_from_unsigned_int8(self):
        expected = bytes([0xFF])
        self.assertEqual(expected, TlvMessage.from_int8(255, False))

    def test_get_int_16(self):
        message = TlvMessage(bytes([0x02, 0x04, 0x01, 0x02, 0x03, 0x04]))
        self.assertEqual(260, message.int16(1))

    def test_get_negative_int_16(self):
        message = TlvMessage(bytes([0x02, 0x8B, 0xFF, 0x02, 0x03, 0x04]))
        self.assertEqual(-117, message.int16(1))

    def test_get_unsigned_int_16(self):
        message = TlvMessage(bytes([0x02, 0x8B, 0xFF, 0x02, 0x03, 0x04]))
        self.assertEqual(65419, message.int16(1, False))

    def test_int16_index_out_of_range(self):
        message = TlvMessage(b'\x02\x04\x01\x02\x03\x04')
        with self.assertRaises(IndexError):
            message.int16(5)

    def test_from_int16(self):
        expected = bytes([0x04, 0x01])
        self.assertEqual(expected, TlvMessage.from_int16(260))

    def test_from_negative_int16(self):
        expected = bytes([0x8B, 0xFF])
        self.assertEqual(expected, TlvMessage.from_int16(-117))

    def test_from_unsigned_int16(self):
        expected = bytes([0x8B, 0xFF])
        self.assertEqual(expected, TlvMessage.from_int16(65419, False))

    def test_get_int_32(self):
        message = TlvMessage(bytes([0x02, 0x04, 0x01, 0x02, 0x03, 0x04]))
        self.assertEqual(50462980, message.int32(1))

    def test_get_negative_int_32(self):
        message = TlvMessage(bytes([0x02, 0x8B, 0xFF, 0xFF, 0xFF, 0x04]))
        self.assertEqual(-117, message.int32(1))

    def test_get_unsigned_int_32(self):
        message = TlvMessage(bytes([0x02, 0x8B, 0xFF, 0xFF, 0xFF, 0x04]))
        self.assertEqual(4294967179, message.int32(1, False))

    def test_int32_index_out_of_range(self):
        message = TlvMessage(b'\x02\x04\x01\x02\x03\x04')
        with self.assertRaises(IndexError):
            message.int32(5)

    def test_from_int32(self):
        expected = bytes([0x04, 0x01, 0x02, 0x03])
        self.assertEqual(expected, TlvMessage.from_int32(50462980))

    def test_from_negative_int32(self):
        expected = bytes([0x8B, 0xFF, 0xFF, 0xFF])
        self.assertEqual(expected, TlvMessage.from_int32(-117))

    def test_from_unsigned_int32(self):
        expected = bytes([0x8B, 0xFF, 0xFF, 0xFF])
        self.assertEqual(expected, TlvMessage.from_int32(4294967179, False))

    def test_to_hex_string(self):
        message = TlvMessage(bytes([0x02, 0x04, 0x2A, 0x00, 0xCA, 0xDE]))
        print(message.int32(2, False))
        string = message.int_to_hex_string(message.int32(2, False))
        self.assertEqual('DECA002A', string)

    def test_from_hex_string(self):
        data = TlvMessage.hex_string_to_int('DECA002A')
        self.assertEqual(3737780266, data)
