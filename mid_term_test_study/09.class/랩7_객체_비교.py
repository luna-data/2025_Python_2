class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __lt__(self,other):
        return self.age<other.age
    
s1=Student("Kim",20)
s2=Student("Lee",22)

print(s1<s2)
print(s2<s1)