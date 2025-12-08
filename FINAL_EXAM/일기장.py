from tkinter import *
import os

base_dir=os.path.dirname(__file__)

filename=os.path.join(base_dir, "out.txt")

def down():
    outfile=open(filename,"w",encoding="utf-8")
    outfile.write(e1)

def load():
    openfile=open(filename,"r",encoding="utf-8")
    openfile.readline()

def stop():
    root.quit()

root=Tk()
root.title("일기장 애플리케이션")
root.geometry("700x500")

frame=Frame(root,'600x400')
frame.pack()

e1=Entry(frame)
e1.pack()

Button(root,text="저장",command=down).pack()
Button(root,text="불러오기",command=load).pack()
Button(root,text="종료",command=stop).pack()

openfile.close()
outfile.close()

root.mainloop()
