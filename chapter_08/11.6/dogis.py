class Animal:
    def speak(self):
        print('동물이 소리를 냅니다.')

class Dog(Animal):
    def speak(self):
        print("멍멍!") #상속받아서,. 받아서 사용하는겨
    
dog=Dog()
dog.speak()  