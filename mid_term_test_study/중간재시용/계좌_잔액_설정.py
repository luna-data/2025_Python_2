#클래스 - 은행시스템

from datetime import datetime

# -------------------- Person --------------------
class Person:
  def __init__(self, name: str, date_birth: str, address: str, position: str = None):
    self.name = name
    self.date_birth = date_birth
    self.address = address
    self.position = position

  # 설정자 (setter)
  def set_name(self, name: str):
    self.name = name

  def set_address(self, address: str):
    self.address = address

  def set_position(self, position: str):
    self.position = position

  def __str__(self):
    pos = f" ({self.position})" if self.position else ""
    return f"{self.name}{pos}, 생년월일={self.date_birth}, 주소={self.address}"


# -------------------- Transaction --------------------
class Transaction:
  def __init__(self, tx_id: int, amount: int, time: datetime):
    self.tx_id = tx_id
    self.amount = amount
    self.time = time

  # 설정자
  def set_amount(self, amount: int):
    self.amount = amount

  def set_time(self, time: datetime):
    self.time = time

  def __str__(self):
    sign = "+" if self.amount >= 0 else "-"
    return f"거래#{self.tx_id} {sign}{abs(self.amount):,}원 @ {self.time.strftime('%Y-%m-%d %H:%M')}"


# -------------------- Account --------------------
from datetime import datetime

class Account:
  def __init__(self, account_no, owner, opened, balance=0):
    self.account_no = account_no
    self.owner = owner
    self.opened = opened
    self.balance = balance
    self.history = []  # 거래 내역을 '문자열'로 저장

  def deposit(self, amount):
    self.balance += amount
    self.history.append(f"입금 {amount}원")

  def withdraw(self, amount):
    if amount > self.balance:
      print("잔액 부족!")
    else:
      self.balance -= amount
      self.history.append(f"출금 {amount}원")

  def print_statement(self):
    print(f"[계좌 {self.account_no}] {self.owner} | 개설일: {self.opened.date()} | 잔액: {self.balance:,}원")
    for tx in self.history:   # 문자열 리스트이므로 그대로 출력
      print("  -", tx)

# -------------------- 예제 실행 --------------------
if __name__ == "__main__":
  # 사람 생성
  kim = Person("Kim Hankook", "1958/02/02", "Bangbae 27", "Manager")
  lee = Person("Lee Sera", "1958/02/02", "Bangbae 27")

  # 계좌 생성
  saving = Account(1278, lee, datetime.strptime("1998/03/02", "%Y/%m/%d"), 279_000)

  # 거래 (심플 버전: 금액만 전달)
  saving.withdraw(104_000)   # 출금
  saving.deposit(50_000)     # 입금 예시

  # 출력
  print("=== 사람 ===")
  print(kim)
  print(lee)

  print("\n=== 계좌 명세 ===")
  saving.print_statement()

# Q1. 새로운 사람 "Lee Sera"를 생성하세요. (생성자 사용)
Lee = Person("Lee Sera", "1990/03/15", "seoul")
# Q2. Lee의 계좌(번호 1001, 잔액 100000원)를 생성하세요. (생성자 사용)
account=Account(1001,lee,datetime.strptime("2025/9/18","%Y/%m/%d"),100000)
# Q3. 계좌에 50000원을 입금하세요. (deposit 사용)
account.deposit(50000)
# Q4. 계좌에서 30000원을 출금하세요. (withdraw 사용)
account.withdraw(30000)
# Q5. 계좌의 잔액을 직접 바꿔보세요. (balance 속성에 값 대입)
account.balance=20000 #difficult
# Q6. 사람의 주소를 "Busan"으로 바꿔보세요. (set_address 사용)
Lee.set_address("Busan")
# Q7. 최종 출력문을 확인하세요.
print(Lee)

print("=== 사람 정보 ===")
account.print_statement()