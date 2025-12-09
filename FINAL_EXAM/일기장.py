#---일기장 만드는 프로그램
# 파일 불러오기 -> 라벨 콘피그로 내용 띄우는거/ 여러줄 불러오는 기능 추가하기
# 파일 저장하기 -> 새로운 텍스트 파일 내에 내가 쓴 일기 내용 저장되는거




from tkinter import *
import os

base_dir=os.path.dirname(__file__)

filename=os.path.join(base_dir, "out.txt")

def down():
    outfile=open(filename,"w",encoding="utf-8")
    outfile.write("=====new=====\n")
    return outfile.write(e1.get())

def load():
    openfile=open(filename,"r",encoding="utf-8")
    read=openfile.readline()
    label.config(text=read)

def stop():
    root.quit()

root=Tk()
root.title("일기장 애플리케이션")
root.geometry("700x500")

frame=Frame(root,width=600,height=400)
frame.pack()

e1=Entry(frame)
e1.pack()

Button(root,text="저장",command=down).pack()
Button(root,text="불러오기",command=load).pack()
Button(root,text="종료",command=stop).pack()
label=Label(root,text="이곳에 불러온 텍스트가 보여집니다")
label.pack()
#openfile.close()
#outfile.close()

root.mainloop()
