class Classroom:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity


class School:
    def __init__(self, name):  # School has Classrooms
        self.name = name
        self.classrooms = []  # Classroom 리스트를 속성으로 가짐
    
    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

school = School("덕성여자대학교")

class1 = Classroom("101호", 30)
class2 = Classroom("102호", 35)
class3 = Classroom("103호", 25)

school.add_classroom(class1)
school.add_classroom(class2)
school.add_classroom(class3)

print(f"{school.name}의 교실 목록:")
for room in school.classrooms:
    print(f"- {room.room_number}, 수용 인원: {room.capacity}명")