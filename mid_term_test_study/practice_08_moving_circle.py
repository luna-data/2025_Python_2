import tkinter as tk
import random

class MovingShapeApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Moving Shape App")

        #캔버스 생성
        self.canvas=tk.Canvas(root, width=800, height=800, bg="white")
        self.canvas.pack() #고정

        #원 만들기
        self.shape=self.canvas.create_oval(100,100,200,200,fill="red") #100,100~200,200 까지 원을 그리겠다는 의미

        #키보드 이벤트 
        self.root.bind("<Up>",self.move_up)
        self.root.bind("<Down>",self.move_down) 
        self.root.bind("<Left>",self.move_left)
        self.root.bind("<Right>",self.move_right)

        #마우스 이벤트
        self.canvas.bind("<B1-Motion>",self.change_color)

    #이동 메소드
    def move_shape(self,dx,dy):
        self.canvas.move(self.shape,dx,dy)

    def move_up(self,event):
        self.move_shape(0,-10)

    def move_down(self, event):
        self.move_shape(0,10)

    def move_left(self,event):
        self.move_shape(-10,0)

    def move_right(self,event):
        self.move_shape(10,0)


    #색변경 메소드
    def change_color(self,event):
        colors=["red","orange","green","blue","purple","pink"]
        color=random.choice(colors)
        self.canvas.itemconfig(self.shape,fill=color)

root=tk.Tk()
app=MovingShapeApp(root)
root.mainloop()
# move_shape, move_up, move_downn, move_left, move_right, change_color