class Balanceable:
    def getBalance(self):
        pass
    def setBalance(self, amount):
        pass

class Depositable:
    def deposit(self, amount):
        pass

class Withdrawable:
    def withdraw(self, amount):
        pass

class Account(Balanceable, Depositable, Withdrawable):

    balance = 0.0
    def getBalance(self):
        return self.balance

    def setBalance(self, amount):
        self.balance = amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

class CheckingAccount(Account):
    monthlyFee = 0.0

    def __init__(self, fee):
        self.monthlyFee = fee

    def getMonthlyFee(self):
        return self.monthlyFee

    def balMonFee(self):
        self.balance = self.balance - self.monthlyFee

class SavingsAccount(Account):
    monIntRate = 0.0
    monIntPay = 0.0

    def __init__(self, rate):
        self.monIntRate = rate

    def calcPay(self):
        self.monIntPay = self.balance * self.monIntRate
        self.balance = self.balance + self.monIntPay

    def getMonIntPay(self):
        return self.monIntPay


class Transactions:
    def deposit(self, Depositable, amount):
        Depositable.deposit(amount)

    def withdraw(self, Withdrawable, amount):
        Withdrawable.withdraw(amount)

class Validator:

    def wOrD(self):
        response = input("Withdrawl or deposit? (w/d): ")
        while (response != "w" and response != "d"):
            print("Error! This entry is required. Try again.")
            response = input("Withdrawl or deposit? (w/d): ")

        return response

    def cOrS(self):
        response = input("Checking or Savings? (c/s): ")
        while (response != "c" and response != "s"):
            print("Error! This entry is required. Try again.")
            response = input("Checking or Savings? (c/s): ")

        return response

    def yesOrNo(self):
        response = input("Continue? (y/n): ")
        while (response != "y" and response != "n"):
            print("Error! This entry is required. Try again.")
            response = input("Continue? (y/n): ")

        return response

class AccountApp:
    def rawr(self):
        valid = Validator()
        print("Welcome to the Account application \n")
        print("Starting Balances")

        Transaction = Transactions()
        Save = SavingsAccount(.01)
        Check = CheckingAccount(1)
        Save.deposit(1000.00)
        Check.deposit(1000.00)

        print("Checking: $" + str(Check.getBalance()))
        print("Savings: $" + str(Save.getBalance()))

        print("Enter the transactions for the month")

        response = "y"

        while(response == "y"):
            wd = valid.wOrD()
            if(wd == "w"):
                cs = valid.cOrS()
                if(cs == "c"):
                    x = 0
                    number = input("Amount?: ")
                    while(x == 0):
                        try:
                            number = int(number)
                            x=1
                        except ValueError:
                            print("Error! Invalid integer value. Try again")
                            x=0
                    Check.withdraw(number)
                elif(cs == "s"):
                    number = input("Amount?: ")
                    x = 0
                    while (x == 0):
                        try:
                            number = int(number)
                            x = 1
                        except ValueError:
                            print("Error! Invalid integer value. Try again")
                            x = 0
                    Save.withdraw(number)
            elif(wd == "d"):
                cs = valid.cOrS()
                if (cs == "c"):
                    number = input("Amount?: ")
                    x=0
                    while (x == 0):
                        try:
                            number = int(number)
                            x = 1
                        except ValueError:
                            print("Error! Invalid integer value. Try again")
                            x = 0
                    Check.deposit(number)
                elif (cs == "s"):
                    number = input("Amount?: ")
                    x=0
                    while (x == 0):
                        try:
                            number = int(number)
                            x = 1
                        except ValueError:
                            print("Error! Invalid integer value. Try again")
                            x = 0
                    Save.deposit(number)
            response = valid.yesOrNo()

        print("Monthly Payments and Fees: ")
        Save.calcPay()
        print("Checking fee:              " + str(Check.getMonthlyFee()))
        print("Savings interest payment: " + str(Save.getMonIntPay()))

        print("Final Balances")
        Check.balMonFee()
        print("Checking: $" + str(Check.getBalance()))
        print("Savings: $" + str(Save.getBalance()))



acc = AccountApp()
acc.rawr()
