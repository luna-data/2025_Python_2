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
#class Person:
    #def 

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
Checkbutton(frame3,text='예방접종 완료',variable=value1,onvalue=1,offvalue=0).pack(side="left")
value2=IntVar()
Checkbutton(frame3,text='중성화 완료',variable=value2,onvalue=1,offvalue=0).pack(side="left")

frame4=Frame(root)
frame4.pack(pady=10)

Label(text="홍길동의 반려동물 등록 완료!",fg="blue")
label1=Label(text=)
root.mainloop()