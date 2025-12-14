class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.__balance=balance
        print(f"{self.owner} 계좌가 생성되었습니다.")

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"{self.owner} 통장에 {amount}원이 입금되었습니다.")
    
    def withdraw(self, amount):
        if self.__balance>amount:
            self.__balance-=amount
            print(f"{self.owner} 통장에서 {amount}원이 출금되었습니다.")

        else:
            print("잔액부족")

    def get_balance(self): #현재잔액
        return self.__balance

    def set_balance(self,amount): #잔액 직접 수정
        if amount>=0:
            self.__balance=amount
            return self.__balance

        
a=BankAccount("A")
b=BankAccount("B")

a.deposit(100)
b.deposit(200)
a.withdraw(30)
b.withdraw(50)

print(f"{a.owner} 계좌의 현재 잔액:", a.get_balance())
print(f"{b.owner} 계좌의 현재 잔액:",b.get_balance())

a.set_balance(500)
print(f"{a.owner} 계좌의 수정된 잔액:",a.get_balance())