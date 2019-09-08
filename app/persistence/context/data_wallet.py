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
        db = pymysql.connect("localhost", "root", "root", "wallet")
        cursor = db.cursor()
        cursor.execute("SELECT max(idwallet_balance) FROM wallet_balance")
        data = cursor.fetchall()
        id_wallet = 0
        current_balance = 0
        for item in data:
            id_wallet = item[0]
            cursor.execute("SELECT balance FROM wallet_balance WHERE idwallet_balance = %s", (id_wallet))
            balance_query = cursor.fetchall()
            for balance_iterator in balance_query:
                current_balance = balance_iterator[0]
            id_wallet = id_wallet + 1
        income_amount = int(wallet.get_income_amount())
        discharge_amount = int(wallet.get_discharge_amount())
        if income_amount > 0:
            balance = current_balance + income_amount
        else:
            balance = current_balance - discharge_amount
        cursor = db.cursor()
        cursor.execute("INSERT INTO wallet_balance (idwallet_balance, income_amount, discharge_amount, balance)"
                       "VALUES(%s, %s, %s, %s)", (id_wallet, income_amount, discharge_amount, balance))

        db.commit()
        cursor.close()
        return 1

