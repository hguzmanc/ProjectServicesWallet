import unittest
from app.domain.wallet_domain import Wallet

wallet_domain = Wallet


class TestWallet(unittest.TestCase):
    def test_is_number_income(self):
        self.assertTrue(wallet_domain.is_number_income, 50)

    def test_is_number_discharge(self):
        self.assertTrue(wallet_domain.is_number_discharge, 50)

    def test_income_greater_than_or_equal_to_zero(self):
        self.assertTrue(wallet_domain.income_greater_than_or_equal_to_zero, 5)

    def test_discharge_greater_than_or_equal_to_zero(self):
        self.assertTrue(discharge_greater_than_or_equal_to_zero, 5)


if __name__ == '__main__':
    unittest.main()
