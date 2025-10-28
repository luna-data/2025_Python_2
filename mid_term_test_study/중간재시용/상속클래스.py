# 1) Person
class Person:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} <{self.email}>"


# 2) Student (Person 상속)
class Student(Person):
    def __init__(self, stu_id: str, name: str, major: str, email: str):
        super().__init__(name, email)
        self.stu_id = stu_id
        self.major = major

    def __eq__(self, other):
        return isinstance(other, Student) and (self.stu_id == other.stu_id)

    # 읽기 전용: 게터만 제공 (데코레이터 금지)
    def get_year(self) -> int:
        return int(self.stu_id[:4])


# 3) Course
class Course:
    def __init__(self, code: str, title: str, credit: int):
        self.code = code
        self.title = title
        self.credit = credit
        if not (1 <= self.credit <= 3):
            raise ValueError("credit는 1~3 정수여야 합니다.")


# 4) Enrollment
class Enrollment:
    def __init__(self, student: Student, course: Course, score: int):
        if not (0 <= score <= 100):
            raise ValueError("score는 0~100 범위여야 합니다.")
        self.student = student
        self.course = course
        self.score = score

    def grade(self) -> str:
        s = self.score
        if s >= 90: return "A"
        if s >= 80: return "B"
        if s >= 70: return "C"
        if s >= 60: return "D"
        return "F"


# 6) 다형성: 등급 정책
class GradePolicy:
    # 인터페이스 개념: 하위 클래스가 구현
    def points(self, letter: str) -> float:
        raise NotImplementedError


class LetterPolicy(GradePolicy):
    def __init__(self):
        self.map = {"A": 4.5, "B": 3.5, "C": 2.5, "D": 1.5, "F": 0.0}

    def points(self, letter: str) -> float:
        return self.map.get(letter, 0.0)


# 5) Transcript
class Transcript:
    def __init__(self, student: Student):
        self.student = student
        self.items = []  # type: list[Enrollment]

    def add(self, enrollment: Enrollment):
        code = enrollment.course.code
        # 같은 코드 제거 후 최신 삽입
        self.items = [e for e in self.items if e.course.code != code]
        self.items.append(enrollment)

    def gpa(self, policy: GradePolicy) -> float:
        total_pts = 0.0
        total_cred = 0
        for e in self.items:
            gp = policy.points(e.grade())
            total_pts += gp * e.course.credit
            total_cred += e.course.credit
        return round(total_pts / total_cred, 2) if total_cred > 0 else 0.0

    def __lt__(self, other):
        if not isinstance(other, Transcript):
            return NotImplemented
        # 기본 정책으로 비교(필요시 외부에서 같은 정책 주입)
        return self.gpa(LetterPolicy()) < other.gpa(LetterPolicy())


# 7) 일반 함수(데코레이터/정규식 없이)
def is_valid_course_code(code: str) -> bool:
    # "대문자 2~4 + 숫자 3" 패턴을 수작업 검사
    if len(code) < 5:
        return False
    # 앞에서부터 대문자 연속 구간 길이 확인
    i = 0
    while i < len(code) and 'A' <= code[i] <= 'Z':
        i += 1
    letters = i
    digits = len(code) - i
    if not (2 <= letters <= 4):
        return False
    if digits != 3:
        return False
    # 남은 3글자가 모두 숫자인지 확인
    for ch in code[i:]:
        if not ('0' <= ch <= '9'):
            return False
    return True


def parse_student_from_email(email: str) -> Student:
    """
    형식: 'stu{stu_id}@duksung.ac.kr'
    - stu_id: 숫자만
    - name: 로컬파트 전체
    - major: 'Undeclared'
    정규식 없이 수작업 파싱
    """
    parts = email.split("@")
    if len(parts) != 2:
        raise ValueError("이메일 형식 오류")
    local, domain = parts
    if domain != "duksung.ac.kr":
        raise ValueError("도메인 오류")
    if not local.startswith("stu"):
        raise ValueError("로컬파트 형식 오류")
    stu_id = local[3:]
    if not (len(stu_id) > 0 and stu_id.isdigit()):
        raise ValueError("stu_id 형식 오류")
    name = local
    return Student(stu_id=stu_id, name=name, major="Undeclared", email=email)


# ---- 간단 실행 예시 ----
if __name__ == "__main__":
    # Student 생성 & 읽기 전용 year은 게터로만 접근
    s1 = Student("2025012", "Kim Minsu", "DS", "minsu@duksung.ac.kr")
    print(s1.get_year())  # 2025

    # 과목/검증
    print(is_valid_course_code("DS101"))    # True
    print(is_valid_course_code("MATH201"))  # True
    print(is_valid_course_code("Cs10"))     # False

    c1 = Course("DS101", "Intro to DS", 3)
    e1 = Enrollment(s1, c1, 92)

    tr = Transcript(s1)
    tr.add(e1)

    policy = LetterPolicy()
    print(tr.gpa(policy))  # 4.5
