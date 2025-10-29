class Employee:
    empCount=0
    def __init__(self, name, salary):
        Employee.empCount+=1
        self.name=name
        self.salary=salary

    def displayEmp(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
    
emp1=Employee("Kim", 5000)
emp2=Employee("Lee", 6000)

emp1.displayEmp()
emp2.displayEmp()

print("Total emplyees:", Employee.empCount)