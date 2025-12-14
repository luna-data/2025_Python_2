class Student:
    def __init__(self,name=None,age=0):
        self.__name=name
        self.setAge(age)

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    
    def setName(self,name):
        self.__name=name
    def setAge(self,age):
        if age<0:
            self.__age=0
        else:
            self.__age=age

#객체생성
s1=Student("Hong",20)
print(f"{s1.getName()} 학생의 나이는 {s1.getAge()}살입니다.")
s1.setAge(-5)
print(f"{s1.getName()} 학생의 나이는 {s1.getAge()}살입니다.")
s1.setAge(25)
print(f"{s1.getName()} 학생의 나이는 {s1.getAge()}살입니다.")