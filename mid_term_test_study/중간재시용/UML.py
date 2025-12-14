class Person:
    def __init__(self,name,height, age, weight):
        self.name=name
        self.height=height
        self.age=age
        self.weight=weight
    def show_info(self):
        print(f"이름:{self.name}, 키:{self.height}, 나이:{self.age}, 몸무게:{self.weight}")

class Student(Person):
    def __init__(self,name,height,age,weight,stu_id,score,grade):
        super().__init__(name,height,age,weight)
        self.stu_id=stu_id
        self.score=score
        self.grade=grade
    def show_student_info(self):
        self.show_info()
        print(f"학번:{self.stu_id}, 학점:{self.score}, 학년:{self.grade}")

class Teacher(Person):
    def __init__(self,name,height,age,weight,teach_id,wage,year):
        super().__init__(name,height,age,weight)
        self.teach_id=teach_id
        self.wage=wage
        self.year=year
    def show_teacher_info(self):
        self.show_info()
        print(f"교직원번호:{self.teach_id}, 월금:{self.wage}, 년차{self.year}")


stu1=Student("홍길동",170,20,60,"2023001","A+",2)
stu1.show_student_info()

tea1=Teacher("김선생",175, 40, 70, "T1001",300,10)
tea1.show_teacher_info()