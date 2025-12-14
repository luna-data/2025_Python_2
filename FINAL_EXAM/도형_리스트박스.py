# shape_editor.py
from tkinter import *
from tkinter import ttk, messagebox
import math

# ============== 도형 클래스 ==============
class Shape:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color
        self.canvas_id = None

    def draw(self, canvas):
        raise NotImplementedError

    def move(self, canvas, dx, dy):
        if self.canvas_id:
            canvas.move(self.canvas_id, dx, dy)
        self.x += dx
        self.y += dy

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def summary(self):
        return f"Shape({self.x},{self.y},{self.color})"


class Rectangle(Shape):
    def __init__(self, x, y, w, h, color="tomato"):
        super().__init__(x, y, color)
        self.w = w
        self.h = h

    def draw(self, canvas):
        self.canvas_id = canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h,
            fill=self.color
        )

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def summary(self):
        return f"Rectangle(x={self.x},y={self.y},w={self.w},h={self.h},color={self.color})"


class Circle(Shape):
    def __init__(self, x, y, r, color="skyblue"):
        super().__init__(x, y, color)
        self.r = r

    def draw(self, canvas):
        self.canvas_id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def summary(self):
        return f"Circle(cx={self.x},cy={self.y},r={self.r},color={self.color})"


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3, color="lightgreen"):
        super().__init__(x1, y1, color)
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def draw(self, canvas):
        self.canvas_id = canvas.create_polygon(
            self.x1, self.y1,
            self.x2, self.y2,
            self.x3, self.y3,
            fill=self.color
        )

    def area(self):
        return abs(
            (self.x1 * (self.y2 - self.y3)
             + self.x2 * (self.y3 - self.y1)
             + self.x3 * (self.y1 - self.y2)) / 2
        )

    def perimeter(self):
        def dist(xa, ya, xb, yb):
            return math.hypot(xa - xb, ya - yb)
        a = dist(self.x1, self.y1, self.x2, self.y2)
        b = dist(self.x2, self.y2, self.x3, self.y3)
        c = dist(self.x3, self.y3, self.x1, self.y1)
        return a + b + c

    def summary(self):
        return f"Triangle(({self.x1},{self.y1}),({self.x2},{self.y2}),({self.x3},{self.y3}),color={self.color})"


# ============== 유틸 함수 ==============
def calculate_total_area(shapes):
    return sum(s.area() for s in shapes)


def filter_shapes_by_type(shapes, shape_type_name):
    return [s for s in shapes if type(s).__name__ == shape_type_name]


# ============== GUI ==============
def main():
    root = Tk()
    root.title("도형 편집 & 통계 시스템")
    root.geometry("900x500")

    shapes = []

    # 좌측 입력
    frame_left = Frame(root, padx=10, pady=10)
    frame_left.pack(side="left", fill="y")

    Label(frame_left, text="도형 타입").grid(row=0, column=0, sticky="w")
    shape_type_var = StringVar(value="Rectangle")
    combo_type = ttk.Combobox(
        frame_left, textvariable=shape_type_var,
        values=["Rectangle", "Circle", "Triangle"],
        state="readonly", width=12
    )
    combo_type.grid(row=0, column=1, pady=5)

    Label(frame_left, text="x").grid(row=1, column=0, sticky="e")
    entry_x = Entry(frame_left, width=8)
    entry_x.grid(row=1, column=1)
    entry_x.insert(0, "50")

    Label(frame_left, text="y").grid(row=2, column=0, sticky="e")
    entry_y = Entry(frame_left, width=8)
    entry_y.grid(row=2, column=1)
    entry_y.insert(0, "50")

    Label(frame_left, text="w/r/x2").grid(row=3, column=0, sticky="e")
    entry_a = Entry(frame_left, width=8)
    entry_a.grid(row=3, column=1)
    entry_a.insert(0, "100")

    Label(frame_left, text="h/x3").grid(row=4, column=0, sticky="e")
    entry_b = Entry(frame_left, width=8)
    entry_b.grid(row=4, column=1)
    entry_b.insert(0, "60")

    Label(frame_left, text="y2").grid(row=5, column=0, sticky="e")
    entry_c = Entry(frame_left, width=8)
    entry_c.grid(row=5, column=1)
    entry_c.insert(0, "150")

    Label(frame_left, text="y3").grid(row=6, column=0, sticky="e")
    entry_d = Entry(frame_left, width=8)
    entry_d.grid(row=6, column=1)
    entry_d.insert(0, "100")

    Label(frame_left, text="색상").grid(row=7, column=0, sticky="e")
    entry_color = Entry(frame_left, width=8)
    entry_color.grid(row=7, column=1)
    entry_color.insert(0, "tomato")

    def add_shape():
        stype = shape_type_var.get()
        try:
            x = int(entry_x.get())
            y = int(entry_y.get())
            a = int(entry_a.get())
            b = int(entry_b.get())
            c = int(entry_c.get())
            d = int(entry_d.get())
        except ValueError:
            messagebox.showerror("입력 오류", "좌표/크기는 정수로 입력하세요.")
            return
        color = entry_color.get().strip() or "black"

        if stype == "Rectangle":
            shape = Rectangle(x, y, a, b, color)
        elif stype == "Circle":
            shape = Circle(x, y, a, color)  # a를 반지름으로 사용
        elif stype == "Triangle":
            shape = Triangle(x, y, a, c, b, d, color)
        else:
            messagebox.showerror("오류", "알 수 없는 도형 타입입니다.")
            return

        shape.draw(canvas)
        shapes.append(shape)
        update_listbox()

    def update_listbox(show_shapes=None):
        listbox.delete(0, END)
        target = show_shapes if show_shapes is not None else shapes
        for idx, s in enumerate(target):
            listbox.insert(END, f"{idx}: {s.summary()}")

    def delete_selected():
        sel = listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        # 리스트를 기준으로 삭제
        if 0 <= idx < len(shapes):
            s = shapes[idx]
            if s.canvas_id:
                canvas.delete(s.canvas_id)
            del shapes[idx]
            update_listbox()

    def clear_all():
        shapes.clear()
        canvas.delete("all")
        update_listbox()
        label_status.config(text="모든 도형 삭제")

    def calc_total_area():
        total = calculate_total_area(shapes)
        label_status.config(text=f"총 넓이: {total:.2f}")

    def filter_by_type():
        stype = shape_type_var.get()
        filtered = filter_shapes_by_type(shapes, stype)
        update_listbox(filtered)
        label_status.config(text=f"{stype} 개수: {len(filtered)}")

    Button(frame_left, text="도형 추가", width=15, command=add_shape).grid(row=8, column=0, columnspan=2, pady=5)
    Button(frame_left, text="선택 도형 삭제", width=15, command=delete_selected).grid(row=9, column=0, columnspan=2, pady=5)
    Button(frame_left, text="전체 도형 삭제", width=15, command=clear_all).grid(row=10, column=0, columnspan=2, pady=5)
    Button(frame_left, text="전체 넓이 계산", width=15, command=calc_total_area).grid(row=11, column=0, columnspan=2, pady=5)
    Button(frame_left, text="타입별 필터(우측 목록만)", width=20, command=filter_by_type).grid(row=12, column=0, columnspan=2, pady=5)

    # 중앙 Canvas
    canvas = Canvas(root, bg="white", width=450, height=450)
    canvas.pack(side="left", padx=5, pady=10)

    # 우측 목록
    frame_right = Frame(root, padx=10, pady=10)
    frame_right.pack(side="left", fill="both", expand=True)

    Label(frame_right, text="도형 목록").pack(anchor="w")
    listbox = Listbox(frame_right, width=40, height=20)
    listbox.pack(fill="both", expand=True)

    label_status = Label(frame_right, text="상태 메시지")
    label_status.pack(anchor="w", pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
