from tkinter import *

def print_field():
    print("아이디: %s\n 패스워드: %s" %(e1.get(), e2.get()))

root=Tk()
root.title("tk")

Label(root,text="아이디").grid(row=0,column=0)
Label(root, text="패스워드").grid(row=1,column=0)

e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

Button(root, text="로그인", command=print_field).grid(row=3,column=0)
Button(root, text="취소",command=root.quit).grid(row=3,column=1)

root.mainloop()