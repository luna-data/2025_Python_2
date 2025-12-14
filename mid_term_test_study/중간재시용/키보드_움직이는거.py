from tkinter import *

root = Tk()
root.title("문제4: 키보드 연속 이동")

W, H = 420, 260
canvas = Canvas(root, width=W, height=H, bg="white")
canvas.pack()

player = canvas.create_rectangle(190, 110, 230, 150, fill="deepskyblue")

keys_down = set()
SPEED = 4

def on_press(e):
    keys_down.add(e.keysym)

def on_release(e):
    keys_down.discard(e.keysym)

def tick():
    dx = dy = 0
    if "Left" in keys_down:  dx -= SPEED
    if "Right" in keys_down: dx += SPEED
    if "Up" in keys_down:    dy -= SPEED
    if "Down" in keys_down:  dy += SPEED
    canvas.move(player, dx, dy)
    # 경계 제한
    x1, y1, x2, y2 = canvas.coords(player)
    if x1 < 0: canvas.move(player, -x1, 0)
    if y1 < 0: canvas.move(player, 0, -y1)
    if x2 > W: canvas.move(player, W - x2, 0)
    if y2 > H: canvas.move(player, 0, H - y2)
    root.after(16, tick)

root.bind("<KeyPress>", on_press)
root.bind("<KeyRelease>", on_release)
root.focus_force()

tick()
root.mainloop()
