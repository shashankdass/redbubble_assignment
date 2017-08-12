import json

from BasePrices import BasePrices
from Cart import Cart

user_input = True
default_cart = "/Users/shashankdass/assignments/redbubble/sample_inputs/cart2.json"
default_base_price = "/Users/shashankdass/assignments/redbubble/sample_inputs/base_price.json"
while user_input:
    print("Enter a valid json path for cart:")
    cart_path = input() or default_cart
    print("Enter a valid json path for base prices:")
    base_price_path = input() or default_base_price

    with open(base_price_path) as data_file:
        base_price_data = json.load(data_file)

    with open(cart_path) as data_file:
        cart_data = json.load(data_file)

    base_prices = BasePrices(base_price_data)

    cart = Cart(cart_data, base_prices)

    print(cart.calculate_total_price())

    print("Enter more input?(y/n)")
    user_input = True if input() == 'y' else False
