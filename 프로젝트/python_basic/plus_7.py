class ElectronicDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def power_on(self):
        return f"{self.brand} {self.model} 전원이 켜졌습니다."


class Smartphone(ElectronicDevice):  # Smartphone is an ElectronicDevice
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size


class Laptop(ElectronicDevice):  # Laptop is an ElectronicDevice
    def __init__(self, brand, model, ram_size):
        super().__init__(brand, model)
        self.ram_size = ram_size

phone1 = Smartphone("삼성", "S24", 6.5)
laptop1 = Laptop("LG", "Gram", 16)

print(phone1.power_on())
print(laptop1.power_on())

print("스마트폰 화면 크기:", phone1.screen_size)
print("노트북 RAM:", laptop1.ram_size, "GB")