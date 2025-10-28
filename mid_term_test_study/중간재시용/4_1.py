from tkinter import *

def delete_can():
    canvas.delete("all")
    value_shape=shape.get()
    if value_shape==1:
        canvas.create_rectangle(50,50,200,150,fill='red')
    elif value_shape==2:
        canvas.create_oval(50,50,200,150,fill="blue")
    elif value_shape==3:
        canvas.create_text(150,100, text="Hello Duksung",fill="blue",font=('Arial',20,"bold"))

root=Tk()
root.title("중간고사 4번")
root.geometry("400x400")
shape=IntVar(value=1)

canvas=Canvas(root, width=300, height=300)
canvas.grid(row=0,column=1,columspan=3)


Radiobutton(root, text="사각형",padx=20, variable=shape,value=1).gird(row=0,column=0,sticky="W")
Radiobutton(root, text="원",padx=20, variable=shape,value=2).gird(row=0,column=1,sticky="W")
Radiobutton(root, text="텍스트",padx=20, variable=shape,value=3).gird(row=0,column=2,sticky="W")
Button(root, text="그리기", command=delete_can).grid(row=1,column=1,columnspan=3)

root.mainloop()