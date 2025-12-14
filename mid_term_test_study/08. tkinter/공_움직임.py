from tkinter import *

def move_oval():
    canvas.move(id,3,0) 
    if canvas.coords(id)[2]<400:#오른쪽 끝에 도달하지 않았을 때만 반복!!
        root.after(50,move_oval) #50Ms 이후에 move_oval 함수 호출

root=Tk()

canvas=Canvas(root, width=400, height=300)
canvas.pack()

id=canvas.create_oval(10,100,50,150,fill="green")
move_oval()

root.mainloop()