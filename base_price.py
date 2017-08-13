class BasePriceItem:
    """Represents a base price item.

    Used by BasePrices to create base price item.

    Constructor:
    used to construct the item.

    """
    def __init__(self, product_type=None, bp_options=None, base_price=None):
        self.product_type = product_type
        self.bp_options = bp_options
        self.base_price = base_price
