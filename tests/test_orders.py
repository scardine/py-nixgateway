import unittest
from nixgateway.api import NixGateway
from settings import key, secret
from uuid import uuid4


class TestCardPayments(unittest.TestCase):
    def setUp(self):
        self.gateway = NixGateway(key, secret)

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

    def test_authorize(self):
        response = self.gateway.orders.card_payments.authorize(
            request_id=str(uuid4()),
            order_id=str(uuid4()),
            amount=100.00,
            card={
                'expirationDate': {
                    'month': '01',
                    'year': '2020'
                },
                'holder': {
                    'name': 'Paulo Scardine',
                    'socialNumber': '64865239804'
                },
                'number': '4916548367656009',
                'securityCode': '111'
            },
            return_url='http://requestb.in/ro6pzmro',
        )
        self.assertIsInstance(response, dict)
        self.assertNotIn('error', response)

    def test_capture(self):
        response = self.gateway.orders.card_payments.authorize(
            request_id=str(uuid4()),
            capture=False,
            order_id=str(uuid4()),
            amount=100.00,
            card={
                'expirationDate': {
                    'month': '01',
                    'year': '2051'
                },
                'holder': {
                    'name': 'Paulo Scardine',
                    'socialNumber': '64865239804'
                },
                'number': '4916548367656009',
                'securityCode': '111'
            },
            return_url='http://requestb.in/ro6pzmro',
        )
        self.assertIsInstance(response, dict)
        self.assertNotIn('error', response)
        self.assertIn('payment', response)
        self.assertIn('paymentToken', response['payment'])
        response = self.gateway.orders.card_payments.capture(
            token=response['payment']['paymentToken'],
            amount=100
        )
        self.assertNotIn('error', response)

    def test_reverse(self):
        response = self.gateway.orders.card_payments.authorize(
            request_id=str(uuid4()),
            capture=False,
            order_id=str(uuid4()),
            amount=100.00,
            card={
                'expirationDate': {
                    'month': '01',
                    'year': '2051'
                },
                'holder': {
                    'name': 'Paulo Scardine',
                    'socialNumber': '64865239804'
                },
                'number': '4916548367656009',
                'securityCode': '111'
            },
            return_url='http://requestb.in/ro6pzmro',
        )
        self.assertIsInstance(response, dict)
        self.assertNotIn('error', response)
        self.assertIn('payment', response)
        self.assertIn('paymentToken', response['payment'])
        response = self.gateway.orders.card_payments.reverse(
            token=response['payment']['paymentToken'],
            amount=100
        )
        self.assertNotIn('error', response)


if __name__ == '__main__':
    unittest.main()
