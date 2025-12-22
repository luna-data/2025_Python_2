price=int(input("가격 입력: "))
if 10000<=price<50000:
    price=price-price*0.1
elif 50000<=price<100000:
    price=price-price*0.2
else:
    price=price-price*0.3

print('할인 후 가격: ',price)