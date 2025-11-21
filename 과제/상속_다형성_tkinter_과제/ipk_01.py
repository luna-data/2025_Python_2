from tkinter import *

class Vehicle:
    def __init__(self,name):
        self.name=name

    def drive(self):
        pass
        
class Car(Vehicle):
    def __init__(self,name):
        super().__init__(name)

    def drive(self):
        return f"승용차 {self.name}가 주행합니다."
    
class Truck(Vehicle):
    def __init__(self,name):
        super().__init__(name)
    
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."


root=Tk()
root.title("문제1")
root.geometry('400x300')
Label(root,text="버튼을 눌러보세요.",font=("맑은 고딕", 10)).pack()

car=Car('car1')
truck=Truck('truck1')
#StringVar -> 
#msg = StringVar()

def car_text():
    text1=car.drive()
    label1.config(text=text1)

def truck_text():
    text1=truck.drive()
    label1.config(text=text1)

frame=Frame(root)
frame.pack(pady=10)
Button(frame,text="자동차 주행",command=car_text).grid(row=0, column=0, padx=10, pady=5)
Button(frame,text="트럭 주행",command=truck_text).grid(row=0, column=1, padx=10, pady=5)

label1=Label(root,text='',font=("맑은 고딕", 10))
label1.pack()

root.mainloop()
