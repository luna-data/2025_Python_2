from tkinter import *
import tkinter.messagebox as msgbox
import os

# ==============================
# 1. Vehicle 계층 (is-a 관계)
# ==============================

class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self, distance):
        # 자식 클래스에서 반드시 오버라이딩
        raise NotImplementedError("자식 클래스에서 drive()를 구현해야 합니다.")


class Car(Vehicle):
    def drive(self, distance):
        return f"승용차 {self.name}이(가) {distance}km 주행합니다."


class Truck(Vehicle):
    def __init__(self, name, load_weight):
        super().__init__(name)
        self.load_weight = load_weight  # 톤 단위

    def drive(self, distance):
        return f"트럭 {self.name}이(가) {self.load_weight}톤을 싣고 {distance}km 운행합니다."


class Bus(Vehicle):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity  # 정원

    def drive(self, distance):
        return f"버스 {self.name}이(가) 승객 {self.capacity}명을 태우고 {distance}km 운행합니다."


# ==============================
# 2. 파일 로그 관련 함수
# ==============================

LOG_FILE = "vehicle_log.txt"

def append_log(message):
    """운행 메시지를 로그 파일에 한 줄 추가"""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except Exception as e:
        msgbox.showerror("파일 오류", f"로그 파일에 기록하는 중 오류가 발생했습니다.\n{e}")

def read_last_logs(n=5):
    """로그 파일에서 마지막 n줄을 리스트로 반환"""
    if not os.path.exists(LOG_FILE):
        return ["로그 파일이 없습니다."]

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines[-n:] if len(lines) > n else lines
    except Exception as e:
        msgbox.showerror("파일 오류", f"로그 파일을 읽는 중 오류가 발생했습니다.\n{e}")
        return []


# ==============================
# 3. Tkinter 이벤트 함수들
# ==============================

def run_vehicle():
    """운행 버튼 클릭 시 호출되는 함수"""
    # 입력값 읽기
    name = entry_name.get().strip()
    dist_text = entry_distance.get().strip()
    load_text = entry_load.get().strip()
    cap_text = entry_capacity.get().strip()

    if name == "":
        name = "이름없음"

    if dist_text == "":
        msgbox.showwarning("입력 오류", "운행 거리를 입력하세요.")
        return

    # 거리 숫자 변환
    try:
        distance = float(dist_text)
        if distance <= 0:
            raise ValueError
    except ValueError:
        msgbox.showwarning("입력 오류", "운행 거리는 0보다 큰 숫자로 입력하세요.")
        return

    vehicle_type = vehicle_var.get()  # "car", "truck", "bus"

    # 차량 객체 생성
    vehicle = None

    if vehicle_type == "car":
        vehicle = Car(name)

    elif vehicle_type == "truck":
        # 적재 중량 필요
        if load_text == "":
            msgbox.showwarning("입력 오류", "트럭의 적재 중량(톤)을 입력하세요.")
            return
        try:
            load_weight = float(load_text)
            if load_weight <= 0:
                raise ValueError
        except ValueError:
            msgbox.showwarning("입력 오류", "적재 중량은 0보다 큰 숫자로 입력하세요.")
            return
        vehicle = Truck(name, load_weight)

    elif vehicle_type == "bus":
        # 정원 필요
        if cap_text == "":
            msgbox.showwarning("입력 오류", "버스의 정원(명)을 입력하세요.")
            return
        try:
            capacity = int(cap_text)
            if capacity <= 0:
                raise ValueError
        except ValueError:
            msgbox.showwarning("입력 오류", "정원은 0보다 큰 정수로 입력하세요.")
            return
        vehicle = Bus(name, capacity)

    else:
        msgbox.showwarning("선택 오류", "차량 종류를 선택하세요.")
        return

    # 다형성: 어떤 객체든 drive()만 호출
    message = vehicle.drive(distance)

    # 라벨에 표시
    label_result.config(text=message)

    # 로그 파일에 기록
    append_log(message)


def show_last_logs():
    """최근 로그 5개 보기 버튼"""
    logs = read_last_logs(5)
    text_logs.delete("1.0", END)
    for line in logs:
        text_logs.insert(END, line + "\n")


# ==============================
# 4. Tkinter GUI 구성 (root 부분)
# ==============================

root = Tk()
root.title("차량 운행 기록 시스템")
root.geometry("520x420")

# --- 상단 입력 영역 ---
frame_top = Frame(root)
frame_top.pack(pady=10)

Label(frame_top, text="차량 이름:").grid(row=0, column=0, padx=5, pady=3, sticky="e")
entry_name = Entry(frame_top, width=15)
entry_name.grid(row=0, column=1, padx=5, pady=3)

Label(frame_top, text="운행 거리(km):").grid(row=1, column=0, padx=5, pady=3, sticky="e")
entry_distance = Entry(frame_top, width=15)
entry_distance.grid(row=1, column=1, padx=5, pady=3)

Label(frame_top, text="적재 중량(톤, Truck):").grid(row=2, column=0, padx=5, pady=3, sticky="e")
entry_load = Entry(frame_top, width=15)
entry_load.grid(row=2, column=1, padx=5, pady=3)

Label(frame_top, text="정원(명, Bus):").grid(row=3, column=0, padx=5, pady=3, sticky="e")
entry_capacity = Entry(frame_top, width=15)
entry_capacity.grid(row=3, column=1, padx=5, pady=3)

# --- 차량 종류 선택 (Radiobutton) ---
frame_radio = Frame(root)
frame_radio.pack(pady=5)

vehicle_var = StringVar(value="car")  # 기본값 Car

Label(frame_radio, text="차량 종류:").pack(side="left", padx=5)
Radiobutton(frame_radio, text="Car", value="car", variable=vehicle_var).pack(side="left", padx=5)
Radiobutton(frame_radio, text="Truck", value="truck", variable=vehicle_var).pack(side="left", padx=5)
Radiobutton(frame_radio, text="Bus", value="bus", variable=vehicle_var).pack(side="left", padx=5)

# --- 버튼 영역 ---
frame_btn = Frame(root)
frame_btn.pack(pady=5)

Button(frame_btn, text="운행", width=12, command=run_vehicle).pack(side="left", padx=5)
Button(frame_btn, text="최근 로그 5개 보기", width=18, command=show_last_logs).pack(side="left", padx=5)

# --- 결과 라벨 ---
label_result = Label(root, text="운행 결과가 여기에 표시됩니다.", fg="blue")
label_result.pack(pady=10)

# --- 로그 표시 Text ---
Label(root, text="[최근 운행 로그]").pack()
text_logs = Text(root, width=60, height=10)
text_logs.pack(padx=10, pady=5)

root.mainloop()
