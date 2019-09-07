import re
from html.parser import incomplete

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
        if income_amount >= 0:
            return True
        return False


