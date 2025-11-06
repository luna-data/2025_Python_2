class Animal(object):
    pass

class Dog(Animal):
    def __init__(self,name):
        self.name=name

class Person(object):
    def __init__(self,name):
        self.name=name
        self.pet=None #미리 지정하지 않았는데 왜 사용가능함? => 파이썬은 유연하게 사용가능함, 나중에 사용할 수있음

dog1=Dog("dog1")
person1=Person("홍길동")
person1.pet=dog1