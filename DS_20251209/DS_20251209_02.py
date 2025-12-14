from tkinter import *
from PIL import ImageTk, Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 도형을 그리는 함수
def rectang():
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 150, 150, fill="red") 

def one():
    canvas.delete("all")
    canvas.create_oval(200, 80, 300, 180, fill="blue")

def draw_image():
    global img
    image_path=os.path.join(BASE_DIR,"common_3.jpg")
    pil_img = Image.open(image_path)
    img = ImageTk.PhotoImage(pil_img)
    canvas.create_image(20,20,anchor=NW,image=img)
    #canvas.create_text(200, 150, text="Hello Duksung", fill="blue", font=("Helvetica", 20, "bold"))

def clean():
    canvas.delete("all")

# 메인 윈도우 생성
root = Tk()
root.title("중간고사 7번")
root.geometry("420x440")

# 캔버스
canvas = Canvas(root, width=400, height=320, bg="white")
canvas.pack()

frame = Frame(root)
frame.pack(pady=10)

Button(frame, text="사각형", command=rectang).pack(side="left", padx=10)
Button(frame, text="원", command=one).pack(side="left", padx=10)
Button(frame,text="그림", command=draw_image).pack(side="left", padx=10)
Button(frame, text="지우기", command=clean).pack(side="left", pady=5)
Label(root, text="버튼을 눌러 도형을 선택하세요.",fg="black").pack()
root.mainloop()