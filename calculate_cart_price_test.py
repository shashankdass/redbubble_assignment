import unittest
import json

from base_prices import BasePrices
from pcart import Cart
from pconstants import ProductType, ProductOptions

TEST_CART_INPUTS = ["sample_inputs/cart1.json", "sample_inputs/cart2.json", "sample_inputs/cart3.json",
                    "sample_inputs/cart4.json"]
EXPECTED_OUTPUTS = [4560, 9363, 9500, 11356]
INPUT_INDEX = 3
TEST_BASE_PRICE = "sample_inputs/base_price.json"
DISTINCT_PRODUCTS = 3


class CartTestCase(unittest.TestCase):
    def setUp(self):
        this_cart = TEST_CART_INPUTS[INPUT_INDEX]
        with open(TEST_BASE_PRICE) as data_file:
            base_price_data = json.load(data_file)
        self.base_prices = BasePrices(base_price_data)
        with open(this_cart) as data_file:
            self.cart_data = json.load(data_file)

    def test_cart_creation(self):
        cart = Cart(self.cart_data, self.base_prices)
        self.assertEqual(len(self.cart_data), len(cart.cart_items))

    def test_total_price_of_cart(self):
        cart = Cart(self.cart_data, self.base_prices)
        self.assertEqual(EXPECTED_OUTPUTS[INPUT_INDEX], (cart.calculate_total_price()))


class BasePriceTestCase(unittest.TestCase):
    def setUp(self):
        with open(TEST_BASE_PRICE) as data_file:
            self.base_price_data = json.load(data_file)

    def test_base_price_creation(self):
        base_prices = BasePrices(self.base_price_data)
        self.assertEqual(len(base_prices.base_prices), DISTINCT_PRODUCTS)

    def test_get_base_price(self):
        base_prices = BasePrices(self.base_price_data)
        bp_small_white_hoodie = base_prices.get_base_price(ProductType.HOODIE, {ProductOptions.COLOR: 'white',
                                                                                ProductOptions.SIZE: 'small'})
        bp_medium_sticker = base_prices.get_base_price(ProductType.STICKER, {ProductOptions.SIZE: 'medium'})
        bp_leggings = base_prices.get_base_price(ProductType.LEGGINGS, {})

        self.assertEqual(bp_small_white_hoodie, 3800)
        self.assertEqual(bp_medium_sticker, 583)
        self.assertEqual(bp_leggings, 5000)


suite1 = unittest.TestLoader().loadTestsFromTestCase(CartTestCase)
suite2 = unittest.TestLoader().loadTestsFromTestCase(BasePriceTestCase)
alltests = unittest.TestSuite([suite1, suite2])
unittest.TextTestRunner(verbosity=2).run(alltests)
