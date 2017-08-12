import json
from pprint import pprint


user_input = True
while user_input:
    print("Enter a valid json path for cart:")
    cart_path = input()
    print ("Enter a valid json path for base prices:")
    base_price_path = input()

    with open(base_price_path) as data_file:
        base_price_data = json.load(data_file)

    with open(cart_path) as data_file:
        cart_data = json.load(data_file)

    pprint(cart_data)
    pprint(base_price_data)
    print("Enter more input?(y/n)")
    user_input = True if input() == 'y' else False
