clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +

test: clean-pyc
	python calculate_base_price_test.py

run:
	python calculate_cart_price.py
