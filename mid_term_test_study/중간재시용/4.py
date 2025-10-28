from tkinter import *

def draw():
    w.delete("all")
    sel=shape_var.get()
    if sel==1:
        w.create_rectangle(50,25,200,100,fill="red")
    elif sel==2:
        w.create_oval(50,50,200,100,fill="blue")
    elif sel==3:
        w.create_text(150,100,text="Hello Duksung",fill="blue",font=('Arial',20,'bold'))


win=Tk()
win.title("중간고사 4번")
win.geometry("400x400")
shape_var=IntVar(value=1)

w=Canvas(win, width=300, height=250, bg="white")
w.grid(row=0,column=0,columnspan=3, padx=10, pady=10)


Radiobutton(win, text="사각형", padx=20, variable=shape_var,value=1).grid(row=1,column=0,sticky="w",padx=10)
Radiobutton(win, text="원", padx=20, value=2,variable=shape_var).grid(row=1,column=1,sticky="w")
Radiobutton(win, text="텍스트", padx=20, value=3,variable=shape_var).grid(row=1,column=2,sticky="w")
Button(win, text="그리기", command=draw).grid(row=2,column=0,columnspan=3,padx=10)

win.mainloop()