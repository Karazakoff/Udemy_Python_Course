import random
class Account():
    def __init__(self, owner, balance = 0, card):
        self.owner = owner
        self.balance = balance
        self.card = card
    def __str__(self):
        return f" Account owner: {self.owner} \n Account card: {self.card} \n Account balance: {self.balance}$"
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Accepted")
        else:
            print("Sorry, Funds Unavailable!")

name = input("What is your name: ")
balance = "WRONG"
while type(balance) != 'int':
    try:
        balance = int(input("Give me your amount: "))
    except ValueError:
        print("Invalid amount, give me normal please !!!")
    else:
        break

card = ""
for i in range(1,17):
    if i % 4 == 1:
        card += " "
    card += str(random.randint(0,9))
account = Account(name, balance, card)
print(account)
