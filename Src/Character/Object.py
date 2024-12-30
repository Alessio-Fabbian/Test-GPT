

class Object:
    def __init__(self):
        self.name = ""
        self.food = False
        self.usable = False
        self.weapon = False

    def is_food(self, it_is: bool):
        self.food = it_is

    def is_usable(self, it_is: bool):
        self.usable = it_is

    def is_weapon(self, it_is: bool):
        self.weapon = it_is


class Weapon(Object):
    def __init__(self):
        super().__init__()
        self.power = 0
        self.long_range = False

        self.is_weapon(True)

    def set_power(self, power: int):
        self.power = power

    def is_long_range(self, it_is: bool):
        self.long_range = it_is


class Usable(Object):
    def __init__(self):
        super().__init__()
        self.function = ""
        self.is_usable(True)

    def give_function(self, text: str):
        self.function = text


class Food(Object):
    def __init__(self):
        super().__init__()
        self.energy = 0

        self.is_food(True)

    def set_energy(self, energy: int):
        self.energy = energy