from tkinter import *

root=Tk()
root.geometry("300x100")

button1=Button(root, text="버튼1",bg="red",fg="white")
button1.grid(row=0,column=0)

button2=Button(root, text="버튼2",bg="green",fg="black")
button2.grid(row=0,column=1)

button3=Button(root, text="버튼3",bg="blue",fg="white")
button3.grid(row=1,column=0)

button4=Button(root, text="버튼4",bg="yellow",fg="black")
button4.grid(row=1,column=1)

root.mainloop()