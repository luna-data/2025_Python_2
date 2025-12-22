# 문제 3: 컴퓨터와 부품
class CPU:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed


class RAM:
    def __init__(self, size, type):
        self.size = size
        self.type = type


class HardDrive:
    def __init__(self, capacity, type):
        self.capacity = capacity
        self.type = type


class Computer:
    def __init__(self, cpu, ram, hard_drive):  # Computer has CPU, RAM, HardDrive
        self.cpu = cpu  # CPU 객체
        self.ram = ram  # RAM 객체
        self.hard_drive = hard_drive  # HardDrive 객체
    
    def get_specs(self):
        return (f"CPU: {self.cpu.model} ({self.cpu.speed}GHz), "
                f"RAM: {self.ram.size}GB ({self.ram.type}), "
                f"HDD: {self.hard_drive.capacity}GB ({self.hard_drive.type})")

# 부품 객체 생성
cpu1 = CPU("Intel i7-9700K", 3.6)
ram1 = RAM(16, "DDR4")
hdd1 = HardDrive(512, "SSD")

# 컴퓨터 객체 생성 (HAS-A 관계)
com1 = Computer(cpu1, ram1, hdd1)

# 사양 출력
print(com1.get_specs())