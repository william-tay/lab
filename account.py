class Account:
    def __init__(self, name: str) -> None:
        """
        This is just for the constructor. It takes in a name param and sets
        an initial balance of 0 for the account
        :param name: This parameter takes in the name for the account
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float) -> float:
        """
        This is just a function that is used to deposit the money, it will take in the amount param
        and add that to the existing account balance
        :param amount: this is the amount which will be deposited into the account
        :return: returns the balance after depositing the intended amount
        """
        if float(amount) > 0:
            self.account_balance = self.account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> float:
        """
               This is just a function that is used to withdraw the money, it will take in the amount param
               and subtract that from the existing account balance
               :param amount: this is the amount which will be withdrawn into the account
               :return: returns the balance after withdrawing the intended amount
               """
        if 0 < float(amount) < self.account_balance:
            self.account_balance = self.account_balance - amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        all this does is return the current balance
        :return: returns the current account balance
        """
        return self.account_balance

    def get_name(self) -> str:
        """
        all this does is return the current name
        :return: returns the current account name
        """
        return self.account_name
