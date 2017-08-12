class CartItem:
    def __init__(self, product_type=None, options=None, artist_markup=None, quantity=None, base_price=None):
        """

        :param product_type:
        :param options:
        :param artist_markup:
        :param quantity:
        :param price:
        """
        self.product_type = product_type
        self.options = options
        self.artist_markup = artist_markup
        self.quantity = quantity
        self.price = None
        if base_price:
             self.price = (base_price + round(base_price * artist_markup)) * quantity


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
