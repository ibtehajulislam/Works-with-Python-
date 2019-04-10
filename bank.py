#Creating a bank account:
class Account:
    def __init__(self,name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

# Creating methonds for the account
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry not enough funds!")

    def statement(self):
        print("Account balance: CA${}".format(self.balance))

# Creating a checking account
class checking(Account):
    def __init__(self, name, balance):
        super().__init__(name,balance,min_balance = -1000)
    def __str__(self):
        return "{}'s checking account: CA${}.".format(self.name, self.balance)

# Creating a savings account
class saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s saving account: CA${}.".format(self.name, self.balance)
        
