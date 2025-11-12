from tkinter import *

class Animal:
    def speak(self):
        return '...'

class Dog(Animal):
    def speak(self):
        return label.config(text="멍멍!")

class Cat(Animal):
    def speak(self):
        return label.config(text="야옹!")

class Duck(Animal):
    def speak(self):
        return label.config(text="꽥꽥!")

def make_sound(animal:Animal):
    #animal=Animal()
    animal.speak()
    #label.config(text=sound)

root=Tk()
root.title("동물 소리 듣기")

Label(root,text="동물 버튼을 눌러 소리를 들어보세요.").pack()

frame=Frame(root)
frame.pack(pady=10)
Button(frame,text='강아지',command=lambda:make_sound(Dog())).pack(side="left")
Button(frame,text='고양이',command=lambda:make_sound(Cat())).pack(side="left")
Button(frame,text='오리',command=lambda:make_sound(Duck())).pack(side="left")
# lambda는 바로 호출되는 함수를 지연호출하기 위한 요소!!

label=Label(root,text='(여기에 울음소리가 나옵니다)',font=("맑은 고딕",15))
label.pack()

root.mainloop()