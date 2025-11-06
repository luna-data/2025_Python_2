import math

class Shape:
    def calculate_area():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    
    def calculate_area(self):
        return math.pi*self.radius**2
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def calculate_area(self):
        return self.width*self.height
    
def total_area(shapes):
    total=0
    for s in shapes:
        total +=s.calculate_area()

    return total

c=Circle(5)
r=Rectangle(4,6)

print(f"Circle의 면적: {c.calculate_area():.2f}")
print(f"Rectangle의 면적: {r.calculate_area():.2f}")
print(f"도형들의 총 넓이: {total_area([c,r]):.2f}")