from tkinter import *
import os
base_dir=os.path.dirname(__file__)

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

#car
def drive_car():
    name=e1.get().strip()
    if name=="":
        car=Car("이름없음")
    else:
        car=Car(name)
    message=car.drive()
    append_log(message)

#truck
def drive_truck():
    name=e1.get().strip()
    if name=="":
        truck=Truck("이름없음")
    else:
        truck=Truck(name)
    message=truck.drive()
    append_log(message)


#clear
def clear_dog():
    clear_log_file()
    label.config(text="로그 파일을 비웠습니다.")


#로그추가
def append_log(message):
    global filepath
    filepath=os.path.join(base_dir,"drive_log.txt")
    with open(filepath,"a") as a:
        a.write(message+"\n")
    label.config(text=message)

#파일 지우기 - open으로 하면 후에 전역함수로 영향을 받아서 각 함수에서 지정하는 방식!
def clear_log_file():
    with open(filepath,"w") as a:
        pass
    


root=Tk()
root.title("문제4")
root.geometry("400x320")
Label(root,text="차량 이름을 입력하세요: ").pack()

e1=Entry(root)
e1.pack()

label=Label(root,text="결과가 여기에 표시됩니다.")
label.pack()

#button
frame=Frame(root)
frame.pack()
Button(frame,text="자동차 주행",command=drive_car).pack()
Button(frame,text="트럭 주행",command=drive_truck).pack()
Button(frame,text="로그 비우기",command=clear_dog).pack()


root.mainloop()