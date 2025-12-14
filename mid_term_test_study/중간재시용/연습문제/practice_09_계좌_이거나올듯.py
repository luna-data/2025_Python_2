class BankAccount:
    def __init__(self,name,number, balance):
        self.name=name
        self.number=number
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance>amount:
            print("인출 성공")
            return self.balance-amount
        else:
            print("잔액부족")

        
account=BankAccount("Kim","123456789", 1000)
print("초기 잔고:",account.balance)
account.deposit(500)
print("저축 후 잔고:", account.balance)
account.withdraw(200)
print("인출 후 잔고:", account.balance)
account.withdraw(1500)#잔액부족