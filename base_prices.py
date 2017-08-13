from collections import defaultdict

from base_price import BasePriceItem
from constants import ItemConstants


class BasePrices:
    """Represent list of base price items.

    Constructor:
    __init__: creates a base price list out of json items. It also maintains number of unique options for each
            product type.

    Available functions:
    get_base_price : utility function to get the base price of a product given product type and options.

    """
    def __init__(self, base_price_json):
        self.base_prices = defaultdict(list)
        self.option_list_for_product = defaultdict(list)
        for bp in base_price_json:
            if bp:
                bp = BasePriceItem(bp[ItemConstants.PRODUCT_TYPE], bp[ItemConstants.OPTIONS],
                                   bp[ItemConstants.BASE_PRICE])
                if bp.product_type not in self.option_list_for_product:
                    self.option_list_for_product[bp.product_type].extend(list(bp.bp_options.keys()))
                self.base_prices[bp.product_type].append(bp)

    def get_base_price(self, product_type, options):
        base_price_list = self.base_prices[product_type]
        option_list = self.option_list_for_product[product_type]
        for bp in base_price_list:
            if all([options[option] in bp.bp_options[option] for option in option_list]):
                return bp.base_price

        raise Exception("No base price found for given input.")
