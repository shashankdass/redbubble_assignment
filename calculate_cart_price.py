import json
import sys

from base_prices import BasePrices
from cart import Cart

"""
Command-line utility to find total price of given cart given base prices

How it works:
1) Parse the base price json.
2) Parse the cart and create cart items assigning price to each of them using base prices.
3) Calculate total price.

"""

arguments = sys.argv
# arg check!!
if len(arguments) == 1:
    print("Please pass complete path of the cart json file followed by base price json file")
elif len(arguments) < 3:
    print(
        "One of the path is missing. Please pass complete path of the cart json file followed by base price json file")
else:
    cart_path = sys.argv[1]
    base_price_path = sys.argv[2]

    # Read base price.
    with open(base_price_path) as data_file:
        try:
            base_price_data = json.load(data_file)
        except IOError:
            print("There was an error opening the base price file! Please check the path again")

    # Convert to BasePrices Class.
    base_prices = BasePrices(base_price_data)

    # Read cart.
    with open(cart_path) as data_file:
        try:
            cart_data = json.load(data_file)
        except IOError:
            print("There was an error opening the cart file! Please check the path again")

    # Convert to Cart Class and add cost of each item using base_price.
    cart = Cart(cart_data, base_prices)

    # Calculate the total cost of the cart.
    print("Total cost of your cart is : {}".format(cart.calculate_total_price()))
