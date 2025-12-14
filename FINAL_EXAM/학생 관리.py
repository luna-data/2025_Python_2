# student_enrollment.py

class Person:
    def __init__(self, name: str):
        self.name = name

    def info(self) -> str:
        return f"이름: {self.name}"


class Student(Person):  # Student is-a Person
    def __init__(self, name: str, student_id: str, major: str):
        super().__init__(name)
        self.student_id = student_id
        self.major = major

    def info(self) -> str:  # 오버라이딩
        return f"이름: {self.name}, 학번: {self.student_id}, 전공: {self.major}"


class Course:
    def __init__(self, name: str, credit: int):
        self.name = name
        self.credit = credit

    def __str__(self) -> str:
        return f"{self.name}({self.credit}학점)"


class Enrollment:   # Enrollment has-a Student, has-a Course 리스트
    def __init__(self, student: Student):
        self.student = student
        self.courses: list[Course] = []

    def add_course(self, course: Course):
        self.courses.append(course)

    def total_credit(self) -> int:
        return sum(c.credit for c in self.courses)

    def summary(self) -> str:
        course_str = ", ".join(str(c) for c in self.courses) if self.courses else "없음"
        total = self.total_credit()
        lines = [
            f"학생: {self.student.name}({self.student.student_id})",
            f"수강 과목: {course_str}",
            f"총 학점: {total}",
        ]
        return "\n".join(lines)


# ===== 테스트 코드 =====
if __name__ == "__main__":
    s = Student("홍길동", "2025001", "데이터사이언스")
    e = Enrollment(s)
    e.add_course(Course("파이썬 프로그래밍", 3))
    e.add_course(Course("데이터베이스", 3))
    print(e.summary())
