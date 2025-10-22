#376page
class Circle:
    def __init__(self, radius):
        self.radius=radius

    def __eq__(self,other):
        return self.radius==other.radius
    
c1=Circle(10)
c2=Circle(10)
if c1==c2:
    print("원의 반지름은 동일합니다.")