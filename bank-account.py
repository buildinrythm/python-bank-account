from abc import ABC, abstractmethod

class Account:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    @abstractmethod
    def depMoney():
        pass

    @abstractmethod
    def withdrawMoney():
        pass

    @abstractmethod
    def getBalance():
        pass

class savingsAccount:
    pass

class currentAccount:
    pass