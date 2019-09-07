from abc import ABC, abstractmethod
from app.domain.wallet_domain import Wallet as DomainWallet


class IWalletContext(ABC):

    @abstractmethod
    def save_wallet(self, wallet: DomainWallet):
        pass

    @abstractmethod
    def get_balance(self) -> DomainWallet:
        pass
