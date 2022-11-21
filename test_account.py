import pytest
from account import Account


class Test:
    decimal = 0.0001

    def setup_method(self):
        self.p1 = Account('Steve')
        self.p2 = Account("Joey")

    def teardown_method(self):
        del self.p1
        del self.p2

    def test__init__(self):
        assert self.p1.get_name() == "Steve"
        assert self.p2.get_name() == "Joey"
        assert self.p2.get_balance() == 0

    def test_withdraw(self):
        # Withdraw tests
        assert self.p1.withdraw(77) is False
        assert self.p1.get_balance() is 0

        self.p1.deposit(100.50)
        assert self.p1.withdraw(0) is False
        pytest.approx(self.p1.get_balance(), rel=self.decimal) is 100.50
        assert self.p1.withdraw(100) is True
        pytest.approx(self.p1.get_balance(), rel=self.decimal) is .50
        assert self.p1.withdraw(0.5) is True

        # Negatives
        self.p2.deposit(50)
        assert self.p2.withdraw(-100) is False
        assert self.p2.withdraw(-5000) is False

        assert self.p2.get_balance() is 50

        assert self.p2.withdraw(50) is True

        # Zeros
        assert self.p2.withdraw(0) is False

        assert self.p2.get_balance() is 0

        #
        assert self.p1.withdraw(300) is False
        assert self.p1.withdraw(300) is False

        pytest.approx(self.p1.get_balance(), rel=self.decimal) is 0


    def test_deposit(self):

        assert self.p1.deposit(50) is True
        pytest.approx(self.p1.get_balance(), rel=self.decimal) is 50

        assert self.p1.deposit(-100) is False

        assert self.p1.deposit(0) is False
        pytest.approx(self.p1.get_balance(), rel=self.decimal) is 50
        assert self.p2.deposit(600) is True
        pytest.approx(self.p2.get_balance(), rel=self.decimal) is 600
        assert self.p2.deposit(100) is True
        pytest.approx(self.p1.get_balance(), rel=self.decimal) is 700
