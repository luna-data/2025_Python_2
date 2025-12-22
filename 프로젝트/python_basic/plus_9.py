class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class Store:
    def __init__(self, name):  # Store has Products
        self.name = name
        self.products = []  # Product 리스트
    
    def add_product(self, product):
        self.products.append(product)
    
    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

# 가게 객체 생성
store = Store("W쇼핑")

# 상품 객체 생성
p1 = Product("커피", 4500, 100)
p2 = Product("쿠키", 2500, 50)
p3 = Product("머그컵", 8000, 30)

# 가게에 상품 추가
store.add_product(p1)
store.add_product(p2)
store.add_product(p3)

# 상품 검색
item = store.search_product("쿠키")
print(f"찾은 상품: {item.name}, 가격: {item.price}원, 재고: {item.stock}개")