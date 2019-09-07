from app.application.presentation.interfaces import IWalletCommand
from app.application.persistence.interfaces import IWalletContext
from app.domain.wallet_domain import Wallet as DomainWallet


class WalletCommand(IWalletCommand):
    def __init__(self, wallet_context: IWalletContext):
        self.wallet_context = wallet_context

    def save_wallet(self, income_amount, discharge_amount):
        balance = self.wallet_context.get_balance()
        wallet = DomainWallet()
        if wallet.set_discharge_amount(discharge_amount) <= balance:
            wallet.set_income_amount(income_amount)
            wallet.set_discharge_amount(discharge_amount)
            self.wallet_context.save_wallet(wallet)
        else:
            raise Exception('Error: Cannot be discounted')

    def get_balance(self):
        balance = self.wallet_context.get_balance()
        return balance

