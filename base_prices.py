from collections import defaultdict

from base_price import BasePriceItem
from constants import ItemConstants, ProductType, ProductOptions


class BasePrices:
    def __init__(self, base_price_json):
        self.base_prices = defaultdict(list)
        for bp in base_price_json:
            if bp:
                bp = BasePriceItem(bp[ItemConstants.PRODUCT_TYPE], bp[ItemConstants.OPTIONS],
                                   bp[ItemConstants.BASE_PRICE])
                self.base_prices[bp.product_type].append(bp)

    def get_base_price(self, product_type, options):
        base_price_list = self.base_prices[product_type]
        try:
            color = options[ProductOptions.COLOR]
        except KeyError:
            color = None
        try:
            size = options[ProductOptions.SIZE]
        except KeyError:
            size = None

        for bp in base_price_list:
            if product_type == ProductType.HOODIE and color in bp.bp_options[ProductOptions.COLOR] and size in \
                    bp.bp_options[ProductOptions.SIZE]:
                return bp.base_price
            elif product_type == ProductType.STICKER and size in bp.bp_options[ProductOptions.SIZE]:
                return bp.base_price
            elif product_type == ProductType.LEGGINGS:
                return bp.base_price
