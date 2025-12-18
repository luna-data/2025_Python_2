class Product:
    def __init__(self, name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def apply_discount(self, discount_percentage):
        discount_amount=self.price*discount_percentage/100
        self.price-=discount_amount

class ShoppingCart:
    def __init__(self):
        self.items={}

    def add_item(self,product,quantity):
        self.items[product]=quantity

    def remove_item(self,product):
        if product in self.items:
            self.items.pop(product)

    def get_total_price(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total


product1 = Product("노트북", 1000000, 5)
product2 = Product("마우스", 30000, 10)
cart = ShoppingCart()
cart.add_item(product1, 1)
cart.add_item(product2, 2)

print(f"총 금액: {cart.get_total_price()}")
print(f"상품 종류 수: {len(cart.items)}")

