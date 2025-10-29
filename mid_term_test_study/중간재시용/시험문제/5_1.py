from tkinter import *

class Student:
    def __init__(self, stu_id, name):
        self.stu_id=stu_id
        self.name=name

    def __eq__(self,other):
        if isinstance(other, Student):
            return self.stu_id == other.stu_id  # 학번이 같으면 같은 학생
        return NotImplemented
    
students=[Student("202501","김민수"), Student("202502","이수정"), Student("202503","박지훈")]

root=Tk()
root.title("중간고사 5번")
root.geometry("250x150")

def login():
    stu=Student(e1.get(),e2.get())
    if stu in students:
        lable.config(text=f"{stu.name}학생, 로그인 성공!")
    else:
        lable.config(text="등록되지 않은 학생입니다.")

Label(root, text="학번").grid(row=0)
Label(root, text="이름").grid(row=1)

e1=Entry(root)
e2=Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

lable=Label(root, text="",fg="blue" )
lable.grid(row=2, column=0, columnspan=2, pady=5)

Button(root, text="로그인", command=login).grid(row=3, column=0, sticky="w", pady=4) #간격
Button(root, text="취소", command=root.quit).grid(row=3, column=1, sticky="w", pady=4)

root.mainloop()



