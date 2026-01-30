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

class savingsAccount(Account):
    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber, balance)

        self.interestRate = interestRate

    def calcInterest(self):
        return self.balance * self.interestRate

    def withdrawMoney(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds")
        
    def printSummary(self):
        print("=== Savings Account Summary ===")
        print(f"Account number: {self.accountNumber}")
        print(f"Balance: {self.balance}")
        print(f"Interest rate: {self.interestRate}")
        print("===============================")

class currentAccount(Account):
    def __init__(self, accountNumber, balance, transactionFee):
        super().__init__(accountNumber, balance)

        self.transactionFee = transactionFee

    def withdrawMoney(self, amount):
        if amount + self.transactionFee <= self.balance:
            self.balance = self.balance - (amount + self.transactionFee)
        else:
            print("Insufficient funds")

    def printSummary(self):
        print("=== Current Account Summary ===")
        print(f"Account number: {self.accountNumber}")
        print(f"Balance: {self.balance}")
        print(f"Interest rate: {self.transactionFee}")
        print("===============================")

    