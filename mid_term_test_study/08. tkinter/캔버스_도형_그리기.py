from tkinter import *

root=Tk()

w=Canvas(root, width=300, height=200)

w.pack()

w.create_line(0,0,300,200)
w.create_line(0,0,300,100,fill="red")
w.create_rectangle(50,25,200,100,fill="blue")

root.mainloop()