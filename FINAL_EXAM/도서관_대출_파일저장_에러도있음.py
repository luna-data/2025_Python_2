#문제: 도서 대출 시스템을 파일과 연동하도록 기능을 확장하시오.

#아래 제시된 기존 코드(Book 클래스, GUI, 대출/반납 로직)는 그대로 유지하되,
#파일 I/O 기능을 추가하여 프로그램을 완성하시오.

#1 ✔ 추가 요구사항 1 — 프로그램 실행 시 자동으로 파일에서 대출 목록 불러오기
#2 ✔ 추가 요구사항 2 — 대출/반납이 발생할 때마다 파일에 즉시 저장
#3 ✔ 추가 요구사항 3 — “대출 기록 보기” 버튼 추가
#4 ✔ 추가 요구사항 4 — 파일이 손상되었을 경우 오류 메시지를 출력
#5 
from tkinter import *

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.borrowed=False

    def borrow(self):
        if not self.borrowed:
            self.borrowed=True
          
        
    def return_book(self):
        self.borrowed=False

def load_from_file():
    try:
        with open("borrowed_books.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "," not in line:
                    raise ValueError("파일 형식 오류")
                title, author = line.split(",", 1)
                b = Book(title, author)
                b.borrow()
                borrowed_books.append(b)
    except FileNotFoundError:
        pass  # 파일 없으면 무시하고 시작
    except Exception:
        lable1.config(text="⚠ 파일 형식 오류: borrowed_books.txt를 확인하세요.", fg="red")


def save_to_file():
    with open("borrowed_books.txt", "w", encoding="utf-8") as f:
        for b in borrowed_books:
            f.write(f"{b.title},{b.author}\n")

#대출현황리스트
borrowed_books=[]

#이벤트핸들러
def update_borrowed_list():
    if borrowed_books:
        joined = ", ".join([f"{b.title}({b.author})" for b in borrowed_books])
        lable2.config(text=f"대출 현황: {joined}")
    else:
        lable2.config(text="대출 현황: 현재 대출 중인 도서가 없습니다.")

def find_book(title:str,author:str):
    for b in borrowed_books:
        if b.title==title and b.author==author:
            return b
    return None

def dachul():
    title=e1.get().strip()
    author=e2.get().strip()

    if not title or not author:
        lable1.config(text="제목과 저자를 모두 입력해주세요", fg="red")
        return
    if find_book(title, author) is not None:
        lable1.config(text=f"『{title}』은(는) 이미 대출중입니다.", fg="red")
        return
    
    book=Book(title,author)
    book.borrow()
    borrowed_books.append(book)
    lable1.config(text=f"{title}이(가) 대출되었습니다", fg="blue")
    update_borrowed_list()
    borrowed_books.append(book)
    save_to_file()
    borrowed_books.remove()
    save_to_file()

    
## 파일에서 읽어오는 거!!
def show_file():
    try:
        with open("borrowed_books.txt", "r", encoding="utf-8") as f:
            text.delete("1.0", END)
            text.insert(END, "현재 대출 중인 목록:\n")
            for line in f:
                title, author = line.strip().split(",", 1)
                text.insert(END, f"- {title} ({author})\n")
    except FileNotFoundError:
        text.delete("1.0", END)
        text.insert(END, "대출 기록이 없습니다.")


def return_act():
    title=e1.get().strip()
    author=e2.get().strip()

    if not title or not author:
        lable1.config(text="제목과 저자를 모두 입력해주세요", fg="red")
        return
    b = find_book(title, author)

    if b is None:
        lable1.config(text=f"『{title}』은(는) 대출 목록에 없습니다.", fg="red")
        return

    b.return_book()         
    borrowed_books.remove(b)     
    lable1.config(text=f"{title}이(가) 반납되었습니다", fg="green")
    update_borrowed_list()


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

Button(root, text="대출 기록 보기", command=show_file).pack(pady=3)

text = Text(root, width=50, height=6)
text.pack()

root.mainloop()