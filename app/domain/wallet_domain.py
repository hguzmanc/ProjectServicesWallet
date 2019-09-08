import re
from app.domain.base import Base


class Wallet(Base):
    def __init__(self):
        Base.__init__(self)
        self.__income_amount = 0
        self.__discharge_amount = 0
        self.__balance = 0

    def is_number_income(self, income_amount):
        number = re.match('[0-9]', income_amount)
        if number is not None:
            return True
        return False

    def is_number_discharge(self, discharge_amount):
        number = re.match('[0-9]', discharge_amount)
        if number is not None:
            return True
        return False

    def income_greater_than_or_equal_to_zero(self, income_amount):
        if int(income_amount) >= 0:
            return True
        return False

    def discharge_greater_than_or_equal_to_zero(self, discharge_amount):
        if int(discharge_amount) >= 0:
            return True
        return False

    def set_income_amount(self, income_amount):
        if not self.is_number_income(income_amount):
            raise Exception("The value is not numeric")
        if not self.income_greater_than_or_equal_to_zero(income_amount):
            raise Exception("Entered value is less than 0")
        self.__income_amount = income_amount

    def set_discharge_amount(self, discharge_amount):
        if not self.is_number_discharge(discharge_amount):
            raise Exception("The value is not numeric")
        if not self.discharge_greater_than_or_equal_to_zero(discharge_amount):
            raise Exception("Entered value is less than 0")
        self.__discharge_amount = discharge_amount

    def get_income_amount(self):
        return self.__income_amount

    def get_discharge_amount(self):
        return self.__discharge_amount

    def is_number_balance(self, balance):
        if balance is not None:
            return True
        return False

    def set_balance_amount(self, balance_amount: int):
        if not self.is_number_balance(balance_amount):
            raise Exception("Entered value is less than 0")
        self.__balance = balance_amount

    def get_balance_amount(self):
        return self.__balance

    def to_json(self):
        return {'income_amount': self.get_income_amount(), 'discharge_amount': self.get_discharge_amount(),
                'balance': self.get_balance_amount()}
