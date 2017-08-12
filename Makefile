clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +

test: clean-pyc
	python CalculateBasePriceTest.py

run:
	python calculate_cart_price.py
