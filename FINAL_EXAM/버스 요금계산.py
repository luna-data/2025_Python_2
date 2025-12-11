# vehicle_fare.py

class Vehicle:
    def __init__(self, name: str, base_fare: int):
        self.name = name
        self.base_fare = base_fare

    def fare(self, distance: float) -> int:
        """자식 클래스에서 반드시 오버라이딩"""
        raise NotImplementedError("fare()는 자식 클래스에서 구현해야 합니다.")

    def info(self) -> str:
        return f"수단: {self.name}, 기본요금: {self.base_fare}원"


class Bus(Vehicle):  # Bus is-a Vehicle
    def __init__(self, name: str, base_fare: int, capacity: int):
        super().__init__(name, base_fare)
        self.capacity = capacity

    def fare(self, distance: float) -> int:
        # 기본요금 + 거리당 100원
        return int(self.base_fare + distance * 100)


class Taxi(Vehicle):  # Taxi is-a Vehicle
    def __init__(self, name: str, base_fare: int, night_surcharge: float):
        super().__init__(name, base_fare)
        self.night_surcharge = night_surcharge  # 0.2 → 20%

    def fare(self, distance: float, night: bool = False) -> int:
        base = self.base_fare + distance * 500
        if night:
            base *= (1 + self.night_surcharge)
        return int(base)


class Truck(Vehicle):  # Truck is-a Vehicle
    def __init__(self, name: str, base_fare: int, load_weight: float):
        super().__init__(name, base_fare)
        self.load_weight = load_weight  # ton

    def fare(self, distance: float) -> int:
        # 적재 중량과 거리에 비례
        return int(self.base_fare + distance * self.load_weight * 200)


# ===== 테스트 코드 =====
if __name__ == "__main__":
    bus = Bus("시내버스1", 1200, capacity=40)
    taxi = Taxi("개인택시35", 3800, night_surcharge=0.3)
    truck = Truck("화물트럭", 5000, load_weight=2.5)

    vehicles: list[Vehicle] = [bus, taxi, truck]

    distance = 10  # km

    for v in vehicles:
        if isinstance(v, Taxi):
            fare_day = v.fare(distance, night=False)
            fare_night = v.fare(distance, night=True)
            print(f"{v.info()} → {distance}km 주간 요금: {fare_day}원, 야간 요금: {fare_night}원")
        else:
            fare_val = v.fare(distance)
            print(f"{v.info()} → {distance}km 요금: {fare_val}원")
