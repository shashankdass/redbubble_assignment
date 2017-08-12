from CartItem import CartItem


class Cart:
    def __init__(self, cart_data_json, base_prices):
        self.cart_items = []
        for cart_item in cart_data_json:
            product_type, options = cart_item['product-type'], cart_item['options']
            bp = base_prices.get_base_price(product_type, options)
            if cart_item:
                item = CartItem(cart_item, bp)
                self.cart_items.append(item)

    def calculate_total_price(self):
        total_price = 0
        for item in self.cart_items:
            total_price += item.price
        return total_price

