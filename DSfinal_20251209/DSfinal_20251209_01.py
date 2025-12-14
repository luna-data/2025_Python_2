from tkinter import *

class DrawableShape():
    def __init__(self,canvas):
        self.canvas=canvas

    def draw(self):
        pass

class Square(DrawableShape):
    def __init__(self,canvas,x,y,size):
        super().__init__(canvas)
        self.x=x
        self.y=y
        self.size=size

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(100, 50, 40) 

class Circle(DrawableShape):
    def __init__(self,x,y,radius):
        super().__init__(canvas)
        self.x=x
        self.y=y
        self.radius=radius
        self.canvas.delete("all")
        self.canvas.create_oval(200, 120, 30) 

shapes=[]

def saka():
    global sq
    sq=Square(100,50,40)
    shapes.append(sq)
    

def one():
    global on
    on=Circle(200,120,30)
    shapes.append(sq)
    

def all_do():
    for i in shapes:
        i.draw()
        return i


root=Tk()
root.geometry()

left=Frame(root,padx=10,pady=10)
left.pack(side='left', expand=True)

right=Frame(root,padx=10,pady=10)
right.pack(side="left", expand=True)


canvas=Canvas(right,width=400,height=300)
canvas.pack()

Button(right,text="사각형 추가",command=saka).pack(side=left)
Button(right,text="사각형 추가",command=one).pack(side=left)
Button(right,text="사각형 추가",command=all_do).pack(side=left)

root.mainloop()