# coding=utf-8
import requests
import time
from jose import jwt
import base64


class Orders(object):
    def __init__(self, gateway):
        self.gateway = gateway

    def get_headers(self):
        return {
            "Authorization": "Bearer {}".format(self.gateway.get_token())
        }

    def card_payments(self, payment_token=None):
        params = {}
        if payment_token is not None:
            if isinstance(payment_token, str):
                url = '{}/Orders/CardPayments/{}'.format(self.gateway.base_url, payment_token)
            elif isinstance(payment_token, (list, tuple)):
                url = '{}/Orders/CardPayments'.format(self.gateway.base_url)
                params = {"paymentToken": payment_token}
            else:
                raise TypeError(u'payment_token should None, list or tuple')
        else:
            url = '{}/Orders/CardPayments'.format(self.gateway.base_url)
        r = requests.get(url, headers=self.get_headers(), params=params)
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


class NixGageway(object):
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





