import random
class Animal:
    live = True
    sound = None # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, _cords, speed ):
        self._coords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self._coords[0] = self.dx * self.speed
        self._coords[1] = self.dy * self.speed
        self._coords[2] = self.dz * self.speed
        if self._coords[2] < 0:
            print("It's too deep, i can't dive :(" )

    def get_cords(self):
        print(f"X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER <  5:
            print (f"Sorry, i'm peaceful :)")
        else:
            print(f"Be careful, i'm attacking you 0_0")

class Bird(Animal):
    import random
    beak = True  #наличие клюва
    def lay_eggs(self):
        print("Here are(is)", random.randint(1,4), "eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3.
    def dive_in(self, dz):
        self.dz = dz
        self._coords[2]  = round(self._coords[2] + ( - abs((self.dz * self.speed)/2)))

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"  # звук, который издаёт утконос


db = Duckbill([0,0,0],10)

print(db.live)
print(db.beak)

print(db.sound)
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()