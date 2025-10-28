from tkinter import *
from PIL import Image, ImageTk
import os
path = os.path.join(base_dir, "common.jpg")  # JPG 그대로

root=Tk()
root.title("중간고사_이미지뷰어")
root.geometry('600x450')

def chogi():
    root.delete("all")
    sel=shape_var.get()

Button(root, text="파일열기",file="common.jpg").grid(row=0,column=0)
Button(root, text="지우기",comman=chogi).grid(row=1,column=0)
Radiobutton(root, text="사각형", padx=20, variable=shape_var,value=1).grid(row=1,column=0,sticky="w",padx=10)
Radiobutton(root, text="사각형", padx=20, variable=shape_var,value=1).grid(row=1,column=0,sticky="w",padx=10)