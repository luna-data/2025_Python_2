class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "멍멍"
    
class Cat(Animal):
    def make_sound (self):
        return "야옹"
    
dog=Dog()
cat=Cat()

print(f"강아지 소리: {dog.make_sound()}")
print(f"고양이 소리: {cat.make_sound()}")