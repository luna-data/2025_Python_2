# shape_manager_gui.py

import math
from tkinter import *


# ====== 클래스 영역 ======
class Shape:
    def __init__(self, x: int, y: int, color: str = "black"):
        self.x = x
        self.y = y
        self.color = color
        self.canvas_id = None  # Canvas 객체 ID

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError

    def draw(self, canvas: Canvas):
        raise NotImplementedError


class Rectangle(Shape):  # Rectangle is-a Shape
    def __init__(self, x: int, y: int, w: int, h: int, color: str = "tomato"):
        super().__init__(x, y, color)
        self.w = w
        self.h = h

    def area(self) -> float:
        return float(self.w * self.h)

    def perimeter(self) -> float:
        return float(2 * (self.w + self.h))

    def draw(self, canvas: Canvas):
        self.canvas_id = canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.w,
            self.y + self.h,
            fill=self.color,
            outline="black",
        )


class Circle(Shape):  # Circle is-a Shape
    def __init__(self, x: int, y: int, r: int, color: str = "skyblue"):
        super().__init__(x, y, color)
        self.r = r

    def area(self) -> float:
        return float(math.pi * self.r ** 2)

    def perimeter(self) -> float:
        return float(2 * math.pi * self.r)

    def draw(self, canvas: Canvas):
        self.canvas_id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color,
            outline="black",
        )


class ShapeManager:  # ShapeManager has-a Shape 리스트
    def __init__(self):
        self.shapes: list[Shape] = []

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)

    def clear(self, canvas: Canvas):
        for s in self.shapes:
            if s.canvas_id is not None:
                canvas.delete(s.canvas_id)
        self.shapes.clear()

    def total_area(self) -> float:
        return sum(s.area() for s in self.shapes)

    def summary(self) -> str:
        return f"도형 수: {len(self.shapes)}, 총 넓이: {self.total_area():.2f}"


# ====== 이벤트 함수 영역 ======
def add_rectangle():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        w = int(entry_w.get())
        h = int(entry_h.get())
    except ValueError:
        status_label.config(text="숫자를 정확히 입력하세요.")
        return

    rect = Rectangle(x, y, w, h, color="tomato")
    rect.draw(canvas)
    manager.add_shape(rect)
    status_label.config(text="사각형이 추가되었습니다.")
    update_summary()


def add_circle():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        r = int(entry_r.get())
    except ValueError:
        status_label.config(text="숫자를 정확히 입력하세요.")
        return

    circle = Circle(x, y, r, color="skyblue")
    circle.draw(canvas)
    manager.add_shape(circle)
    status_label.config(text="원이 추가되었습니다.")
    update_summary()


def clear_all():
    manager.clear(canvas)
    status_label.config(text="모든 도형을 삭제했습니다.")
    update_summary()


def update_summary():
    summary_label.config(text=manager.summary())


# ====== GUI 영역 ======
root = Tk()
root.title("도형 편집 & 통계 시스템")

manager = ShapeManager()

# Canvas
canvas = Canvas(root, width=400, height=250, bg="white")
canvas.pack(padx=10, pady=10)

# 입력 영역
input_frame = Frame(root)
input_frame.pack(pady=5)

Label(input_frame, text="x:").grid(row=0, column=0)
entry_x = Entry(input_frame, width=5)
entry_x.grid(row=0, column=1)

Label(input_frame, text="y:").grid(row=0, column=2)
entry_y = Entry(input_frame, width=5)
entry_y.grid(row=0, column=3)

Label(input_frame, text="w:").grid(row=1, column=0)
entry_w = Entry(input_frame, width=5)
entry_w.grid(row=1, column=1)

Label(input_frame, text="h:").grid(row=1, column=2)
entry_h = Entry(input_frame, width=5)
entry_h.grid(row=1, column=3)

Label(input_frame, text="r:").grid(row=2, column=0)
entry_r = Entry(input_frame, width=5)
entry_r.grid(row=2, column=1)

btn_frame = Frame(root)
btn_frame.pack(pady=5)

Button(btn_frame, text="사각형 추가", command=add_rectangle, width=12).pack(side="left", padx=5)
Button(btn_frame, text="원 추가", command=add_circle, width=12).pack(side="left", padx=5)
Button(btn_frame, text="전체 삭제", command=clear_all, width=12).pack(side="left", padx=5)

summary_label = Label(root, text="도형 수: 0, 총 넓이: 0.00")
summary_label.pack(pady=5)

status_label = Label(root, text="좌표와 크기를 입력한 뒤 버튼을 눌러보세요.")
status_label.pack(pady=5)

root.mainloop()
