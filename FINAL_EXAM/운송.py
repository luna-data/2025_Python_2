# transport_manager.py
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

LOG_FILE = "transport_log.txt"


# ================== 클래스 정의 ==================
class Vehicle:
    def __init__(self, name, base_fare):
        self.name = name
        self.base_fare = base_fare

    def drive(self, distance):
        raise NotImplementedError

    def calculate_fare(self, distance, **kwargs):
        raise NotImplementedError

    def __str__(self):
        return f"차량: {self.name}, 기본요금: {self.base_fare}원"


class Bus(Vehicle):
    def __init__(self, name, base_fare, capacity):
        super().__init__(name, base_fare)
        self.capacity = capacity

    def drive(self, distance):
        return f"버스 {self.name}이(가) {distance}km 운행합니다."

    def calculate_fare(self, distance, **kwargs):
        per_km = 300
        return self.base_fare + per_km * distance


class Taxi(Vehicle):
    def __init__(self, name, base_fare, night_surcharge):
        super().__init__(name, base_fare)
        self.night_surcharge = night_surcharge  # 0.2 = 20%

    def drive(self, distance):
        return f"택시 {self.name}이(가) {distance}km 손님을 태우고 이동합니다."

    def calculate_fare(self, distance, night=False, **kwargs):
        per_km = 800
        fare = self.base_fare + per_km * distance
        if night:
            fare = int(fare * (1 + self.night_surcharge))
        return fare


class Truck(Vehicle):
    def __init__(self, name, base_fare, load_weight):
        super().__init__(name, base_fare)
        self.load_weight = load_weight  # ton

    def drive(self, distance):
        return f"트럭 {self.name}이(가) {self.load_weight}톤을 싣고 {distance}km 운행합니다."

    def calculate_fare(self, distance, **kwargs):
        per_km_per_ton = 500
        return self.base_fare + int(per_km_per_ton * self.load_weight * distance)


# ================== 로그 함수 ==================
def log_trip(vehicle_type, name, distance, fare, filename=LOG_FILE):
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{date_str},{vehicle_type},{name},{distance},{fare}"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    return line


def load_logs(filename=LOG_FILE):
    logs = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                logs.append(line)
    except FileNotFoundError:
        pass
    return logs


def parse_log(line):
    # date,type,name,distance,fare
    parts = line.split(",")
    if len(parts) != 5:
        return None
    date, vtype, name, distance, fare = parts
    return {
        "date": date,
        "type": vtype,
        "name": name,
        "distance": float(distance),
        "fare": int(fare),
        "raw": line
    }


def filter_logs_by_type(logs, vehicle_type):
    result = []
    for line in logs:
        obj = parse_log(line)
        if obj and obj["type"] == vehicle_type:
            result.append(obj)
    return result


def calculate_total_revenue(logs):
    total = 0
    for line in logs:
        obj = parse_log(line)
        if obj:
            total += obj["fare"]
    return total


# ================== GUI ==================
def main():
    root = Tk()
    root.title("운송수단 운행·요금 관리")
    root.geometry("720x420")

    # 상단 입력 영역
    frame_top = Frame(root, padx=10, pady=10)
    frame_top.pack(fill="x")

    Label(frame_top, text="차종").grid(row=0, column=0, sticky="e")
    vehicle_var = StringVar(value="Bus")
    combo_type = ttk.Combobox(frame_top, textvariable=vehicle_var,
                              values=["Bus", "Taxi", "Truck"], width=10, state="readonly")
    combo_type.grid(row=0, column=1, padx=5)

    Label(frame_top, text="차량 이름/번호").grid(row=0, column=2, sticky="e")
    entry_name = Entry(frame_top, width=10)
    entry_name.grid(row=0, column=3, padx=5)
    entry_name.insert(0, "001")

    Label(frame_top, text="기본요금").grid(row=0, column=4, sticky="e")
    entry_base = Entry(frame_top, width=8)
    entry_base.grid(row=0, column=5, padx=5)
    entry_base.insert(0, "2000")

    Label(frame_top, text="거리(km)").grid(row=1, column=0, sticky="e", pady=5)
    entry_distance = Entry(frame_top, width=10)
    entry_distance.grid(row=1, column=1, padx=5, pady=5)
    entry_distance.insert(0, "10")

    # 추가 옵션
    Label(frame_top, text="정원(Bus) / 적재톤(Truck)").grid(row=1, column=2, sticky="e")
    entry_extra = Entry(frame_top, width=10)
    entry_extra.grid(row=1, column=3, padx=5)
    entry_extra.insert(0, "40")

    Label(frame_top, text="야간할증(Taxi, 0.2=20%)").grid(row=1, column=4, sticky="e")
    entry_night_rate = Entry(frame_top, width=8)
    entry_night_rate.grid(row=1, column=5, padx=5)
    entry_night_rate.insert(0, "0.2")

    night_var = BooleanVar()
    check_night = Checkbutton(frame_top, text="야간 운행(Taxi)", variable=night_var)
    check_night.grid(row=2, column=0, columnspan=2, sticky="w", pady=5)

    # 중앙 버튼 / 결과
    frame_mid = Frame(root, padx=10, pady=5)
    frame_mid.pack(fill="x")

    text_result = Text(frame_mid, height=5)
    text_result.pack(side="bottom", fill="x", pady=5)

    def print_result(msg):
        text_result.insert(END, msg + "\n")
        text_result.see(END)

    def add_trip():
        vtype = vehicle_var.get()
        name = entry_name.get().strip() or "이름없음"
        try:
            base = int(entry_base.get())
            distance = float(entry_distance.get())
        except ValueError:
            messagebox.showerror("입력 오류", "기본요금과 거리는 숫자로 입력하세요.")
            return

        extra = entry_extra.get().strip()
        night_rate_str = entry_night_rate.get().strip()

        vehicle = None
        try:
            if vtype == "Bus":
                cap = int(extra) if extra else 40
                vehicle = Bus(name, base, cap)
                msg = vehicle.drive(distance)
                fare = vehicle.calculate_fare(distance)
            elif vtype == "Taxi":
                night_rate = float(night_rate_str) if night_rate_str else 0.0
                vehicle = Taxi(name, base, night_rate)
                msg = vehicle.drive(distance)
                fare = vehicle.calculate_fare(distance, night=night_var.get())
            elif vtype == "Truck":
                load_weight = float(extra) if extra else 5.0
                vehicle = Truck(name, base, load_weight)
                msg = vehicle.drive(distance)
                fare = vehicle.calculate_fare(distance)
            else:
                messagebox.showerror("오류", "알 수 없는 차종입니다.")
                return
        except ValueError:
            messagebox.showerror("입력 오류", "추가 옵션(정원/톤/할증)은 숫자로 입력하세요.")
            return

        log_line = log_trip(vtype, name, distance, fare)
        print_result(f"[운행] {msg}  → 요금: {fare}원")
        print_result(f"[로그] {log_line}")

    def show_all_logs():
        text_result.delete("1.0", END)
        logs = load_logs()
        if not logs:
            print_result("기록이 없습니다.")
            return
        print_result("=== 전체 운행 로그 ===")
        for line in logs:
            print_result(line)

    def filter_by_type():
        vtype = vehicle_var.get()
        logs = load_logs()
        objs = filter_logs_by_type(logs, vtype)
        text_result.delete("1.0", END)
        if not objs:
            print_result(f"{vtype} 로그가 없습니다.")
            return
        print_result(f"=== {vtype} 로그 ===")
        for obj in objs:
            print_result(obj["raw"])

    def show_total_revenue():
        logs = load_logs()
        total = calculate_total_revenue(logs)
        print_result(f"=== 총 매출액: {total}원 ===")

    btn_frame = Frame(frame_mid)
    btn_frame.pack(side="top", fill="x")

    Button(btn_frame, text="운행 기록 추가", command=add_trip).pack(side="left", padx=5)
    Button(btn_frame, text="전체 로그 보기", command=show_all_logs).pack(side="left", padx=5)
    Button(btn_frame, text="차종별 필터", command=filter_by_type).pack(side="left", padx=5)
    Button(btn_frame, text="총 매출 계산", command=show_total_revenue).pack(side="left", padx=5)

    root.mainloop()


if __name__ == "__main__":
    main()
