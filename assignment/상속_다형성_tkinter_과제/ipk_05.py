from tkinter import *
class Pet:
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        return "..."
    
class Dog(Pet):
    def speak(self):
        return "멍멍!"
class Cat(Pet):
    def speak(self):
        return "야옹!"
class Person:
    def __init__(self,name,pet=None):
        self.name=name
        self.pet=pet

def sign():
    name=Name()
    sound= Sound()
    if value1.get()==1:
        b= "O"
    else:
        b= "X"
    
    if value2.get()==1:
        c= "O"
    else:
        c="X"
    #justify 를 왼쪽으로하면 왼쪽 정렬됩니당!
    label1.config(text=f"홍길동의 반려동물 등록 완료! \n이름: {name} \n소리: {sound} \n예방접종: {b} 중성화: {c}",justify="left")

def Name():
    na=e_name.get().strip()
    if na=="":
        return "이름 없음"
    else:
        return na

def Sound():
    p_name=Name()
    if value.get()==1:
        dog=Dog(p_name)
        return dog.speak()
        
    else:
        cat=Cat(p_name)
        return cat.speak()

def reset(): # 초기화는 너무 잘됨
    value1.set(0)
    value2.set(0)
    value.set(0)
    e_name.delete(0,END)
    label1.config(text="등록 정보를 확인하세요.")

root=Tk()
root.title("문제 5")
root.geometry("700x300")
Label(root,text="반려동물 등록하기").pack()

frame1=Frame(root)
frame1.pack()

Label(frame1, text="반려동물 이름: ").grid(row=0, column=0, padx=10, pady=5)
e_name = Entry(frame1)
e_name.grid(row=0, column=1, padx=10, pady=5)

frame2=Frame(root)
frame2.pack()

Label(frame2,text="종류: ").grid(row=0, column=0, padx=10, pady=5)
value=IntVar()
Radiobutton(frame2, text="강아지", variable=value, value=1).grid(row=0, column=1, padx=10, pady=5)
Radiobutton(frame2, text="고양이", variable=value, value=2).grid(row=0, column=2, padx=10, pady=5)

frame3=Frame(root)
frame3.pack()
Label(frame3,text="옵션: ").grid(row=0, column=0, padx=10, pady=5)

value1=IntVar()
Checkbutton(frame3,text='예방접종 완료',variable=value1,onvalue=1,offvalue=0).grid(row=0, column=1, padx=10, pady=5)
value2=IntVar()
Checkbutton(frame3,text='중성화 완료',variable=value2,onvalue=1,offvalue=0).grid(row=0, column=2, padx=10, pady=5)

frame4=Frame(root)
frame4.pack(pady=10)

label1=Label(frame4,text="",fg="blue")
label1.pack()

Button(frame4,text=" 등록하기",command=sign).pack(side="left",padx=10)
Button(frame4,text=" 초기화",command=reset).pack(side="left",padx=10)
root.mainloop()