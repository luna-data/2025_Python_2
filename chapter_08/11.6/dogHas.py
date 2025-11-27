class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog:
    def __init__(self):
        #super().__init__(인스턴스 변수들), 그런데 여기서 해즈어 관계는 애니멀을 가집니다
        self.animal=Animal()

    def speak(self):
        self.animal.speak() #animal이라는 객체의 스피크를 가져와 사용할거야,
        print('멍멍!') #가져와서 사용하는개념, 클래스가 별개임

dog=Dog()
dog.speak()