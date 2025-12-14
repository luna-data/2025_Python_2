from tkinter import *

LOG_FILE = "animal_log.txt"   # 🔥 파일 저장 경로


# ---------------------------
# 클래스 정의
# ---------------------------
class Animal:
    def speak(self):
        return '...'

class Dog(Animal):
    def speak(self):
        label.config(text="멍멍!")
        return "멍멍!"      # 🔥 파일 저장을 위해 문자열 반환

class Cat(Animal):
    def speak(self):
        label.config(text="야옹!")
        return "야옹!"      # 🔥 반환 필수

class Duck(Animal):
    def speak(self):
        label.config(text="꽥꽥!")
        return "꽥꽥!"      # 🔥 반환 필수


# ---------------------------
# 파일 저장 함수
# ---------------------------
def save_log(text):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(text + "\n")
    except:
        print("파일 저장 오류 발생")


# ---------------------------
# 버튼 클릭 시 동작
# ---------------------------
def make_sound(animal:Animal):
    sound = animal.speak()   # label에 표시
    save_log(sound)          # 🔥 파일에 기록


# ---------------------------
# Tkinter UI 구성
# ---------------------------
root = Tk()
root.title("동물 소리 듣기")

Label(root, text="동물 버튼을 눌러 소리를 들어보세요.").pack()

frame = Frame(root)
frame.pack(pady=10)

Button(frame, text='강아지', command=lambda: make_sound(Dog())).pack(side="left")
Button(frame, text='고양이', command=lambda: make_sound(Cat())).pack(side="left")
Button(frame, text='오리',  command=lambda: make_sound(Duck())).pack(side="left")

label = Label(root, text='(여기에 울음소리가 나옵니다)', font=("맑은 고딕", 15))
label.pack()

root.mainloop()
