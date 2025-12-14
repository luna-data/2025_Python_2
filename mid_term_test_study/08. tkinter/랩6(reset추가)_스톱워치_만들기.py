from tkinter import *

def startTimer():
    if (running):
        global timer
        timer+=1
        timeText.configure(text=str(timer))
    root.after(10,startTimer)

def start():
    global running
    running=True

def stop():
    global running
    running=False

def reset():
    global timer, running
    running=False
    timer=0
    timeText.config(text=format_time(timer))

def format_time(s):
    return f"{s}"

running=False

root=Tk()
root.title("간단한 스톱워치")
timer=0

timeText=Label(root, text=format_time(timer), font=("Helvetica",80))
timeText.pack()

startButton=Button(root, text="시작",bg="yellow",command=start)
startButton.pack(fill=BOTH)

stopButton=Button(root, text="중지",bg="yellow", command=stop)
stopButton.pack(fill=BOTH)
#초기화 추가
resetButton=Button(root, text="초기화",bg="yellow", command=reset)
resetButton.pack(fill=BOTH)

startTimer()
root.mainloop()