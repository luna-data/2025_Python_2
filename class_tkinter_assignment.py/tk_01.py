from tkinter import *

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.borrowed=False

    def borrow(self):
        if not self.borrowed:
            self.borrowed=True
            lable1.config(text=f"{self.title}이(가) 대출되었습니다",fg="blue")

        else:
            lable1.config(text=f"{self.title}은(는) 이미 대출중입니다.",fg="blue")


    def return_book(self):
        if self.borrowed:
            lable1.config(text=f"{self.title}이(가) 반납되었습니다",fg="green")
            self.borrowed=False

        else:
            lable1.config(text=f"{self.title}은(는) 대출되지 않은 상태입니다.",fg="green")


def dachul():
    global book
    book=Book(e1.get(),e2.get())
    book.borrow()

def return_act():
    book.return_book()

    
root=Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("380x220")

Label(root,text="도서 대출 관리 시스템", font=("맑은 고딕", 20, "bold")).pack(pady=10)

row1=Frame(root)
row1.pack(pady=5)
Label(row1, text="제목").pack(side=LEFT, padx=5)
e1=Entry(row1)
e1.pack(side=LEFT,padx=5)

row2=Frame(root)
row2.pack(pady=5)
Label(row2, text="저자").pack(side=LEFT, padx=5)
e2=Entry(row2)
e2.pack(side=LEFT,padx=5)


frame = Frame(root)
frame.pack(pady=10)

Button(frame, text="대출", command=dachul).pack(side="left", padx=10)
Button(frame, text="반납", command=return_act).pack(side="left", padx=10)

lable1=Label(root,text="",font=("맑은 고딕",15))
lable1.pack(pady=10)

root.mainloop()


