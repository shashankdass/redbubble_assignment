from collections import defaultdict


class BasePrices:
    def __init__(self):
        self.base_prices = defaultdict(list)

    def __add__(self, other):
        self.base_prices[other.product_type].append(other)


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
            if (color and color in bp.bp_options['colour']):
                if size and size in bp.bp_options['size']:
                    return bp.base_price
            elif not color and size and size in bp.bp_options['size']:
                return  bp.base_price
            elif not color and not size:
                return bp.base_price