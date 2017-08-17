from collections import defaultdict

from base_price import BasePriceItem
from constants import ItemConstants


class BasePrices:
    """Represent list of base price items.

    Constructor:
    __init__: creates a base price list out of json items. It also maintains number of unique options for each
            product type.

    Available Functions:
    get_base_price : utility function to get the base price of a product given product type and options.
    get_key_by_options_and_product_type: utility function to get the key according to product type and options.

    Private Functions:
    __get_all_possible_keys__: creates a key in the form of <product_type>_<option_1_value>_<option_2_value>...
    __get_merged_keys__ : helper function to create the key in above mentioned format
    __get_key_helper__: helper function to create the key in above mentioned format

    """

    def __init__(self, base_price_json):
        self.base_prices = defaultdict(list)
        self.option_list_for_product = defaultdict(list)
        for bp in base_price_json:
            if bp:
                bp = BasePriceItem(bp[ItemConstants.PRODUCT_TYPE], bp[ItemConstants.OPTIONS],
                                   bp[ItemConstants.BASE_PRICE])

                if bp.product_type not in self.option_list_for_product:
                    self.option_list_for_product[bp.product_type].extend(sorted(list(bp.bp_options.keys())))
                keys = self.__get_all_possible_keys__(bp, self.option_list_for_product)
                for key in keys:
                    self.base_prices[key].append(bp.base_price)

    def __get_all_possible_keys__(self, bp, option_list_for_product):
        options_present, lists_to_merge, final_keys = option_list_for_product[bp.product_type], [], []
        for option in options_present:
            lists_to_merge.append(bp.bp_options[option])
        merged_keys = self.__get_merged_keys__(lists_to_merge)
        for key in merged_keys:
            final_keys.append(bp.product_type + key)
        return final_keys

    def __get_merged_keys__(self, lists):
        result = []
        self.__get_key_helper__(lists, result, 0, "")
        return result

    def __get_key_helper__(self, lists, result, depth, cur_string):
        if depth == len(lists):
            result.append(cur_string)
            return
        for i in range(len(lists[depth])):
            self.__get_key_helper__(lists, result, depth + 1, cur_string + "_" + lists[depth][i])

    def get_base_price(self, product_type, options):
        option_list = self.option_list_for_product[product_type]
        key = self.get_key_by_options_and_product_type(option_list, options, product_type)
        if key in self.base_prices:
            return self.base_prices[key][0]
        raise Exception("No base price found for given input.")

    def get_key_by_options_and_product_type(self, option_list, options, product_type):
        key, opts = product_type, []
        for option in option_list:
            opts.append(options[option])
        if opts:
            key = "_".join([key, "_".join(opts)])
        return key
