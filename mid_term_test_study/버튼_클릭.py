from tkinter import *

def button_clicked():
    print('button')

root=Tk()
root.geometry("300x200")

button=Button(root, text="click",command=button_clicked)
button.pack()

root.mainloop()