class Shape:
    def __init__(self,width,height):
        self.width=width
        self.height=height

class Triangle(Shape):
    def area(self):
        return self.width*self.height*0.5
    
tri=Triangle(4,6)
print(f"삼각형의 밑변: {tri.width}")
print(f"삼각형의 높이: {tri.height}")
print(f"삼각형의 넓이: {tri.area()}")