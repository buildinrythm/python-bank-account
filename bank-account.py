from abc import ABC, abstractmethod
#Shared account settings
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
#Savings account settings
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

#Current account settings
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
        print(f"Transaction fee: {self.transactionFee}")
        print("===============================")


# Create test accounts
savings = savingsAccount("S123", 1000, 0.05)
current = currentAccount("C123", 500, 10)

# Test deposit works
savings.depMoney(200)
assert savings.getBalance() == 1200, "Savings deposit failed"

# Test withdraw with insufficient funds (SavingsAccount)
savings.withdrawMoney(1300)  # Should fail
assert savings.getBalance() == 1200, "Savings overdraft allowed incorrectly"

# Test withdraw with fee (CurrentAccount)
current.withdrawMoney(100)  # Fee = 10, total deduction = 110
assert current.getBalance() == 390, "CurrentAccount withdrawal with fee failed"

# Test interest calculation
assert savings.calcInterest() == 1200 * 0.05, "Interest calculation incorrect"

print("All tests passed!")


def getFloatInput(prompt):
    #This is to get a float value from user
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid number. Please enter a numeric value.")

def main():
    print("Welcome to the Bank Program!\n")

    # Ask which account the user wants to create
    account_type = input("Do you want a Savings or Current account? (S/C): ").strip().upper()

    if account_type == "S":
        accountNumber = input("Enter savings account number: ")
        balance = getFloatInput("Enter initial balance for savings account: ")
        interestRate = getFloatInput("Enter interest rate (e.g., 0.05 for 5%): ")
        account = savingsAccount(accountNumber, balance, interestRate)
    elif account_type == "C":
        accountNumber = input("Enter current account number: ")
        balance = getFloatInput("Enter initial balance for current account: ")
        transactionFee = getFloatInput("Enter transaction fee for current account: ")
        account = currentAccount(accountNumber, balance, transactionFee)
    else:
        print("Invalid option. Exiting program.")
        return

    print("\nAccount created successfully!\n")

    # Menu loop
    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Print account summary")
        if account_type == "S":
            print("5. Calculate interest")
            print("6. Exit")
        else:
            print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            deposit = getFloatInput("Enter amount to deposit: ")
            account.depMoney(deposit)
            print(f"Balance after deposit: {account.getBalance()}")
        elif choice == "2":
            withdraw = getFloatInput("Enter amount to withdraw: ")
            account.withdrawMoney(withdraw)
            print(f"Balance after withdrawal: {account.getBalance()}")
        elif choice == "3":
            print(f"Current balance: {account.getBalance()}")
        elif choice == "4":
            account.printSummary()
        elif choice == "5" and account_type == "S":
            print(f"Interest earned: {account.calcInterest()}")
        elif (choice == "5" and account_type == "C") or (choice == "6" and account_type == "S"):
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


