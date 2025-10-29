from tkinter import *
from PIL import ImageTk, Image
import os

#현재 파이썬 파일이 있는 폴더 기준으로 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def draw_image():
    global img
    image_path=os.path.join(BASE_DIR,"common.png")
    #img=PhotoImage(file=image_path)
    #img=Image.open(image_path)
    pil_img = Image.open(image_path)
    #resize  두줄은 크기 조정할때 출력하는거!!!
    resized=pil_img.resize((200,150))
    img = ImageTk.PhotoImage(resized)
    canvas.create_image(20,20,anchor=NW,image=img)

def finish():
    canvas.delete("all")

root=Tk()
root.geometry("360x280")

canvas=Canvas(root, width=300, height=200, bg="white")
canvas.pack()

Button(root, text="이미지 표시",command=draw_image).pack()
Button(root, text="지우기",command=finish).pack()

root.mainloop()