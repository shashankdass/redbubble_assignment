from  pconstants import ItemConstants


class CartItem:
    def __init__(self, cart_item_json, base_price=None):
        self.product_type = cart_item_json[ItemConstants.PRODUCT_TYPE]
        self.options = cart_item_json[ItemConstants.OPTIONS]
        self.artist_markup = cart_item_json[ItemConstants.ARTIST_MARKUP]
        self.quantity = cart_item_json[ItemConstants.QUANTITY]
        self.price = None
        if base_price:
            self.price = (base_price + round((base_price * self.artist_markup) / 100)) * self.quantity
