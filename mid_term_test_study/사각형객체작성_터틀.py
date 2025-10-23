import turtle

class Rectangle:
    def __init__(self, w, h, x, y):
        self.w = w
        self.h = h
        self.x = x
        self.y = y

    def calcArea(self):
        return self.w * self.h

    def draw(self):
        # TODO: 터틀 그래픽으로 사각형 그리기
        global w, h, x, y      # 모든 변수는 전역변수로 선언
        w = self.w
        h = self.h
        x = self.x
        y = self.y
        t.penup()
        t.goto(x, y)
        t.pendown()
        for i in range(2):
            t.forward(w)
            t.right(90)
            t.forward(h)
            t.right(90)

# === 전역 터틀 객체 생성 ===
t = turtle.Turtle()

# === 객체 생성 ===
r1 = Rectangle(100, 100, 0, 0)
r2 = Rectangle(200, 200, 10, 10)

# === 넓이 출력 ===
print("첫 번째 사각형 => 폭:", r1.w, "높이:", r1.h, "넓이:", r1.calcArea())
print("두 번째 사각형 => 폭:", r2.w, "높이:", r2.h, "넓이:", r2.calcArea())

# === 사각형 그리기 ===
r1.draw()
r2.draw()

turtle.done()
