class BankAccount:
    #dont forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0):
        self.balance = balance
        self.interest = int_rate
        pass
    def deposit(self, amount):
        self.balance += amount
        print(f"Added ${amount}")
        print("Balance: $" + str(self.balance))
        return self
        pass
    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}")
            print("Balance: $" + str(self.balance))
        else:
            self.balance -= 5
            print(f"Error trying to withdraw ${amount}")
            print("Insufficient Funds: Charging a $5 fee")
            print("Balance: $" + str(self.balance))
        return self
        pass
    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self
        pass
    def yield_interest(self):
        gain = self.balance * self.interest
        if self.balance > 0:
            print(f"Yielded ${gain} from interest!")
            self.balance += self.balance * self.interest
            print("Balance: $" + str(self.balance))
        else:
            print("Error: Balance too low to Yield Interest.")
            print("Balance: $" + str(self.balance))
        return self
        pass
jack = BankAccount(0.2, 800)
sam = BankAccount(0.21, 2000)

jack.deposit(111).deposit(222).deposit(333).withdraw(3000).yield_interest().display_account_info()

sam.deposit(117).deposit(151).withdraw(420).withdraw(365).withdraw(222).withdraw(334).yield_interest().display_account_info()