class Temperature:
    def __init__(self, celsius):
        self.celsius=celsius

    def to_fahrenheit(self):
        return self.celsius*1.8+32
    
t=Temperature(25)
print("섭씨:",t.celsius)
print("화씨:",t.to_fahrenheit())