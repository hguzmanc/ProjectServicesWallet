import pymysql
from app.domain.wallet_domain import Wallet as DomainWallet
from app.application.persistence.interfaces import IWalletContext


class WalletContext(IWalletContext):

    def get_balance(self) ->[]:
        db = pymysql.connect("localhost", "root", "root", "wallet")
        cursor = db.cursor()
        cursor.execute("SELECT balance FROM wallet_balance where idwallet_balance = (select max(idwallet_balance) From wallet_balance)")
        data = cursor.fetchall()
        wallet = DomainWallet()
        for item in data:
            balance_amount = item[0]
            wallet.set_balance_amount(balance_amount)
        db.close()
        return wallet

    def save_wallet(self, wallet: DomainWallet):
        income_amount = wallet.get_income_amount()
        discharge_amount = wallet.get_discharge_amount()
        balance = wallet.get_balance_amount()
        db = pymysql.connect("localhost", "root", "root", "wallet")
        cursor = db.cursor()
        cursor.execute("INSERT INTO wallet_balance (income_amount, discharge_amount, balance)VALUES (" +
                    income_amount + ", " + discharge_amount + ", " + balance + ")")
        return 1

