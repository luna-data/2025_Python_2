from tkinter import * #값들의 움직임을 알 수 있어야함 , 디벨롭 하는 방식으로 하기!
import time #공이 찌그러짐?? 윈도우에서 찌그러짐
import random

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.paddle=paddle
        self.canvas.move(self.id,245,100) #이 부분에서 위치조정하는거!

        #self.x=0 #좌우 속도 =0 위아래만 움직임
        #self.y=-1 #위쪽 -1로 이동
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0] #속도 지정하고 랜덤으로 섞어서 하나씩 데려옴

        self.y=-3
        self.hit_bottom=False
    

        #캔버스 높이 저장
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0] <=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False
        
    
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)#공의 위치 저장
        #print(self.canvas.coords(self.id))#저장된 위치를 출력 -> 위치 계속 출력되니까 주석처리 

        if pos[1]<=0: #사각형을 만든다하면 맨 위 왼쪽이 (0,0)이고 윗부분에 그려지는 모든 원은 y=0이어야함!
            self.y=3 # 천장에 닿으면 아래로 방향 전환하는거!!!
        
        if pos[3]>=self.canvas_height:
            #self.y=-3
            self.hit_bottom=True

        if not self.hit_bottom:
            if self.hit_paddle(pos) ==True:
                self.y=-3

        if pos[0]<=0: #왼쪽벽에 닿으면 오른쪽으로 튕기기 -> 3씩 증가
            self.x=3

        if pos[2]>=self.canvas_width: #오른쪽 벽에 닿으면 왼쪽으로 튕기기 -> 3씩 감소
            self.x=-3




class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)

        self.x=0
        self.canvas_width=self.canvas.winfo_width() #너비 저장하는거!

        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def turn_left(self,evt):
        self.x=-2

    def turn_right(self,evt):
        self.x=2

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)

        if pos[0]<=0:
            self.x=0 #2로 바꾸면 혼자 움직임

        elif pos[2]>=self.canvas_width:
            self.x=0 #-2로 바꾸면 혼자 움직임

root=Tk()
root.title("Game")
root.resizable(0,0)
root.wm_attributes("-topmost",1)

canvas=Canvas(root,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
root.update()

paddle=Paddle(canvas,'blue')
ball=Ball(canvas,paddle,'red')


while True:
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()