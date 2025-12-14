# ================================
# 문제 1: IS-A + 클래스 변수 + 다형성
#---------✅ 문제 요구사항 (IS-A 중심)
#---------Animal(부모)
#---------클래스 변수 total_animals = 0
#---------name, species
#---------생성될 때마다 total_animals 1 증가
#---------speak() → 오버라이딩 전용
#---------info() → "이름: 초코 (종: 개)" 형식
#---------자식 클래스 (is-a 관계)
#---------Dog → speak(): “멍멍!”
#---------Cat → speak(): “야옹!”
#---------Bird → speak(): “짹짹!”
#---------리스트에 여러 동물 저장 후 다형성 적용
#---------모든 speak() 한 번씩 호출하기
#---------클래스 변수로 총 몇 마리 생성됐는지 출력
# ================================

class Animal:
    total_animals = 0   # ★ 클래스 변수

    def __init__(self, name, species):
        self.name = name
        self.species = species
        Animal.total_animals += 1   # 객체 생성될 때 증가

    def speak(self):
        return "..."

    def info(self):
        return f"이름: {self.name} (종: {self.species})"


# -------- 자식 클래스 (IS-A 관계) --------
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "개")

    def speak(self):
        return "멍멍!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "고양이")

    def speak(self):
        return "야옹!"


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, "새")

    def speak(self):
        return "짹짹!"


# ------- 테스트 (다형성 + 리스트) -------
animals = [
    Dog("초코"),
    Dog("보리"),
    Cat("나비"),
    Bird("파랑"),
]

print("=== 동물 소리 출력(다형성) ===")
for a in animals:
    print(f"{a.info()} → {a.speak()}")

print("\n전체 생성된 동물 수:", Animal.total_animals)
