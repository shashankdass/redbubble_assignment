class BasePriceItem:
    def __init__(self, product_type=None, bp_options=None, base_price=None):
        self.product_type = product_type
        self.bp_options = bp_options
        self.base_price = base_price

class BasePriceOption:
    def __init__(self, color=None, size=None):
        self.color = color
        self.size = size