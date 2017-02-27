
"""
    Objected Oriented ATM

    Object:
        Methods/Functions
        Attributes/Properties
        Constructor -- defines the initial state
        Destructor -- defines the terminating actions

"""

class Account:

    def __init__(self, balance):
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
        return True

    def Withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal cannot be made.")
            return False

        self.balance -= amount

    def CheckBalance(self):
        print("Your balance is " + str(self.balance))

"""
    options
        List of lists
        [
            ["Deposit", Deposit],
            ["Back", Back]
        ]

"""
class Menu:
    def __init__(self, options, previous=None):
        self.previous = previous
        self.options = options

    def Display(self):
        print("Menu:")
        counter = 1
        for option in self.options:
            print("\t" + str(counter) + ": " + option[0])
            counter += 1
        print("")

class ATM:

    def __init__(self):
        self.account = Account(500)

    def Run(self):
        home = Menu([
            ["Deposit", self.account.Deposit],
            ["Withdraw", self.account.Withdraw]
        ])
        home.Display()



atm = ATM()
atm.Run()
