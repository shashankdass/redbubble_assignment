import json
import sys

from base_prices import BasePrices
from cart import Cart


# user_input = True
sample_carts = ["sample_inputs/cart1.json", "sample_inputs/cart2.json", "sample_inputs/cart3.json",
                "sample_inputs/cart4.json"]
default_base_price = "sample_inputs/base_price.json"

arguments = sys.argv
if len(arguments) == 1:
    print("Please pass complete path of the cart json file followed by base price json file")
elif len(arguments) < 3:
    print(
        "One of the path is missing. Please pass complete path of the cart json file followed by base price json file")
else:
    cart_path = sys.argv[1]  # Uncomment for testing : or sample_carts[random.randint(0, 3)]
    print("Cart path:{}".format(cart_path))
    base_price_path = sys.argv[2]  # Uncomment for testing :  or default_base_price
    # Read base price.
    try:
        with open(base_price_path) as data_file:
            base_price_data = json.load(data_file)
    except IOError:
        print("There was an error opening the base price file! Please check the path again")
    # Convert to BasePrices Class.
    base_prices = BasePrices(base_price_data)

    # Read cart.
    try:
        with open(cart_path) as data_file:
            cart_data = json.load(data_file)
    except IOError:
        print("There was an error opening the cart file! Please check the path again")
    # Convert to Cart Class and add cost of each item using base_price.
    cart = Cart(cart_data, base_prices)
    print("Total cost of your cart is : {}".format(cart.calculate_total_price()))
