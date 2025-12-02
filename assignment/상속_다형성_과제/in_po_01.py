class Car:
    def __init__(self,speed):
        self.speed=speed

    def get_speed(self):
        return f"현재속도: {self.speed}km/h"
    
class SportsCar(Car):
    def __init__(self,speed,turbo):
        super().__init__(speed)
        self.turbo=turbo

    def get_speed(self):
        #super().drive()
        if self.turbo==True:
            return f"현재속도: {self.speed}km/h (터보 ON)"
        else:
            return f"현재속도: {self.speed}km/h (터보 OFF)"
        
car1=Car(80)
print(car1.get_speed())

sport1=SportsCar(200,True)
print(sport1.get_speed())

sport2=SportsCar(100,False)
print(sport2.get_speed())
