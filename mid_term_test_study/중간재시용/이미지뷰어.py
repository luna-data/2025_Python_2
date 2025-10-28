from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("중간고사_이미지뷰어")
root.geometry("600x450")
def file_open():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "common.jpg")
    pil_img = Image.open(path)
    img = ImageTk.PhotoImage(pil_img)
    canvas.create_image(20, 20, anchor=NW, image=img)

def delete_file():
    root.delete("all")
    
Button(root,text="파일열기",command=file_open).grid(row=0,column=0,padx=5)
Button(root,text="지우기",command=delete_file).grid(row=0,column=1,padx=5)