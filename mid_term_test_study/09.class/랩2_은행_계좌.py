class BankAccount:
    #은행계좌는 은닉이 필요함!
    def __init__(self):
        self.__balance=0

    def withdraw(self,amount):
        self.__balance-=amount
        print("통장에 ",amount, "원이 출금되었음")
        return self.__balance
    
    def deposit(self,amount):
        self.__balance+=amount
        print("통장에 ",amount,"원이 입금되었음")
        return self.__balance
    
a=BankAccount()
a.deposit(100)
a.withdraw(10)