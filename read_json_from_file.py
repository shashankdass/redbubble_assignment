import json
from pprint import pprint
from BasePrices import BasePrices
from BasePrice import BasePriceItem,BasePriceOption
from Cart import Cart
from CartItem import CartItem

user_input = True
default_cart = "/Users/shashankdass/assignments/redbubble/sample_inputs/cart2.json"
default_base_price = "/Users/shashankdass/assignments/redbubble/sample_inputs/base_price.json"
while user_input:
    print("Enter a valid json path for cart:")
    cart_path = input() or default_cart
    print ("Enter a valid json path for base prices:")
    base_price_path = input() or default_base_price

    with open(base_price_path) as data_file:
        base_price_data = json.load(data_file)

    with open(cart_path) as data_file:
        cart_data = json.load(data_file)

    base_prices = BasePrices()
    for bp in base_price_data:
        if bp:
            bp = BasePriceItem(bp['product-type'], bp['options'], bp['base-price'])
            base_prices + bp

    cart = Cart()
    for cart_item in cart_data:
        pprint(cart_item)
        item = CartItem()
        product_type = cart_item['product-type']
        options = cart_item['options']
        bp = base_prices.get_base_price(product_type, options)
        if cart_item:
            item = CartItem(product_type, cart_item['options'], cart_item['artist-markup'], cart_item['quantity'], bp)
            cart + item
    print(cart.calculate_total_price())

    print("Enter more input?(y/n)")
    user_input = True if input() == 'y' else False
