from tkinter import *
import tkinter.messagebox as msgbox #메시지박스 모듈
#1
class Food:
    def __init__(self,name,price):
        self.name=name
        self.price=int(price)

    def total_price(self,qty):
        return self.price*qty
    
    def __str__(self):
        return f"메뉴: {self.name}, 단가: {self.price}원"
#2
class DeliveryFood(Food):
    def __init__(self,name,price,delivery_fee):
        super().__init__(name,price)
        self.delivery_fee=int(delivery_fee)
         
    def total_price(self,qty):
        return (self.price*qty)+self.delivery_fee

    def __str__(self):
        return f"메뉴: {self.name}, 단가: {self.price}, 배달비: {self.delivery_fee}원"
#3
class Order:
    def __init__(self):
        self.items=[]

    def add(self,food,qty):
        self.items.append((food,qty))
    
    def clear(self):
        self.items.clear()

    def total(self):
        return sum(f.total_price(q) for f, q in self.items)
    
    def summary_lines(self):
        lines = []
        for f, q in self.items:
            lines.append(f"{f.name} x {q} = {f.total_price(q):,}원")
        lines.append(f"----------------------------")
        lines.append(f"총 합계: {self.total():,}원")
        return lines


def add_cart():
    cart=menu_list.curselection()
    if not cart:
        msgbox.showwarning("안내", "메뉴를 선택하세요.")
        return
    qty = int(s.get())
    food = menu_items[cart[0]]

    order.add(food, qty)
    cart_list.insert(END, f"{food.name} x {qty} = {food.total_price(qty):,}원")
    label_total.config(text=f"합계: {order.total():,}원")

def order_now():
    if not order.items:
        msgbox.showinfo("알림", "장바구니가 비어 있습니다.")
        return
    receipt = "\n".join(order.summary_lines())
    msgbox.showinfo("영수증", receipt)

def clear_all():
    if not order.items:
        msgbox.showinfo("알림", "이미 장바구니가 비어 있습니다.") #메시지 박스 띄우기
        return
    if msgbox.askyesno("확인", "정말 모두 비우시겠습니까?"): #재시도나 취소 관련 메시지 박스 출력
        order.clear()
        cart_list.delete(0, END) 
        label_total.config(text="합계: 0원")

#4
root=Tk()
root.geometry("680x440")
root.title('주문.배달 시스템')

#과제 자료 및 교수님 깃허브 참고___
order = Order()
menu_items = [
    Food("김밥", 3000),
    Food("라면", 4000),
    Food("떡볶이", 5000),
    DeliveryFood("치킨", 18000, 3000),
    DeliveryFood("피자", 20000, 3000),
]
#_______이부분까지 참고

left=Frame(root,padx=10,pady=10)
left.pack(side='left', expand=True)
right=Frame(root,padx=10,pady=10)
right.pack(side="left", expand=True)

#5 left
Label(left,text='메뉴 목록').pack(anchor='w')
menu_list=Listbox(left,width=35,height=20)
menu_list.pack(expand=True)
for menu in menu_items:
    menu_list.insert(END, str(menu)) #리스트박스에 추가하는거! 리스트 마지막에 맨 아랫줄에 생성!

ctrl=Frame(left)
ctrl.pack()
Label(ctrl,text="수량").pack(side='left')

q_var=IntVar(value=1)
s=Spinbox(ctrl, from_=1, to=30, width=5, textvariable=q_var, justify="center")
s.pack(side="left")
Button(ctrl,text="장바구니 담기",command=add_cart).pack(side='left')

#6 right
Label(right,text="장바구니").pack(anchor='w')
cart_list=Listbox(right,width=35,height=20)
cart_list.pack(expand=True)

# pack을 한 줄에 다 써서 오류가 계속 생김. 같은 실수를 계속 반복함
last=Frame(right)
label_total=last.pack(side='left')
Label(last,text="합계: 0원")
#label_total.pack(side='left')

b_frame=Frame(last)
b_frame.pack(side='right')
Button(b_frame, text="주문하기",command=order_now).pack(side="left")
Button(b_frame, text="전체 비우기", command=clear_all).pack(side="left")

root.mainloop()