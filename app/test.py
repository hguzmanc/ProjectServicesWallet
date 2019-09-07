import unittest
from app.domain.wallet_domain import Wallet
from app.command.wallet_command import WalletCommand

wallet_domain = Wallet
wallet_command = WalletCommand


class TestWalletDomain(unittest.TestCase):
    def test_is_number_income(self):
        self.assertTrue(wallet_domain.is_number_income, 50)

    def test_is_number_discharge(self):
        self.assertTrue(wallet_domain.is_number_discharge, 50)

    def test_income_greater_than_or_equal_to_zero(self):
        self.assertTrue(wallet_domain.income_greater_than_or_equal_to_zero, 5)

    def test_discharge_greater_than_or_equal_to_zero(self):
        self.assertTrue(wallet_domain.discharge_greater_than_or_equal_to_zero, 5)

    def test_balance_is_none(self):
        self.assertTrue(wallet_domain.is_number_balance, 3)


if __name__ == '__main__':
    unittest.main()
