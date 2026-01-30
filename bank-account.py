from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    
    def depMoney(self, amount):
        self.balance = self.balance + amount
        return self.balance

    @abstractmethod
    def withdrawMoney(self, amount):
        pass

    
    def getBalance(self):
        return self.balance

    @abstractmethod
    def printSummary(self):
        pass

class savingsAccount:
    pass

class currentAccount:
    pass