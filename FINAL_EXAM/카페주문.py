# cafe_pos.py
from tkinter import *
from tkinter import messagebox

# ========== 클래스 ==========
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # 단가

    def total_price(self, qty):
        return self.price * qty

    def __str__(self):
        return f"{self.name}({self.price}원)"


class SpecialDrink(Drink):
    def __init__(self, name, price, extra_fee):
        super().__init__(name, price)
        self.extra_fee = extra_fee

    def total_price(self, qty):
        return self.price * qty + self.extra_fee

    def __str__(self):
        return f"{self.name}({self.price}원, 추가비 {self.extra_fee}원)"


class Order:
    def __init__(self):
        self.items = []  # (Drink, qty)

    def add(self, drink, qty):
        self.items.append((drink, qty))

    def remove(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)

    def clear(self):
        self.items.clear()

    def total(self):
        return sum(d.total_price(q) for d, q in self.items)

    def receipt_lines(self):
        lines = []
        for d, q in self.items:
            line = f"{d.name} x {q} → {d.total_price(q)}원"
            lines.append(line)
        lines.append(f"총합: {self.total()}원")
        return lines


# ========== GUI ==========
def main():
    root = Tk()
    root.title("카페 주문 POS")
    root.geometry("750x450")

    # 메뉴 준비
    menu_items = {
        "아메리카노": Drink("아메리카노", 3000),
        "카페라떼": Drink("카페라떼", 4000),
        "카푸치노": Drink("카푸치노", 4500),
        "시그니처 블렌드": SpecialDrink("시그니처 블렌드", 5000, 1000),
        "콜드브루 스페셜": SpecialDrink("콜드브루 스페셜", 5500, 1500),
    }

    order = Order()

    # 왼쪽: 메뉴
    frame_left = Frame(root, padx=10, pady=10)
    frame_left.pack(side="left", fill="y")

    Label(frame_left, text="메뉴 목록").pack(anchor="w")
    list_menu = Listbox(frame_left, width=25, height=15)
    list_menu.pack()
    for name in menu_items:
        list_menu.insert(END, name)

    Label(frame_left, text="수량").pack(pady=5)
    spin_qty = Spinbox(frame_left, from_=1, to=10, width=5)
    spin_qty.pack()

    def add_to_cart():
        sel = list_menu.curselection()
        if not sel:
            messagebox.showwarning("선택 없음", "메뉴를 선택하세요.")
            return
        idx = sel[0]
        name = list_menu.get(idx)
        drink = menu_items[name]
        try:
            qty = int(spin_qty.get())
        except ValueError:
            messagebox.showerror("입력 오류", "수량은 정수로 입력하세요.")
            return
        order.add(drink, qty)
        update_cart()

    Button(frame_left, text="장바구니 담기", width=20, command=add_to_cart).pack(pady=10)

    # 오른쪽: 장바구니 + 영수증
    frame_right = Frame(root, padx=10, pady=10)
    frame_right.pack(side="left", fill="both", expand=True)

    Label(frame_right, text="장바구니").pack(anchor="w")
    list_cart = Listbox(frame_right, width=40, height=10)
    list_cart.pack(fill="x")

    label_total = Label(frame_right, text="총합: 0원")
    label_total.pack(anchor="w", pady=5)

    frame_btns = Frame(frame_right)
    frame_btns.pack(fill="x", pady=5)

    def update_cart():
        list_cart.delete(0, END)
        for d, q in order.items:
            list_cart.insert(END, f"{d.name} x {q} → {d.total_price(q)}원")
        label_total.config(text=f"총합: {order.total()}원")

    def remove_selected():
        sel = list_cart.curselection()
        if not sel:
            return
        idx = sel[0]
        order.remove(idx)
        update_cart()

    def clear_cart():
        order.clear()
        update_cart()
        text_receipt.delete("1.0", END)

    def checkout():
        if not order.items:
            messagebox.showinfo("결제", "장바구니가 비어 있습니다.")
            return
        lines = order.receipt_lines()
        text_receipt.delete("1.0", END)
        for line in lines:
            text_receipt.insert(END, line + "\n")

    def save_receipt():
        if not order.items:
            messagebox.showinfo("저장", "저장할 주문이 없습니다.")
            return
        lines = order.receipt_lines()
        with open("receipt.txt", "a", encoding="utf-8") as f:
            f.write("=== 새 주문 ===\n")
            for line in lines:
                f.write(line + "\n")
        messagebox.showinfo("저장", "receipt.txt에 저장되었습니다.")

    Button(frame_btns, text="선택 삭제", width=10, command=remove_selected).pack(side="left", padx=5)
    Button(frame_btns, text="전체 비우기", width=10, command=clear_cart).pack(side="left", padx=5)
    Button(frame_btns, text="결제", width=10, command=checkout).pack(side="left", padx=5)
    Button(frame_btns, text="주문 기록 저장", width=15, command=save_receipt).pack(side="left", padx=5)

    Label(frame_right, text="영수증").pack(anchor="w")
    text_receipt = Text(frame_right, height=10)
    text_receipt.pack(fill="both", expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
