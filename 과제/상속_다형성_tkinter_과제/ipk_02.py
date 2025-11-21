from tkinter import *

class Pet:
    def speak(self):
        return "..."
    
class Dog(Pet):
    def speak(self):
        return "멍멍!"

class Cat(Pet):
    def speak(self):
        return "야옹!"

class Person:
    def __init__(self, name):
        self.pet=Pet()
        self.name=name

dog=Dog()
cat=Cat()
person=Person("홍길동")

root=Tk()
root.title("문제2")
root.geometry("400x200")
Label(root,text="동물을 선택해주세요",font=("맑은 고딕",10)).pack()

frame=Frame(root)
frame.pack()

def ch_dog():
    person.pet=dog
    label1.config(text="강아지를 선택했습니다.")

def ch_cat():
    person.pet=cat
    label1.config(text="고양이를 선택했습니다.")

def fin():
    label1.config(text=f"{person.name}의 반려동물 -> {person.pet.speak()}")

Button(frame, text="강아지 선택",command=ch_dog).grid(row=0, column=0, padx=10, pady=5)
Button(frame, text="고양이 선택",command=ch_cat).grid(row=0, column=1, padx=10, pady=5)
Button(root,text="말하기",command=fin).pack()

label1=Label(root,text="",fg="blue",font=("맑은 고딕",13))
label1.pack()

root.mainloop()