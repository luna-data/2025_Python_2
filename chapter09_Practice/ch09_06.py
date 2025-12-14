class BankAccount:
    interest_rate=0.3 #문제에서 클래스변수 지정하라고 명시함!
    def __init__(self, name, number, balance):
        self.name=name
        self.number=number
        self.balance=balance #인스턴스 변수

    def deposit(self,amount): #입금
        self.balance+=amount
        print("입금 성공")
    
    def withdraw(self,amount): #출금
        if self.balance>=amount:
            print('인출 성공')
            self.balance-=amount
        else:
            print('잔액 부족')
        return self.balance
    

account = BankAccount("Kim", "123456789", 1000)
print("초기 잔고:", account.balance)
account.deposit(500)
print("저축 후 잔고:", account.balance)
account.withdraw(200)
print("인출 후 잔고:", account.balance)
account.withdraw(1500) #잔액부족