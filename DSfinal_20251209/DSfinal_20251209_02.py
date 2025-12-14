from tkinter import *

class Person:
    def __init__(self,name):
        self.name=name
    
class HobbyPerson(Person):
    def __init__(self,name):
        super().__init__(name)
        self.hobbies=[]

    def add_hobby(self,hobby):
        self.clear_hobbies()
        self.hobbies.append(hobby)
        label.config(text=f"현재 취미: {hobby}")

    def clear_hobbies(self):
        self.hobbies.clear()


root=Tk()
root.title("문제 2")
root.geometry("380x260")

Label(root,text="이름: 김홍빈").pack()
frame2=Frame(root)
frame2.pack()

stu=HobbyPerson("김홍빈")
def down():
    #stu.clear_hobbies()
    if selected_hobby.get()==1:
        stu.add_hobby('게임')

    if selected_hobby.get()==2:
        stu.add_hobby('독서')


    if selected_hobby.get()==3:
        stu.add_hobby('운동')

    

def chogi():
    selected_hobby.set(0)
    stu.clear_hobbies()
    label.config(text="모든 선택을 해제했습니다.")
    

selected_hobby=IntVar()
b1=Radiobutton(frame2, text="게임", variable=selected_hobby, value=1).grid(row=0, column=1, padx=10, pady=5)
b2=Radiobutton(frame2, text="독서", variable=selected_hobby, value=2).grid(row=0, column=2, padx=10, pady=5)
b3=Radiobutton(frame2, text="운동", variable=selected_hobby, value=3).grid(row=0, column=3, padx=10, pady=5)

label=Label(root,text="취미를 선택하고 [등록하기]를 누르세요.")
label.pack()

frame2=Frame(root)
frame2.pack(pady=10)
Button(frame2,text="등록하기",command=down).pack(side="left",padx=10)
Button(frame2,text="초기화",command=chogi).pack(side="left",padx=10)



root.mainloop()