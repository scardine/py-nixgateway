# coding=utf-8
import json

import requests
import time
from jose import jwt
import base64


class CardPayments(object):
    def __init__(self, gateway):
        self._gateway = gateway

    def __call__(self, payment_token=None):
        params = {}
        if payment_token is not None:
            if isinstance(payment_token, str):
                url = '{}/Orders/CardPayments/{}'.format(self._gateway.base_url, payment_token)
            elif isinstance(payment_token, (list, tuple)):
                url = '{}/Orders/CardPayments'.format(self._gateway.base_url)
                params = {"paymentToken": payment_token}
            else:
                raise TypeError(u'payment_token should None, list or tuple')
        else:
            url = '{}/Orders/CardPayments'.format(self._gateway.base_url)
        r = requests.get(url, headers=self._gateway.orders.get_headers(), params=params)
        if r.status_code == 204:
            return []
        try:
            return r.json()
        except ValueError:
            return {
                "error": u"API is not JSON",
                "status_code": r.status_code,
                "response": r.text,
            }

    def authorize(self, request_id, order_id, amount, card, return_url, customer=None, recurrence=None, installments=1,
                  capture=True, transaction_type=1):
        payload = {
            "installments": installments,
            "capture": capture,
            "merchantOrderId": order_id,
            "amount": int(amount * 100),
            "card": card,
        }
        if customer is not None:
            payload['customer'] = customer

        if recurrence is not None:
            payload['recurrence'] = recurrence

        if return_url is not None:
            payload['returnUrl'] = return_url

        if transaction_type is not None:
            payload['transactionType'] = transaction_type

        headers = self._gateway.orders.get_headers(request_id)
        url = self._gateway.base_url + '/Orders/CardPayments/Authorize'
        r = requests.post(url, headers=headers, json=payload)
        if r.status_code == 200:
            return r.json()
        return {
            "error": "Response was not HTTP 200",
            "status_code": r.status_code,
            "response": r.text,
        }


class Orders(object):
    def __init__(self, gateway):
        self.card_payments = CardPayments(gateway)
        self._gateway = gateway

    def get_headers(self, request_id=None):
        headers = {
            "Authorization": "Bearer {}".format(self._gateway.get_token())
        }
        if request_id is not None:
            headers['requestId'] = request_id
        return headers


class NixGateway(object):
    def __init__(self, key, secret, token_ttl=3600, base_url='https://gateway-ypqai.nexxera.com/v2'):
        self.key = key
        self.secret = base64.b64decode(secret)
        self.token_ttl = token_ttl
        self.base_url = base_url
        self.auth = {
            "token": None,
            "expires": 0,
        }
        self.orders = Orders(self)

    def get_token(self):
        if self.auth['token'] and self.auth['expires'] > time.time():
            return self.auth['token']

        expires = time.time() + self.token_ttl
        payload = {
           "iss": self.key,
           "access":
           [
              "cardPayments",
              "recurrencePlans",
              "recurrences",
              "checkout",
              "boletoPayments"
           ],
           "exp": expires,
        }

        signed = jwt.encode(payload, self.secret, algorithm='HS256')
        self.auth['token'] = signed
        self.auth['expires'] = expires

        return self.auth['token']





