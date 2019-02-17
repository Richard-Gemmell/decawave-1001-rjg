import unittest

from decawave_1001_rjg.messages.simple_dwm_request import SimpleDwmRequest


class SimpleDwmRequestTest(unittest.TestCase):
    def test_constructor(self):
        message = SimpleDwmRequest(123)
        self.assertEqual(bytes([123, 0]), message.message)
        self.assertEqual(123, message.type())
        self.assertEqual(0, message.length())