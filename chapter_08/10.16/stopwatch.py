import tkinter as tk

def startTimer():
    """
    10ms 후에 호툴되어 타이머를 업데이트하는 함수
    """

    if running:
        global timer
        timer+=1
        timeText.config(text=str(timer))
    root.after(10,startTimer)

def start():
    """
    시작 버튼 클릭 시 호출되는 함수
    """
    global running
    running=True

def stop():
    """
    중지 버튼 클릭 시 호출되는 함수
    """
    global running
    running=False

running=False
    
root=tk.Tk()

timer=0
timeText=tk.Label(root, text="0", font=("Helvetica", 80))
timeText.pack()

startButton=tk.Button(root, text="시작",bg="yellow",command=start)
startButton.pack(fill=tk.BOTH)

stopButton=tk.Button(root, text="중지",bg="yellow",command=stop)
stopButton.pack(fill=tk.BOTH)

startTimer()
root.mainloop()
