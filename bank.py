class bank:
    def __init__(self,balance):
        self.balance = balance
        
    def deposit(self,D):
        self.balance += D
        print(f"Current bank balance is ${self.balance}")

    def withdraw(self,W):
        if self.balance - W > 0:
            self.balance -= W
            print(f"Current bank balance is ${self.balance}")
        else:
            print("Your balance is insufficient")

bank1 = bank(50)
bank1.deposit(30)
bank1.withdraw(40)
bank1.withdraw(100)