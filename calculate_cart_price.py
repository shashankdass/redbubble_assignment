import json
import random

from base_prices import BasePrices
from cart import Cart

user_input = True
sample_carts = ["sample_inputs/cart1.json", "sample_inputs/cart2.json", "sample_inputs/cart3.json",
                "sample_inputs/cart4.json"]
default_base_price = "sample_inputs/base_price.json"
while user_input:
    print("Enter a valid json path for cart:")
    cart_path = input() or sample_carts[random.randint(0, 3)]
    print("Cart path:{}".format(cart_path))
    print("Enter a valid json path for base prices:")
    base_price_path = input() or default_base_price
    # Read base price.
    with open(base_price_path) as data_file:
        base_price_data = json.load(data_file)
    # Read cart.
    with open(cart_path) as data_file:
        cart_data = json.load(data_file)
    # Convert to BasePrices Class.
    base_prices = BasePrices(base_price_data)
    # Convert to Cart Class and add cost of each item using base_price.
    cart = Cart(cart_data, base_prices)

    print("Total cost of your cart is : {}".format(cart.calculate_total_price()))

    print("Enter more input?(y/n)")
    user_input = True if input() == 'y' else False
