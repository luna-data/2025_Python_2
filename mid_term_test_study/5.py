from tkinter import *

class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id   # 학번
        self.name = name       # 이름

    def __eq__(self, other):
        # Student 객체끼리만 비교
        if isinstance(other, Student):
            return self.stu_id == other.stu_id  # 학번이 같으면 같은 학생
        return NotImplemented
    
def print_fields():
    #print("학번: %s\n 이름: %s" %(e1.get(), e2.get()))
    a=e1.get()
    if a.__eq__()==a:
        print("{e1.get}학생, 로그인 성공!")
    else:
        print("등록되지 않은 학번입니다")

students=[Student("202501","김민수"),Student("202502","이수정"),Student("202503","박지훈")]

root=Tk()
root.title("중간고사 5번")
root.geometry("250x150")



Label(root, text="학번").grid(row=0, column=0, padx=8, pady=6, sticky="e")
Label(root, text="이름").grid(row=1, column=0, padx=8, pady=6, sticky="e")

e1=Entry(root,width=15)
e2=Entry(root,width=15)
e1.grid(row=0, column=1,padx=8,pady=6)
e2.grid(row=1, column=1,padx=8,pady=6)

lable=Label(root, text="", fg="black")
lable.grid(row=3, column=0, columnspan=2, pady=8)

def login():
    sid=e1.get().strip()
    name=e2.get().strip()
    target=Student(sid,name)
    if target in students:
        lable.config(text=f"{name} 학생, 로그인 성공!", fg="blue")
    else:
        lable.config(text="등록되지 않은 학번입니다",fg="red")


Button(root, text="로그인", command=login).grid(row=2, column=0, sticky="w", pady=4) #간격
Button(root, text="취소", command=root.quit).grid(row=2, column=1, sticky="w", pady=4)

root.mainloop()

