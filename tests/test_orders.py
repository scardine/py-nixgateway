import unittest
from nixgateway.api import NixGageway
from settings import key, secret


class TestCardPayments(unittest.TestCase):
    def setUp(self):
        self.gateway = NixGageway(key, secret)

    def test_get(self):
        self.assertIsInstance(self.gateway.orders.card_payments(), list)

    def test_get_with_single_token(self):
        token = 'e7f7fcbd-e0be-4559-902a-3cf4dd101308'
        self.assertIsInstance(self.gateway.orders.card_payments(token), list)

    def test_get_with_multiple_tokens(self):
        tokens = [
            '9f900422-78dc-4ba1-9ad3-68272fa2ae6d',
            '5b0ee391-d49d-4800-a325-6feb37965be1',
            '3d356135-4ed6-4599-aad9-4b4dac69fb2f',
            'b5861054-7b4d-4a9e-8e47-04c4f933e0a1',
        ]
        self.assertIsInstance(self.gateway.orders.card_payments(tokens), list)



if __name__ == '__main__':
    unittest.main()