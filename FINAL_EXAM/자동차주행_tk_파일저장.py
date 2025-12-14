from tkinter import *
import os
base_dir=os.path.dirname(__file__)

# 전역 파일 경로 지정
filepath = os.path.join(base_dir, "drive_log.txt")

#상속구조
class Vehicle:
    def __init__(self,name):
        self.name=name
    
    def drive(self):
        NotImplementedError

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):                
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."


# -----------------------------
# 차량 버튼 기능
# -----------------------------
def drive_car():
    name = e1.get().strip()
    if name == "":
        car = Car("이름없음")
    else:
        car = Car(name)
    message = car.drive()
    append_log(message)


def drive_truck():
    name = e1.get().strip()
    if name == "":
        truck = Truck("이름없음")
    else:
        truck = Truck(name)
    message = truck.drive()
    append_log(message)


# -----------------------------
# 로그 파일 저장(추가 기능)
# -----------------------------
def save_log_to_file(message):
    """drive_log.txt 파일에 한 줄 저장하는 함수(명시적 분리)"""
    try:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except IOError:
        label.config(text="파일 저장 중 오류 발생")


# -----------------------------
# 로그 추가 (버튼 → 화면 출력 + 파일 저장)
# -----------------------------
def append_log(message):
    label.config(text=message)   # GUI 출력
    save_log_to_file(message)    # 파일 저장 (새로 추가된 파일 저장 기능)


# -----------------------------
# 로그파일 비우기
# -----------------------------
def clear_dog():
    clear_log_file()
    label.config(text="로그 파일을 비웠습니다.")


def clear_log_file():
    with open(filepath, "w", encoding="utf-8") as f:
        pass  # 내용 삭제만 수행


# -----------------------------
# GUI 구성
# -----------------------------
root = Tk()
root.title("문제4")
root.geometry("400x320")

Label(root, text="차량 이름을 입력하세요: ").pack()

e1 = Entry(root)
e1.pack()

label = Label(root, text="결과가 여기에 표시됩니다.")
label.pack()

frame = Frame(root)
frame.pack()

Button(frame, text="자동차 주행", command=drive_car).pack()
Button(frame, text="트럭 주행", command=drive_truck).pack()
Button(frame, text="로그 비우기", command=clear_dog).pack()

root.mainloop()
