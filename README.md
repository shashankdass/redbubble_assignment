Architectural Overview:
(Python 3 installation required.)
==========================================================================

FileInput---------
                  |-----|Parse Input
StdIN-------------      |
						|
					   \|/
					   Create base price data structure
					    |
						|
					   \|/
					   Use it to calculate the price of cart
					    |
						|
					   \|/
					   Show total price

==========================================================================

There are couple of ways you can run this program:
1) Using provided makefile

	a) Run program:  Using the default file provided with this package
		command: ``` make run ```
	b) Run Test
	    command: ``` make test ```
2) Directly using the python program
	a) Running with stdin
		command : ``` python  calculate_cart_price.py ```
        This will prompt user to enter path to base price file and cart file.
        If User does not enter any input I am using the default input that is provided.


I generated some code coverage report using python coverage tool.

To install coverage tool:
``` pip install coverage```

To generate coverage :
```coverage run test_cc_bt.py ```

To look at the report:
```coverage report```

To generat  html format report:
```coverage html```
``` open htmlcov/index.html```