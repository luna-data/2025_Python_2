from tkinter import *

root=Tk()
choice=IntVar()

Label(root, 
      justify=LEFT,
      padx=20).pack()

Radiobutton(root, text="사각형", padx=20, variable=choice, value=1).pack(anchor=W)
Radiobutton(root, text="원", padx=20, variable=choice, value=2).pack(anchor=W)
Radiobutton(root, text="텍스트", padx=20, variable=choice, value=3).pack(anchor=W)


root.mainloop()