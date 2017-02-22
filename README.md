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

    from nixgateway import NixGateway
    ngw = NixGateway(key, secret)
     
Now you can call API methods as native Python methods:

    ngw.orders.card_payments()

Method Mapping
--------------

The following rules are used:

  * slashes from an endpoint are converted to dots
  * path components and argument names are converted from CamelCase to snake_case. 

For exemple, an endpoint like `/Orders/CardPayments/Authorize` is mapped
to `orders.card_payments.authorize()`. 


Support
-------

Issues will be dealt with in a "best effort" capacity. When raising issues, 
always be very polite or they will be promptly closed. Volunteers here are not
your employees, please hold no expectation about them solving 
your problems or responding in a timely manner.

Pull requests are welcome.
 





