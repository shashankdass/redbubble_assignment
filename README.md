Architectural Overview:
(Python 3 installation required.)
==========================================================================

Get File Input --> Parse Input --> Create base price data structure -->
Use it to calculate the price of each item in cart -->  Show total price
==========================================================================

There are couple of ways you can run this program:
1) Using provided makefile

a) Run program:  Using the default file provided with this package

		   command: ``` make run ```
		   effect: uses one of the cart and provided base_price file

b) Run Test

	 command: ``` make test ```

2) Directly using the python program

	a) Running with stdin

		command : ``` python  calculate_cart_price.py <complete_path_to_cart> <complete_path_to_base_price_file>```
        If User does not enter any input, it prints error and comes out.

	b) Running test directly

		command: ```python calculate_cart_price_test.py```

I generated some code coverage report using python "coverage" tool.

To install coverage tool:
``` pip install coverage ```

To generate coverage :
``` coverage run calculate_cart_price_test.py ```

To look at the report:
``` coverage report ```

To generat  html format report:
``` coverage html ```
``` open htmlcov/index.html ```