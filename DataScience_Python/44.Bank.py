import random

class Account:
    name = ''
    AC = ''
    balance = 0

    def __init__(self, name, AC, balance) -> None:
        self.name = name
        self.AC = AC
        self.balance = balance

    

    def deposite(self, amount):
        self.balance += amount
    def widraw(self, amount):
        if self.balance <= 0 or amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
    
    def display(self):
        print(f"Name: {self.name}\nAC : {self.AC}\nBalance : {self.balance}")

print("Welcome to Monoranjan Bank of India")

name = input("Enter your Name: ")
ac = int(random.random()*10e9)

User = Account(name , ac, balance=0)

# print(ac)

while(1):
    print("1. Widraw\n2. Diposite\n3. Display")
    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        amount = int(input("Enter Amount: "))
        User.widraw(amount)
    elif ch == 2:
        amount = int(input("Enter Amount: "))
        User.deposite(amount)
    elif ch == 3:
        User.display()
    else:
        print("Invalid Choice!!!")
        