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

canvas=Canvas(root,width=200,height=200)
canvas.pack()
def delete_file():
    root.delete("all")
    
Button(root,text="파일열기",command=file_open).pack()
Button(root,text="지우기",command=delete_file).pack()

root.mainloop()