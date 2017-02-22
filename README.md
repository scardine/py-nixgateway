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

Issues will be dealed in a "best effort" capacity - be always very 
polite or your issues will be closed right way. Volunteers here are not
your employees and you should have no expectation about we solving 
your problems. Pull requests are welcome, criticism from free-riders 
is not.
 





