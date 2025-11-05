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
            lable1.config(text=f"{self.title}은(는) 이미 대출중입니다.",fg="red")
        
    def return_book(self):
        if self.borrowed:
            lable1.config(text=f"{self.title}이(가) 반납되었습니다",fg="green")
            self.borrowed=False

        else:
            lable1.config(text=f"{self.title}은(는) 대출 목록에 없습니다.",fg="red")

#대출현황리스트
borrowed_books=[]

#이벤트핸들러
def update_borrowed_list():
    if book.borrowed==True:
        books=", ".join([f"{title}({author})" for b in borrowed_books])
        borrowed_books.append(title(author))
        return borrowed_books
    else:
        books="현재 대출 중인 도서가 없습니다."



def dachul():
    global title,author,book
    title=e1.get().strip()
    author=e2.get().strip()

    book=Book(title,author)
    condition=book.borrow()
    borrowed_books.append(book)
    lable1.config(text=condition, fg="blue")
    update_borrowed_list()

def return_act():
    if not title or not author:
        lable1.config(text="제목과 저자를 모두 입력해주세요", fg="red")
    for b in borrowed_books:
        if b.title == title and b.author == author:
            lable1.config(text=f"{title}이(가) 이미 반납되었습니다.", fg="red")
            return
        
    condition=book.return_book()
    lable1.config(text=condition, fg="red")


#GUI
root=Tk()
root.title("도서 대출 관리 프로그램")
root.geometry("430x280")

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

lable2=Label(root,text="대출 현황: 현재 대출 중인 도서가 없습니다.",font=("맑은 고딕",10)) #대출현황 레이블
lable2.pack(pady=5)

root.mainloop()
