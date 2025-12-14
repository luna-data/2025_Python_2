from tkinter import *

class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name):
        super().__init__(name)
        self.classes=[]

    def enrollCourse(self,subject):
        if subject not in self.classes:
            self.classes.append(subject)
            return self.classes
    
    def clearCourses(self):
        self.classes.clear() #리스트 초기화 방법

root=Tk()
root.title("문제4")
root.geometry("380x280")

stu=Student("홍길동")
Label(root,text=f"학생:{stu.name}", font=("맑은 고딕", 10, "bold")).pack()
frame=Frame(root)
frame.pack()

value1=IntVar()
Checkbutton(frame,text='python',variable=value1,onvalue=1,offvalue=0).pack(side="left")
value2=IntVar()
Checkbutton(frame,text='AI',variable=value2,onvalue=1,offvalue=0).pack(side="left")
value3=IntVar()
Checkbutton(frame,text='DataScience',variable=value3,onvalue=1,offvalue=0).pack(side="left")

def danglog():
    stu.clearCourses()
    if value1.get()==1:
        stu.enrollCourse('python')

    if value2.get()==1:
        stu.enrollCourse('AI')

    if value3.get()==1:
        stu.enrollCourse('DataScience')

    label1.config(text=f"등록된 과목: {stu.classes}")

def chogi():
    stu.clearCourses()
    value1.set(0)
    value2.set(0)
    value3.set(0)
    label1.config(text="모든 선택을 해제했습니다.")
    
label1=Label(root,text="과목을 선택하고 [등록하기]를 누르세요.")
label1.pack(pady=10)

frame2=Frame(root)
frame2.pack()
Button(frame2,text="등록하기",command=danglog).pack(side="left",padx=10)
Button(frame2,text="초기화",command=chogi).pack(side="left",padx=10)

root.mainloop()