from cart_item import CartItem
from constants import ItemConstants


class Cart:
    def __init__(self, cart_data_json, base_prices):
        self.cart_items = []
        for cart_item in cart_data_json:
            product_type, options = cart_item[ItemConstants.PRODUCT_TYPE], cart_item[ItemConstants.OPTIONS]
            bp = base_prices.get_base_price(product_type, options)
            item = CartItem(cart_item, bp)
            self.cart_items.append(item)

    def calculate_total_price(self):
        return sum([item.price for item in self.cart_items])
