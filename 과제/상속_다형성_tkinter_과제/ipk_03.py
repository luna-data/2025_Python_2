from tkinter import *
import math

class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        pass
    def perimeter(self):
        pass
    def draw(self,canvas):
        pass

class Rectangle(Shape):
    def __init__(self,x,y,w,h):
        super().__init__(x,y)
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)
    def draw(self,canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.w,self.y+self.h, fill="tomato") 

class Circle(Shape):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.r=r
    def area(self):
        return math.pi*self.r**2
    def perimeter(self):
        return 2*self.r*math.pi
    def draw(self,canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill="skyblue")


# 메인 윈도우 생성
root = Tk()
root.title("문제3")
root.geometry("300x220")

# 캔버스
canvas = Canvas(root,bg="white")
canvas.pack()
label1=Label(root,text="도형을 선택하고 그리기를 누르세요.")
label1.pack()

frame = Frame(root)
frame.pack(pady=10)
choice=IntVar()

def draw_can():
    canvas.delete("all")
    if choice.get()==1:
        rectangle=Rectangle(50,50,100,60)
        rectangle.draw(canvas)
        label1.config(text=f"면적={rectangle.area():.2f}, 둘레={rectangle.perimeter():.2f}")
    
    elif choice.get()==2:
        circle=Circle(150,110,40)
        circle.draw(canvas)
        label1.config(text=f"면적={circle.area():.2f}, 둘레={circle.perimeter():.2f}")

Radiobutton(frame, text="사각형",variable=choice, value=1).pack(side="left", padx=10)
Radiobutton(frame, text="원", variable=choice, value=2).pack(side="left", padx=10)
Button(root,text="그리기",command=draw_can).pack()

root.mainloop()