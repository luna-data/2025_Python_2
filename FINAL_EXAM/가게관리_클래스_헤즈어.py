#---------문제 요구사항 (HAS-A 중심)

#---------Product(부모)

#---------name, price

#---------클래스 변수 total_sales = 0 (전체 매출)

#---------자식 클래스 (다형성 가격 계산)

#---------NormalProduct → 가격 그대로

#---------DiscountProduct → price * 0.8 적용

#---------PremiumProduct → price + 5000 적용

#---------Store 클래스 (HAS-A)

#---------products 리스트 보유

#---------add(product)

#---------sell(name): 해당 상품 판매 & total_sales 업데이트

#---------summary(): 판매된 상품 목록 + 총 매출 출력

# =========================================
# 문제 2: HAS-A + 클래스 변수 + 다형성
# =========================================

class Product:
    total_sales = 0  # ★ 전체 매출(클래스 변수)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price  # 자식에서 오버라이딩됨


# --------- IS-A 관계 활용한 다형성 ---------
class NormalProduct(Product):
    pass  # 가격 변경 없음


class DiscountProduct(Product):
    def get_price(self):
        return int(self.price * 0.8)  # 20% 할인


class PremiumProduct(Product):
    def get_price(self):
        return self.price + 5000  # 프리미엄 추가 비용


# -------- Store 클래스 (HAS-A 관계) --------
class Store:
    def __init__(self):
        self.products = []  # 상품을 "가지고 있다" → HAS-A 관계

    def add(self, product):
        self.products.append(product)

    def sell(self, name):
        for p in self.products:
            if p.name == name:
                price = p.get_price()
                Product.total_sales += price
                return f"{name} 판매됨! 가격: {price}원"
        return f"{name} 상품이 없습니다."

    def summary(self):
        names = ", ".join([p.name for p in self.products])
        return (f"보유 상품: {names}\n"
                f"총 매출: {Product.total_sales}원")


# -------- 테스트 --------
store = Store()
store.add(NormalProduct("커피", 3000))
store.add(DiscountProduct("케이크", 8000))
store.add(PremiumProduct("샌드위치", 5000))

print(store.sell("커피"))
print(store.sell("케이크"))
print(store.sell("샌드위치"))

print("\n=== 매장 요약 ===")
print(store.summary())
