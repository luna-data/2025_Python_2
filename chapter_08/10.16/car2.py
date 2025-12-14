class Car:
    def __init__(self,speed=0, gear=1, color="white"):
        self.__speed=speed
        self.__gear=gear
        self.__color=color

    def setSpeed(self,speed):
        self.__speed=speed

    def setGear(self,gear):
        self.__gear=gear

    def setColor(self,color):
        self.__color=color

myCar=Car()
myCar.setGear(3)
myCar.setSpeed(100)

print(myCar)

print("속도:",myCar._Car__speed)
print("기어:",myCar._Car__gear)
print("색상:",myCar._Car__color)