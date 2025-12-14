# 게임오버 텍스트 띄우면서, 재시작하면됨
# 게임오버 -> 레이븥, 팝업
# 재시작 -> 바로 재시작 또는 버튼으로 만들어서

from tkinter import * #값들의 움직임을 알 수 있어야함 , 디벨롭 하는 방식으로 하기!
import time #공이 찌그러짐?? 윈도우에서 찌그러짐
import random
import tkinter.messagebox as msgbox

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.paddle=paddle
        self.canvas.move(self.id,245,100) #이 부분에서 위치조정하는거!

        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0] #속도 지정하고 랜덤으로 섞어서 하나씩 데려옴

        self.y=-3
        self.hit_bottom=False
    

        #캔버스 높이 저장
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()

    #추가: 공이 패들에 부딪혔는지 검사하는 함수
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id) #패들의위치[px1,py1,px2,py2]
        #가로 방향으로 공과 패들이 겹치는지 확인하기
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
            #self.y=-3 #패배조건
            self.hit_bottom=True #바닥에 닿았을 경우 트루됨
            

        #이미 바닥에 부디혔다면 더이상 충돌 체크 안해도 됨
        if not self.hit_bottom:
            if self.hit_paddle(pos) ==True: #패들과 부딪혔는지 검사
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

paddle=Paddle(canvas,'blue') #패들 먼저 생성하지 않으면 볼이 오류가 생김
ball=Ball(canvas,paddle,'red')

label=Label(root,text="",font=("맑은 고딕", 20, "bold"))
label.pack()
game_running=True

def restart():
    global paddle,ball,game_running,label
    canvas.delete("all")
    paddle=Paddle(canvas,'blue') #패들 먼저 생성하지 않으면 볼이 오류가 생김
    ball=Ball(canvas,paddle,'red')
    label.config(text=" ")
    game_running=True\
    #버튼이 화면에서 보이지 않도록 숨기기!!
    if button is not None:
        button.pack_forget()

def game_over():
    global game_running,label,button
    game_running=False
    label.config(text="GAME OVER")
    #restart()
    button=Button(root,text="재시작",command=restart)
    button.pack()

while True:
    if game_running:
        if ball.hit_bottom==False: #게임 오버가 아닐때만 실행
            ball.draw()
            paddle.draw()
        else:
            game_over()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()

