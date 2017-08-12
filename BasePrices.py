from collections import defaultdict

from BasePrice import BasePriceItem


class BasePrices:
    def __init__(self, base_price_json):
        self.base_prices = defaultdict(list)
        for bp in base_price_json:
            if bp:
                bp = BasePriceItem(bp['product-type'], bp['options'], bp['base-price'])
                self.base_prices[bp.product_type].append(bp)


    def get_base_price(self, product_type, options):
        base_price_list = self.base_prices[product_type]
        try:
            color = options['colour']
        except KeyError:
            color = None
        try:
            size = options['size']
        except KeyError:
            size = None

        for bp in base_price_list:
            if product_type == 'hoodie' and color in bp.bp_options['colour'] and size in bp.bp_options['size']:
                return bp.base_price
            elif product_type == 'sticker' and size in bp.bp_options['size']:
                return bp.base_price
            elif product_type == 'leggings':
                return bp.base_price
