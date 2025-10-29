from tkinter import *
from PIL import ImageTk, Image
import os

#현재 파이썬 파일이 있는 폴더 기준으로 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def draw_image():
    global img
    shape = choice.get()
    if shape==1:
        image_path=os.path.join(BASE_DIR,"common_2.jpg")
        pil_img = Image.open(image_path)
        resized=pil_img.resize((200,300))
        img = ImageTk.PhotoImage(resized)
        canvas.create_image(20,20,anchor=NW,image=img)
    elif shape==2:
        image_path=os.path.join(BASE_DIR,"common_3.jpg")
        pil_img = Image.open(image_path)
        resized=pil_img.resize((200,300))
        img = ImageTk.PhotoImage(resized)
        canvas.create_image(200,20,anchor=NW,image=img)
    else:
        image_path=os.path.join(BASE_DIR,"common_4.jpg")
        pil_img = Image.open(image_path)
        resized=pil_img.resize((200,300))
        img = ImageTk.PhotoImage(resized)
        canvas.create_image(300,20,anchor=NW,image=img)

def cancle():
    canvas.delete("all")

root=Tk()
root.title("내가만든거")
root.geometry("600x800")

canvas=Canvas(root, width=400,height=600)
canvas.pack()

choice=IntVar()

Radiobutton(root, text="미피",padx=10,variable=choice, value=1).pack()
Radiobutton(root, text="짱구", padx=10, variable=choice,value=2).pack()
Radiobutton(root,text="짱구와친구들",padx=10, variable=choice, value=3).pack()
Button(root, text="그리기",command=draw_image).pack()
Button(root, text="지우기",command=cancle).pack()
Button(root,text="종료",command=root.quit).pack()

root.mainloop()
