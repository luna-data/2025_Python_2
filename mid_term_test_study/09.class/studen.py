class Student:
    def __init__(self, name, id):
        self.name=name
        self.id=id

    def getname(self):
        return self.name
    
    def getid(self):
        return self.id
    
best=Student("Lee",101)
print(best.getname())
print(best.getid())