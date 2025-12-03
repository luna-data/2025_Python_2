from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox 

space_cnt=0
upper_cnt=0
lower_cnt=0
try:
    def select_file():
        file_path=filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
        if not file_path:
            label1.config(text="선택된 파일: (없음)")
            return 
        with open(file_path,'r',encoding="utf-8") as f:
            label1.config(text=f"선택된 파일: {file_path}")
            count_stats(f)
            label2.config(text=f"스페이스: {space_cnt}, 대문자: {upper_cnt}, 소문자: {lower_cnt}")

except FileNotFoundError:
    msgbox.showwarning("에러","파일을 찾을 수 없습니다.")
except IOError:
    msgbox.showwarning("에러",'파일을 읽는 중에 오류가 발생했습니다.')


def count_stats(text):
    global space_cnt,upper_cnt,lower_cnt
    for line in text:
        for ch in line:
            if ch==" ":
                space_cnt+=1
            elif ch.isupper():
                upper_cnt+=1
            elif ch.islower():
                lower_cnt+=1

    return space_cnt,upper_cnt,lower_cnt





#msgbox.showwarning("안내", "메뉴를 선택하세요.") -> error 표시 시 사용하기

root=Tk()
root.geometry("520x220")
root.title("문제5")
Label(text="텍스트 파일을 선택하여 스페이스, 대문자, 소문자 개수를 세어보세요.").pack()
Button(root,text="파일 선택",command=select_file).pack()
label1=Label(root,text="선택된 파일: ")
label1.pack()
label2=Label(root,text="")
label2.pack()

root.mainloop()