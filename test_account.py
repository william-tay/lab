import pytest
from account import Account


class Test:
    def setup_method(self):
        self.p1 = Account('Steve')
        self.p2 = Account("Joey")

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_account(self):
        #Withdraw tests
        assert self.p1.withdraw(77) is False
        assert self.p1.withdraw(0) is False
        assert self.p1.withdraw(-100) is False
        assert self.p2.withdraw(-5000) is False
        assert self.p2.withdraw(5000) is False
        assert self.p2.withdraw(0) is False

        #Withdraw test, with money in the account
        assert self.p1.deposit(500) is True
        assert self.p1.withdraw(300) is True
        assert self.p1.withdraw(300) is False

        #Deposit test
        assert self.p1.deposit(-100) is False
        assert self.p1.deposit(0) is False
        assert self.p2.deposit(600) is True
        assert self.p2.deposit(100000000) is True
