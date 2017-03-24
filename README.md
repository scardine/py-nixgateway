Py-NixGateway
=============

This project is an **unofficial** python client to the Nix Gateway API, 
Nexxera's payment gateway.

**disclaimer**: THIS IS NOT OFFICIALLY SUPPORTED BY NEXXERA

For more information refer to their official support channel: 

https://web-nix.cloud.nexxera.com/index.php/suporte/


Running the tests
-----------------

First, you must get your API `key` and `secret` from mep@nexxera.com. 
In order to run the tests, fill the values in `tests/settings.example.py`
and rename it to `tests/settings.py`, then run `python -m unittest discover`.


Instantiating the API client
----------------------------

You must have your API credentials at hand:

    from nixgateway.api import NixGateway
    ngw = NixGateway(key, secret)
     
Now you can call API methods as native Python methods:

    ngw.orders.card_payments()

Method Mapping
--------------

The following rules are used:

  * slashes from an endpoint are converted to dots
  * path components and argument names are converted from CamelCase to snake_case.
  * first level json keys from the JSON payload are converted to Python function arguments

For exemple, an endpoint like `/Orders/CardPayments/Authorize` is mapped
to `orders.card_payments.authorize()`. 

    In [3]: ngw.orders.card_payments.authorize({
      "capture": false,
      "order_id": "a3a82307-fff7-4213-9233-19531c24d272",
      "amount": 100.0,
      "card": {
        "securityCode": "111",
        "holder": {
           "socialNumber": "64865239804",
           "name": "Paulo Scardine"
        },
        "expirationDate": {
          "year": "2051",
          "month": "01"
        },
        "number": "5194111171117780"
      },
      "request_id": "934f1662-eb93-4c1e-9ea4-173f6a573605",
      "return_url": "http://requestb.in/1ca4hkh1"
    })
    Out[3]: {
      "merchantOrderId": "a3a82307-fff7-4213-9233-19531c24d272",
      "payment": {
        "reversals": [],
        "recurrencePlan": null,
        "authenticationUrl": null,
        "paymentToken": "bcc6bf76-2ca6-4245-9fe3-3a05a0d859de",
        "card": {
          "cardBrand": "Mastercard",
          "cardNumber": "519411******7780",
          "holder": null
        },
        "customer": null,
        "paymentStatus": 1,
        "amount": 10000,
        "captures": [],
        "authorization": {
          "authorizationCode": "bf3cbb", 
          "amount": 10000,
          "returnCode": "0000",
          "processedDate": "2017-03-24T11:21:51.7665085-03:00",
          "proofOfSale": "34571"
        },
        "transactionType": 1
      }
    }


Support
-------

Issues will be dealt with in a "best effort" capacity. When raising issues, 
always be very polite or they will be promptly closed. Volunteers here are not
your employees, please hold no expectation about them solving 
your problems or responding in a timely manner.

Pull requests are welcome.
 





