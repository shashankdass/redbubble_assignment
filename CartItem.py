class CartItem:
    def __init__(self, cart_item_json, base_price=None):
        self.product_type = cart_item_json['product-type']
        self.options = cart_item_json['options']
        self.artist_markup = cart_item_json['artist-markup']
        self.quantity = cart_item_json['quantity']
        self.price = None
        if base_price:
            self.price = (base_price + round(base_price * self.artist_markup)) * self.quantity


class CartOptions:
    def __init__(self, size=None, color=None, print_location=None):
        """

        :param size:
        :param color:
        :param print_location:
        """
        self.size = size
        self.color = color
        self.print_location = print_location
