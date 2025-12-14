from tkinter import *

class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id   # 학번
        self.name = name       # 이름

    def __eq__(self, other):
        # Student 객체끼리만 비교
        if isinstance(other, Student):
            return self.stu_id == other.stu_id  # 학번이 같으면 같은 학생
        return False
    
def print_fields():
    print("학번: %s\n 이름: %s" %(e1.get(), e2.get()))
    if e1.get() in students:
        print("{e1.get}학생, 로그인 성공!")
        
root=Tk()
root.title("중간고사 5번")
root.geometry("250x150")

students=[Student("202501","김민수"),Student("202502","이수정"),Student("202503","박지훈")]

Label(root, text="아이디").grid(row=0)
Label(root, text="패스워드").grid(row=1)

e1=Entry(root)
e2=Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
root.create_text(text=print_fileds)

Button(root, text="로그인", command=print_fields).grid(row=3, column=0, sticky="w", pady=4) #간격
Button(root, text="취소", command=root.quit).grid(row=3, column=1, sticky="w", pady=4)

root.mainloop()

