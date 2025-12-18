class Product:
    def __init__(self, name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def apply_discount(self, discount_percentage):
        discount_amount=self.price*discount_percentage/100
        self.price-=discount_amount
class 

product1 = Product("노트북", 1000000, 5)
product2 = Product("마우스", 30000, 10)
cart = ShoppingCart()
cart.add_item(product1, 1)
cart.add_item(product2, 2)
print(cart.get_total_price())
