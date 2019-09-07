from abc import ABC, abstractmethod


class IWalletCommand(ABC):
    @abstractmethod
    def save_wallet(self, income_amount, discharge_amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

