#+본인의 아이디어 아무거나 추가 (주석달기)
# 파란색 공을 추가하여 점수는 2배로 받고, 공이 하나라도 떨어지면 바로 게임 끝
# 공이 랜덤으로 설정되어 파란색공과 빨간색 공이 합쳐져서 같은 경로로 움직이는 경우가 있음!!

from tkinter import * #값들의 움직임을 알 수 있어야함 , 디벨롭 하는 방식으로 하기!
import time 
import random
#import tkinter.messagebox as msgbox
bcount=0
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.paddle=paddle
        self.canvas.move(self.id,245,100) 

        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0] 

        self.y=-3
        self.hit_bottom=False
    
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()


    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id) 
        if pos[2]>=paddle_pos[0] and pos[0] <=paddle_pos[2]: 
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False
        
    
    def draw(self):
        global bcount
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)

        if pos[1]<=0: 
            self.y=3 
        
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True 
            

        if not self.hit_bottom:
            if self.hit_paddle(pos) ==True: 
                self.y=-3
                bcount+=1

        if pos[0]<=0:
            self.x=3

        if pos[2]>=self.canvas_width: 
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
ball1=Ball(canvas,paddle,'red')
ball2=Ball(canvas,paddle,'blue')# ball 하나 추가

label=Label(root,text="",font=("맑은 고딕", 20, "bold"))
label.pack()
game_running=True

def restart():
    global paddle,ball1,ball2,game_running,label,bcount
    canvas.delete("all")
    paddle=Paddle(canvas,'blue') #패들 먼저 생성하지 않으면 볼이 오류가 생김
    ball1=Ball(canvas,paddle,'red')
    ball2=Ball(canvas,paddle,'blue') 
    label.config(text=" ")
    game_running=True
    bcount=0
    #버튼이 화면에서 보이지 않도록 숨기기!!
    if button is not None:
        button.pack_forget()

def game_over():
    global game_running,label,button
    game_running=False
    label.config(text=f"GAME OVER, 점수: {bcount}점")
    #restart()
    button=Button(root,text="재시작",command=restart)
    button.pack()

while True: #볼 하나가 바닥으로 떨어져도 게임은 계속됨
    if game_running:
        if ball1.hit_bottom==False and ball2.hit_bottom==False: #게임 오버가 아닐때만 실행
            ball1.draw()
            ball2.draw()
            paddle.draw()
        elif ball1.hit_bottom==True and ball2.hit_bottom==False:
            ball2.draw()
            paddle.draw()
        elif ball1.hit_bottom==False and ball2.hit_bottom==True:
            ball1.draw()
            paddle.draw()
        else:
            game_over()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()

