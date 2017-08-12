import unittest

from credit_card_bt import CreditCard, CreditCardProvider
from credit_card_enums import Operations

NAME_VALID = "Test_valid"
NAME_INVALID = "Test_invalid"
LIMIT = "$1000"
VALID_CC_NUMBER = "4111111111111111"
INVALID_CC_NUMBER = "1234567890123456"


class CreditCardTestCase(unittest.TestCase):
    def setUp(self):
        self.valid_credit_card = CreditCard(NAME_VALID, VALID_CC_NUMBER, LIMIT)
        self.invalid_credit_card = CreditCard(NAME_INVALID, INVALID_CC_NUMBER, LIMIT)

    def test_valid_credit_card_constructor(self):
        cc = self.valid_credit_card
        self.assertTrue(cc.valid)

    def test_invalid_credit_card_constructor(self):
        cc = self.invalid_credit_card
        self.assertFalse(cc.valid)

    def test_static_luhn_checksum(self):
        self.assertEquals(CreditCard.luhn_checksum(VALID_CC_NUMBER), 0)
        self.assertNotEquals(CreditCard.luhn_checksum(INVALID_CC_NUMBER), 0)

    def test_is_valid_card(self):
        self.assertTrue(CreditCard.is_valid_card(VALID_CC_NUMBER))
        self.assertFalse(CreditCard.is_valid_card(INVALID_CC_NUMBER))


class CreditCardProviderTestCase(unittest.TestCase):
    def setUp(self):
        self.valid_credit_card = CreditCard(NAME_VALID, VALID_CC_NUMBER, LIMIT)
        self.invalid_credit_card = CreditCard(NAME_INVALID, INVALID_CC_NUMBER, LIMIT)
        self.ccp = CreditCardProvider()

    def test_add_card(self):
        self.ccp.add_card(self.valid_credit_card)
        self.ccp.add_card(self.invalid_credit_card)
        self.assertEquals(len(self.ccp.credit_cards), 2)

    def test_charge_card(self):
        CHARGE = "$500"
        self.ccp.add_card(self.valid_credit_card)
        self.ccp.charge_card(NAME_VALID, CHARGE)
        self.assertEquals(len(self.ccp.credit_cards), 1)
        self.assertEquals("$" + self.ccp.credit_cards[NAME_VALID].balance, CHARGE)

    def test_add_credit_to_card(self):
        CREDIT = "$100"
        self.ccp.add_card(self.valid_credit_card)
        cur_balance = self.valid_credit_card.balance
        self.ccp.add_credit_to_card(NAME_VALID, CREDIT)
        self.assertLess(int(self.valid_credit_card.balance), 0)
        self.assertEquals(self.valid_credit_card.balance, str(cur_balance - int(CREDIT.split("$")[1])))

    def test_is_valid_operation(self):
        self.ccp = CreditCardProvider()
        operations = [Operations.CHARGE, Operations.CREDIT]
        for operation in operations:
            self.assertFalse(self.ccp.is_valid_operation(operation, self.invalid_credit_card, 500))
            if operation == Operations.CHARGE:
                self.assertTrue(self.ccp.is_valid_operation(operation, self.valid_credit_card, 999))
                self.assertFalse(self.ccp.is_valid_operation(operation, self.valid_credit_card, 1001))
            else:
                self.assertTrue(self.ccp.is_valid_operation(operation, self.valid_credit_card, 500))

    def test_show_summary(self):
        self.ccp.add_card(self.valid_credit_card)
        self.ccp.add_card(self.invalid_credit_card)
        expected_string = "\n"
        expected_string += "%s: %s" % (NAME_INVALID, "error")
        expected_string += "\n"
        expected_string += "%s: %s" % (NAME_VALID, "$0")
        self.assertEqual(expected_string, self.ccp.show_summary())


suite1 = unittest.TestLoader().loadTestsFromTestCase(CreditCardTestCase)
suite2 = unittest.TestLoader().loadTestsFromTestCase(CreditCardProviderTestCase)
alltests = unittest.TestSuite([suite1, suite2])
unittest.TextTestRunner(verbosity=2).run(alltests)
