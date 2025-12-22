class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
    def attack(self):
        return 0


class Warrior(Character):  # Warrior is a Character
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength
    
    def attack(self):
        return self.strength * 2


class Mage(Character):  # Mage is a Character
    def __init__(self, name, hp, magic_power):
        super().__init__(name, hp)
        self.magic_power = magic_power
    
    def attack(self):
        return self.magic_power * 3


warrior1 = Warrior("강한 전사", 120, 30)
mage1 = Mage("지혜로운 마법사", 90, 25)

print(f"{warrior1.name} 공격력: {warrior1.attack()}")
print(f"{mage1.name} 공격력: {mage1.attack()}")
