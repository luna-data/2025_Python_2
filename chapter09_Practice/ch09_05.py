class Employee:
    empCount=0 #클래스 변수 사용하는 부분
    def __init__(self, name, salary):
        Employee.empCount+=1 #클래스변수 값 변경 : 클래스 변수 지정 시 정해진 형식에 따라야함
        self.name=name
        self.salary=salary

    def displayEmp(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

#Employee 객체 생성
emp1 = Employee("Kim", 5000)
emp2 = Employee("Lee", 6000)

#직원 정보 출력
emp1.displayEmp()
emp2.displayEmp()

#전체 직원 수 출력
print("Total employees:", Employee.empCount)