from tkinter import *

root = Tk()
root.title("문제2: 바운스")

W, H = 350, 200
canvas = Canvas(root, width=W, height=H, bg="white")
canvas.pack()

ball = canvas.create_oval(20, 20, 50, 50, fill="tomato")
vx, vy = 3, 2

def tick():
    global vx, vy
    x1, y1, x2, y2 = canvas.coords(ball)
    # 벽 충돌 체크: 좌/우
    if x1 <= 0 or x2 >= W:
        vx = -vx
    # 상/하
    if y1 <= 0 or y2 >= H:
        vy = -vy
    canvas.move(ball, vx, vy)
    root.after(16, tick)  # ~60fps

tick()
root.mainloop()
