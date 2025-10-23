from tkinter import *
from tkinter import messagebox

def login():
    lbl_result.config(text="로그인 시도 중...")

def confirm_exit():
    if messagebox.askyesno("종료 확인", "정말 종료하시겠습니까?"):
        root.quit()  # mainloop 종료

root = Tk()
root.title("로그인 창")

Label(root, text="아이디:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
Label(root, text="비밀번호:").grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_id = Entry(root)
entry_pw = Entry(root, show="*")
entry_id.grid(row=0, column=1, padx=5, pady=5)
entry_pw.grid(row=1, column=1, padx=5, pady=5)

lbl_result = Label(root, text="", fg="blue")
lbl_result.grid(row=2, column=0, columnspan=2, pady=5)

Button(root, text="로그인", command=login).grid(row=3, column=0, padx=5, pady=5, sticky="we")
Button(root, text="종료", command=confirm_exit).grid(row=3, column=1, padx=5, pady=5, sticky="we")

root.mainloop()
