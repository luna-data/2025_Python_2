# -*- coding: utf-8 -*-
# all_basic_problems.py

import math

# ============================================
# 변형문제 1. 영화 대여 관리 프로그램
# ============================================
class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self.rented = False

    def rent(self):
        if not self.rented:
            self.rented = True
            print(f"{self.title}(이)가 대여되었습니다.")
        else:
            print(f"{self.title}(은)는 이미 대여 중입니다.")

    def return_movie(self):
        if self.rented:
            self.rented = False
            print(f"{self.title}(이)가 반납되었습니다.")
        else:
            print(f"{self.title}(은)는 대여 중이 아닙니다.")


def test_movie():
    m1 = Movie("인셉션", "놀란")
    m1.rent()
    m1.return_movie()


# ============================================
# 변형문제 2. 길이 변환기 클래스
# ============================================
class Length:
    def __init__(self, meter):
        self.meter = meter

    def to_kilometer(self):
        return self.meter / 1000


def test_length():
    l = Length(1500)
    print("미터:", l.meter)
    print("킬로미터:", l.to_kilometer())


# ============================================
# 변형문제 3. 포인트 적립 클래스
# ============================================
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.point = 0

    def add_point(self, rate):
        self.point += int(self.price * rate)

    def get_info(self):
        print(f"상품명: {self.name}, 가격: {self.price}원, 포인트: {self.point}점")


def test_item():
    i1 = Item("헤드폰", 80000)
    i1.add_point(0.05)
    i1.get_info()


# ============================================
# 변형문제 4. 프로젝트 점수 관리
# ============================================
class Project:
    def __init__(self, title):
        self.title = title
        self.scores = []

    def add_score(self, s):
        self.scores.append(s)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def info(self):
        return f"프로젝트: {self.title}, 평균 점수: {self.average()}"


def test_project():
    p = Project("데이터 분석")
    p.add_score(95)
    p.add_score(90)
    print(p.info())


# ============================================
# 변형문제 5. 자전거 이동 거리
# ============================================
class Bike:
    def __init__(self, model):
        self.model = model
        self.distance = 0

    def ride(self, km):
        self.distance += km

    def info(self):
        return f"자전거: {self.model}, 이동 거리: {self.distance}km"


def test_bike():
    b = Bike("MTB")
    b.ride(10)
    b.ride(25)
    print(b.info())


# ============================================
# 변형문제 6. 영화 플레이리스트
# ============================================
class MovieList:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def add(self, title):
        self.movies.append(title)

    def count(self):
        return len(self.movies)

    def show(self):
        movie_str = ", ".join(self.movies)
        return f"플리명: {self.name}, 개수: {self.count()}, 목록: [ {movie_str} ]"


def test_movie_list():
    ml = MovieList("Weekend")
    ml.add("인셉션")
    ml.add("인터스텔라")
    ml.add("테넷")
    print(ml.show())


# ============================================
# 변형문제 7. 시간대 변환
# ============================================
class TimeZone:
    def __init__(self, city, offset):
        self.city = city
        self.offset = offset  # UTC 기준

    def to_local(self, hour_utc):
        return (hour_utc + self.offset) % 24

    def update_offset(self, new_offset):
        self.offset = new_offset
        print(f"{self.city} 시간대가 UTC+{self.offset}로 변경되었습니다.")

    def info(self):
        print(f"도시: {self.city}, UTC+{self.offset}")


def test_timezone():
    seoul = TimeZone("서울", 9)
    seoul.info()
    print("UTC 10시는 서울에서", seoul.to_local(10), "시입니다.")
    seoul.update_offset(8)


# ============================================
# 변형문제 10. 악기 연주 (클래스)
# ============================================
class Instrument:
    def __init__(self, name):
        self.name = name

    def play(self):
        raise NotImplementedError


class Piano(Instrument):
    def play(self):
        return f"피아노 {self.name}이(가) 연주됩니다."


class Guitar(Instrument):
    def play(self):
        return f"기타 {self.name}이(가) 연주되고 있습니다."


def test_instrument():
    p = Piano("Yamaha")
    g = Guitar("Fender")
    print(p.play())
    print(g.play())


# ============================================
# 변형문제 11. Player + Weapon(has-a)
# ============================================
class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def info(self):
        return f"무기: {self.name}, 공격력: {self.power}"


class Sword(Weapon):
    pass


class Bow(Weapon):
    pass


class PlayerChar:
    def __init__(self, name, weapon=None):
        self.name = name
        self.weapon = weapon

    def set_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon is None:
            return f"{self.name}은(는) 맨손으로 공격합니다."
        return f"{self.name}의 무기 → {self.weapon.info()}"


def test_player_char():
    p = PlayerChar("홍길동")
    s = Sword("검", 10)
    b = Bow("활", 8)
    p.set_weapon(s)
    print(p.attack())
    p.set_weapon(b)
    print(p.attack())


# ============================================
# 변형문제 12. Triangle / Circle (로직)
# ============================================
class ShapeBase:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Triangle(ShapeBase):
    def __init__(self, x1, y1, x2, y2, x3, y3, color="lightgreen"):
        super().__init__(x1, y1, color)
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def area(self):
        return abs(
            (self.x1 * (self.y2 - self.y3)
             + self.x2 * (self.y3 - self.y1)
             + self.x3 * (self.y1 - self.y2)) / 2
        )

    def perimeter(self):
        def dist(xa, ya, xb, yb):
            return math.hypot(xa - xb, ya - yb)

        a = dist(self.x1, self.y1, self.x2, self.y2)
        b = dist(self.x2, self.y2, self.x3, self.y3)
        c = dist(self.x3, self.y3, self.x1, self.y1)
        return a + b + c


class Circle(ShapeBase):
    def __init__(self, x, y, r, color="skyblue"):
        super().__init__(x, y, color)
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r


def test_shapes():
    t = Triangle(0, 0, 3, 0, 0, 4)
    c = Circle(0, 0, 5)
    print("삼각형 넓이:", t.area(), "둘레:", t.perimeter())
    print("원 넓이:", c.area(), "둘레:", c.perimeter())


# ============================================
# 변형문제 13. 동아리 신청
# ============================================
class PersonBase:
    def __init__(self, name):
        self.name = name


class Student(PersonBase):
    def __init__(self, name):
        super().__init__(name)
        self.clubs = []

    def join_club(self, club):
        if club not in self.clubs:
            self.clubs.append(club)

    def clear_clubs(self):
        self.clubs.clear()

    def info(self):
        if not self.clubs:
            return f"{self.name}은(는) 신청한 동아리가 없습니다."
        return f"{self.name}이(가) 신청한 동아리: {', '.join(self.clubs)}"


def test_student_clubs():
    s = Student("홍길동")
    s.join_club("밴드부")
    s.join_club("프로그래밍동아리")
    print(s.info())
    s.clear_clubs()
    print(s.info())


# ============================================
# 변형문제 14. 차량 등록 프로그램(클래스)
# ============================================
class VehicleBase:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError


class Car(VehicleBase):
    def sound(self):
        return "부릉!"


class Motorcycle(VehicleBase):
    def sound(self):
        return "부와앙!"


class Owner:
    def __init__(self, name, vehicle=None):
        self.name = name
        self.vehicle = vehicle

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle

    def info(self, insured=False, checked=False):
        if self.vehicle is None:
            return f"{self.name}은(는) 차량이 없습니다."
        ins = "보험 가입" if insured else "보험 미가입"
        chk = "정기 점검 완료" if checked else "정기 점검 미완료"
        return f"소유자: {self.name}, 차량: {self.vehicle.name}, 소리: {self.vehicle.sound()}, {ins}, {chk}"


def test_vehicle_owner():
    o = Owner("홍길동")
    car = Car("소나타")
    o.set_vehicle(car)
    print(o.info(insured=True, checked=False))


# ============================================
# 변형문제 15. Car / ElectricCar
# ============================================
class CarSimple:
    def __init__(self, speed):
        self.speed = speed

    def get_speed(self):
        return f"현재 속도: {self.speed}km/h"


class ElectricCar(CarSimple):
    def __init__(self, speed, mode):
        super().__init__(speed)
        self.mode = mode

    def get_speed(self):
        if self.mode == "eco":
            return "현재 속도: 80km/h (ECO 모드)"
        elif self.mode == "sport":
            return "현재 속도: 160km/h (SPORT 모드)"
        return super().get_speed()


def test_electric_car():
    c = CarSimple(90)
    print(c.get_speed())
    e1 = ElectricCar(120, "eco")
    e2 = ElectricCar(120, "sport")
    print(e1.get_speed())
    print(e2.get_speed())


# ============================================
# 변형문제 16. Worker 다형성
# ============================================
class Worker:
    def work(self):
        raise NotImplementedError


class OfficeWorker(Worker):
    def work(self):
        return "사무직 직원이 업무를 시작합니다."


class FactoryWorker(Worker):
    def work(self):
        return "공장 직원이 기계를 가동합니다."


def test_workers():
    workers = [OfficeWorker(), FactoryWorker(), OfficeWorker()]
    for w in workers:
        print(w.work())


# ============================================
# 변형문제 17. Animal / Turtle
# ============================================
class AnimalBase:
    def move(self):
        return "동물이 움직입니다."


class Turtle(AnimalBase):
    def move(self):
        return "거북이는 천천히 기어갑니다."


def test_turtle():
    a = AnimalBase()
    t = Turtle()
    print(a.move())
    print(t.move())


# ============================================
# 변형문제 18. Device / Tablet
# ============================================
class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price  # 만 원 단위라고 가정

    def get_info(self):
        return f"브랜드: {self.brand}, 가격: {self.price}만 원"


class Tablet(Device):
    def __init__(self, brand, price, size):
        super().__init__(brand, price)
        self.size = size

    def get_info(self):
        return f"브랜드: {self.brand}, 가격: {self.price}만 원, 화면 크기: {self.size}인치"


def test_device():
    d = Device("삼성", 100)
    t = Tablet("애플", 120, 11)
    print(d.get_info())
    print(t.get_info())


# ============================================
# 변형문제 19. Drink / ColdDrink / Order
# ============================================
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"메뉴: {self.name}, 가격: {self.price}원"


class ColdDrink(Drink):
    def __init__(self, name, price, ice_level):
        super().__init__(name, price)
        self.ice_level = ice_level

    def __str__(self):
        return f"메뉴: {self.name}, 가격: {self.price}원(얼음: {self.ice_level})"


class DrinkOrder:
    def __init__(self):
        self.items = []

    def add_drink(self, drink):
        self.items.append(drink)

    def show_order(self):
        for d in self.items:
            print(str(d))


def test_drink_order():
    d1 = Drink("아메리카노", 3000)
    d2 = ColdDrink("아이스라테", 4500, "많이")
    order = DrinkOrder()
    order.add_drink(d1)
    order.add_drink(d2)
    order.show_order()


# ============================================
# 변형문제 22. 학생 목록 읽기
# ============================================
def read_students_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


# ============================================
# 변형문제 23. 단어 빈도 세기
# ============================================
def count_word_in_file(filename, word):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        count = text.count(word)
        print(f"'{word}' 단어가 {count}번 등장합니다.")
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


# ============================================
# 변형문제 24. 로그 병합
# ============================================
def merge_logs(file1, file2, out_file):
    try:
        with open(out_file, "w", encoding="utf-8") as out:
            for fname in (file1, file2):
                with open(fname, "r", encoding="utf-8") as f:
                    for line in f:
                        out.write(line)
        print("로그 병합이 완료되었습니다.")
    except FileNotFoundError as e:
        print("파일을 찾을 수 없습니다:", e.filename)


# ============================================
# 변형문제 25. Train / KTX / Mugunghwa + 파일 로그
# ============================================
class Train:
    def __init__(self, name):
        self.name = name

    def run(self):
        raise NotImplementedError


class KTX(Train):
    def run(self):
        return f"KTX {self.name} 열차가 고속으로 달립니다."


class Mugunghwa(Train):
    def run(self):
        return f"무궁화 {self.name} 열차가 천천히 출발합니다."


def append_log_train(message, filename="train_log.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def clear_log_file_train(filename="train_log.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        pass


def test_train_log():
    t1 = KTX("001")
    msg = t1.run()
    print(msg)
    append_log_train(msg)


# ============================================
# 변형문제 26. 숫자·알파벳 개수 세기(로직)
# ============================================
def count_stats_digits_alpha(filename):
    digit_cnt = 0
    alpha_cnt = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for ch in line:
                if ch.isdigit():
                    digit_cnt += 1
                if ch.isalpha():
                    alpha_cnt += 1
    return digit_cnt, alpha_cnt


# ============================================
# 테스트용 메인
# ============================================
if __name__ == "__main__":
    test_movie()
    test_length()
    test_item()
    test_project()
    test_bike()
    test_movie_list()
    test_timezone()
    test_instrument()
    test_player_char()
    test_shapes()
    test_student_clubs()
    test_vehicle_owner()
    test_electric_car()
    test_workers()
    test_turtle()
    test_device()
    test_drink_order()
    test_train_log()
