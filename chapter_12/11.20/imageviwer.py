from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

def open_image():
    file_path=filedialog.askopenfilename(filetypes=[("Image files","*.png;*.jpg;*jpeg;*.gif")])
    if file_path:
        image=Image.open(file_path)
        photo=ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image=photo

app=Tk()
app.title("이미지 뷰어")
app.geometry("300x200")
label=Label(app)
label.pack()

menubar=Menu(app)
app.config(menu=menubar)
file_menu=Menu(menubar,tearoff=False)
menubar.add_cascade(label="파일",menu=file_menu)
file_menu.add_command(label="열기",command=open_image)
file_menu.add_separator()
file_menu.add_command(label="종료",command=app.quit)

app.mainloop()