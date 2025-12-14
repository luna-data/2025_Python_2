class Inventory():
    stock=0
    def __init__(self):
        print('새 상품이 등록되었습니다.')

    def get_stock(self):
        return Inventory.stock

    def set_stock(self,amount):
        if amount>=0:
            Inventory.stock=amount
    
    def add_stock(self,amount):
        if amount>0:
            Inventory.stock+=amount
            print(f"{amount}개가 입고되었습니다.")
    
    def remove_stock(self,amount):
        if Inventory.stock>amount:
            Inventory.stock-=amount
            print(f"{amount}개가 출고되었습니다.")

item1=Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수량:",item1.get_stock())
item1.set_stock(20)
print("수정된 재고 수량:",item1.get_stock())