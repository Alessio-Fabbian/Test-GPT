

class Object:
    def __init__(self):
        self.food = False
        self.usable = False
        self.weapon = False
        self.name = ""
        self.property = ""
        self.power = 0
        self.energy = 0

    def set_name(self, name: str):
        self.name = name

    def is_food(self, it_is: bool):
        self.food = it_is

    def is_usable(self, it_is: bool):
        self.usable = it_is

    def is_weapon(self, it_is: bool):
        self.weapon = it_is

    def set_power(self, power: int):
        self.power = power

    def set_energy(self, energy: int):
        self.energy = energy

    def give_property(self, text: str):
        self.property = text

