class Room:
    def __init__(self, room_type, area):
        self.room_type = room_type
        self.area = area


class House:
    def __init__(self, address):  # House has Rooms
        self.address = address
        self.rooms = []  # Room 리스트
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def get_total_area(self):
        total = 0
        for room in self.rooms:
            total += room.area
        return total
    
house = House("서울시 도봉구")

room1 = Room("거실", 20.5)
room2 = Room("침실", 15.0)
room3 = Room("주방", 10.0)

house.add_room(room1)
house.add_room(room2)
house.add_room(room3)
total_area = house.get_total_area()
print(f"집 주소: {house.address}")
print(f"총 면적: {total_area} 제곱미터")
