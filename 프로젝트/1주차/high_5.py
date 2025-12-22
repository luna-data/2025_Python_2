from datetime import datetime

# -------------------- Person --------------------
class Person:
    def __init__(self, name, date_birth, address, position=None):
        self.name = name
        self.date_birth = date_birth
        self.address = address
        self.position = position

    def __str__(self):
        pos = f" ({self.position})" if self.position else ""
        return f"{self.name}{pos}, dateBirth: {self.date_birth}, address: {self.address}"


# -------------------- Transaction --------------------
class Transaction:
    def __init__(self, tx_id, amount, time):
        self.tx_id = tx_id
        self.amount = amount      # 입금:+, 출금:-
        self.time = time

    def __str__(self):
        sign = "+" if self.amount >= 0 else "-"
        return f"Transaction {self.tx_id}: amount {sign}{abs(self.amount):,}, time {self.time.strftime('%Y/%m/%d %H:%M')}"


# -------------------- Account (부모 클래스) --------------------
class Account:
    def __init__(self, account_no, owner, opened, balance=0):
        self.account_no = account_no
        self.owner = owner          # Person 객체
        self.opened = opened
        self.balance = balance
        self.transactions = []      # Transaction 객체를 저장

    def deposit(self, tx_id, amount, time=None):
        if amount <= 0:
            print("입금액 오류!")
            return
        if time is None:
            time = datetime.now()

        self.balance += amount
        self.transactions.append(Transaction(tx_id, amount, time))

    def withdraw(self, tx_id, amount, time=None):
        if amount <= 0:
            print("출금액 오류!")
            return
        if amount > self.balance:
            print("잔액 부족!")
            return
        if time is None:
            time = datetime.now()

        self.balance -= amount
        self.transactions.append(Transaction(tx_id, -amount, time))

    def print_statement(self):
        print(f"[Account {self.account_no}] owner: {self.owner.name} | opened: {self.opened.strftime('%Y/%m/%d')} | balance: {self.balance:,}")
        for tx in self.transactions:
            print("  -", tx)


# -------------------- SavingAccount (자식 클래스) --------------------
class SavingAccount(Account):
    def print_statement(self):
        print(f"[Saving Account {self.account_no}] balance: {self.balance:,} | opened: {self.opened.strftime('%Y/%m/%d')}")
        for tx in self.transactions:
            print("  -", tx)


# -------------------- MortgageAccount (자식 클래스) --------------------
class MortgageAccount(Account):
    def __init__(self, account_no, owner, opened, balance=0, property_addr=""):
        super().__init__(account_no, owner, opened, balance)  # 부모 생성자 호출
        self.property_addr = property_addr

    def print_statement(self):
        print(f"[Mortgage Account {self.account_no}] balance: {self.balance:,} | opened: {self.opened.strftime('%Y/%m/%d')} | property: {self.property_addr}")
        for tx in self.transactions:
            print("  -", tx)


# -------------------- 예제 실행 --------------------
if __name__ == "__main__":
    kim = Person("Kim Hankook", "1958/0202", "Bangbae 27", "Manager")
    lee = Person("Lee Sera", "1958/0202", "Bangbae 27")

    saving = SavingAccount(1278, lee, datetime.strptime("1998/03/02", "%Y/%m/%d"), 279_000)
    saving.withdraw(487, 104_000, datetime.strptime("2003/08/12 14:30", "%Y/%m/%d %H:%M"))

    mortgage = MortgageAccount(2944, kim, datetime.strptime("2000/04/24", "%Y/%m/%d"), 2_567_330, "Ilsan 207-8")

    print("=== 사람 ===")
    print(kim)
    print(lee)

    print("\n=== 저축계좌 ===")
    saving.print_statement()

    print("\n=== 주택담보계좌 ===")
    mortgage.print_statement()