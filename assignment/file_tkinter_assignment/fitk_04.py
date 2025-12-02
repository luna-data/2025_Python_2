from tkinter import *
#상속구조
class Vehicle:
    def __init__(self,e1):
        self.name=e1.get()
    def drive(self):
        NotImplementedError

class Car(Vehicle):

    def drive(self):
        label.config=f"승용차 {e1.get()}가 주행합니다."

class Truck(Vehicle):
    def drive(self):                
        label.config=f"트럭 {e1.get()}가 화물을 싣고 주행합니다."

root=Tk()
root.title("문제4")
root.geometry("400x320")
Label(root,text="차량 이름을 입력하세요: ").pack()

e1=Entry(root).pack()


label=Label(text="결과가 여기에 표시됩니다.",text=())
