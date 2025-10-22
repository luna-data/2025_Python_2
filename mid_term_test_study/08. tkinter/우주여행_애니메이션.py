from tkinter import *
import random

#별생성
def create_star(canvas,x,t,radius):
    return canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="white",outline="")
#우주선생성
def create_spacecraft(canvas,x,t,image):
    return canvas.create_image(x,t,image=image)
#우주선이동
def move_spacecraft(canvas,obj_id,dx,dy):
    canvas.move(obj_id,dx,dy)
#우주선애니메이션
def animate_spacecraft():
    x,y,=canvas.coords(spacecraft)
    if x< -50 or x> window_width + 50 or y< -50 or y> window_height + 50 :
        reset_spacecraft()
    else:
        move_spacecraft(canvas, spacecraft,dx,dy)
    window.after(200,animate_spacecraft)
#우주선리셋
def reset_spacecraft():
    global dx, dy

    




window=Tk()
window.title("우주여행 애니메이션")
window_width=800
window_height=600

canvas=Canvas(window, width=window_width, height=window_height, bg="black")
canvas.pack()

spacecraft_image=PhotoImage(file="image.png")

statrs=[]
for _ in range(50):
    x=random.randint(0,window_width)
    t=random.randint(0,window_height)
    radius=random.randint(1,10)
    stars.append(create_star(canvas,x,y,image=spacecraft_image))

x=random.randint(0,window_width)
y=random.randint(0,window_height)
spacecraft=create_spacecratf(canvas,x,y,image=spacecraft_image)
dx=random.randint(0,30)
dy=random.randint(-30,0)

animate_spacecraft()
window.mainloop()