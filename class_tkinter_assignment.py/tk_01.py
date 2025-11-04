from tkinter import *

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.borrowed=False

    def borrow(self):
        if not self.borrowed:
            self.borrowed=True
            lable.config(text=f"{e1.get()}이(가) 대출되었습니다")

        else:
            lable.config(text=f"{e1.get()}은(는) 이미 대출 중입니다")

    def return_book(self):
        if self.borrowed:
            lable.config(text=f"{e1.get()}이(가) 반납되었습니다")
            self.borrowed=False

        else:
            lable.config(text=f"{e1.get()}은(는) 대출되지 않은 상태입니다.")

root=Tk()
root.title("도서 대출 관리 프로그램")

Label(root, text="제목").grid(row=0)
Label(root, text="저자").grid(row=1)

e1=Entry(root)
e2=Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
book=Book(e1.get(),e2.get())

lable=Label(root, text="",fg="blue" )
lable.grid(row=2, column=0, columnspan=2, pady=5)

Button(root, text="대출", command=book.borrow()).grid(row=3, column=0, sticky="w", pady=4) #간격
Button(root, text="반납", command=book.return_book()).grid(row=3, column=1, sticky="w", pady=4)


root.mainloop()


