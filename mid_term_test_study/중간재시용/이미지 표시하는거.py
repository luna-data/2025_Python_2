from tkinter import *
from PIL import Image, ImageTk
import os

def draw_image():
    global img  # 전역 참조 유지
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "common.png")  # JPG 그대로
    pil_img = Image.open(path)
    img = ImageTk.PhotoImage(pil_img)
    canvas.create_image(20, 20, anchor=NW, image=img)

root = Tk()
root.title("Canvas 이미지 표시")
root.geometry("400x400")

canvas = Canvas(root, width=400, height=350, bg="lightyellow")
canvas.pack()

Button(root, text="이미지 표시", command=draw_image).pack(pady=10)

root.mainloop()
