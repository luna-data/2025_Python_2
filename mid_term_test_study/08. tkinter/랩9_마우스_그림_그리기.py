from tkinter import *

start_x=start_y=0

def start_drawing(event):
    global start_x, start_y
    start_x, start_y=event.x, event.y

def draw(event):
    global start_x, start_y
    end_x, end_y=event.x, event.y

    canvas.create_line(start_x, start_y, end_x, end_y, fill="black")
    start_x, start_y=end_x,end_y


root=Tk()
canvas=Canvas(root, width=500, height=300)
canvas.pack()

canvas.bind("<Button-1>",start_drawing)
canvas.bind("<B1-Motion>",draw)

root.mainloop()