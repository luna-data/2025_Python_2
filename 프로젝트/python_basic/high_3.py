class Student:
    def __init__(self, name, student_id,major):
        self.name = name
        self.student_id = student_id
        self.major = major  
    def introduce(self):
        print(f"안녕하세요, {self.major} {self.student_id} {self.name}입니다.")

s1 = Student("홍길동", "2024001", "경영학과")
s2 = Student("김영희", "2024002", "컴퓨터공학과")
s1.introduce()
s2.introduce()
