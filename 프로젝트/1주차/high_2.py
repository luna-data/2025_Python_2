class Student:
    def __init__(self,name,scores):
        self.name=name
        self.scholarship_standard=90
        self.scores=scores

    def get_average(self):
        if len(self.scores)==0:
            return 0
        return sum(self.scores)/len(self.scores)
    
    def is_scholarship(self):
        if self.get_average()>=self.scholarship_standard:
            return True
        else:
            return False

    def info(self):
        avg=self.get_average()
        print(f"이름: {self.name}, 평균 점수: {avg:.2f}")
    

stu1 = Student("홍길동", [85, 90, 88])
stu2 = Student("이영희", [95, 94, 97])
stu3 = Student("정민수", [92, 90, 89])
stu4 = Student("김철수", [70, 75, 80])

students = [stu1, stu2, stu3, stu4]
scholarship_students = []


for s in students:
    s.info()
    if s.is_scholarship():
        scholarship_students.append(s.name)
print("장학생 명단:", scholarship_students)