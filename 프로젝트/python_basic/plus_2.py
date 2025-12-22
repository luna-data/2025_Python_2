class Food:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_description(self):
        return f"{self.name}, 가격: {self.price}원"


class Pizza(Food):
    def __init__(self,name,price,size):
        super().__init__(name,price)
        self.size=size
   # def get_description(self):
       # return f"{self.name}, 가격: {self.price}원"


class Burger(Food):
    def __init__(self,name,price,has_cheese):
        super().__init__(name,price)
        self.has_cheese=has_cheese

    #def get_description(self):
       # return f"{self.name}, 가격: {self.price}원"

    



food1 = Food("샌드위치", 5500)
print(food1.get_description())

pizza1 = Pizza("페퍼로니 피자", 15000, "L")
print(pizza1.get_description())
print("사이즈:", pizza1.size)
burger1 = Burger("치즈버거", 7000, True)
print(burger1.get_description())
print("치즈 포함 여부:", burger1.has_cheese)
