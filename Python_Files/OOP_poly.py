import random


class Character():
    def __init__(self, atk, Hp):
        self.atk = atk
        self.Hp = Hp
        
        
    def attack(self):
        pass

class Swordman(Character):
    
    def attack(self):
        damage = random.uniform(float(self.atk/2), float(self.atk))
        print(f"Swordman Attacked: Damage [{damage:.2f}]")

class Mage(Character):
    
    def attack(self):
        damage = random.uniform(float(self.atk/2), float(self.atk))
        print(f"Mage Attacked: Damage [{damage:.2f}]")

class Archer(Character):
    
    def attack(self):
        damage = random.uniform(float(self.atk/2), float(self.atk))
        print(f"Archer Attacked: Damage [{damage:.2f}]")

ch1 = Archer(23, 50)
ch2 = Swordman(25, 60)
ch3 = Mage(30, 45)



char_list = [ch1, ch2, ch3] 
while True:
    for char in char_list:
        
    