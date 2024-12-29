import random
from Src.Character.Bag import Bag
from Src.Utils import Utils


class Stats:
    def __init__(self):
        self.name = ""
        self.energy = random.choice([4, 5, 6])
        self.power = random.choice([3, 4, 5])
        self.eye = True
        self.n_of_lifes = 3
        self.bag = Bag()

    def set_init(self, name: str):
        self.name = name

    def change_n_lifes(self, is_increase: bool):
        if is_increase:
            self.n_of_lifes = self.n_of_lifes + 1
        else:
            self.n_of_lifes = self.n_of_lifes - 1

        self.check_lifes()

    def check_lifes(self):
        if self.n_of_lifes == 0:
            utils = Utils()
            utils.end_game_lifes()
        else:
            print(f"Ti sono rimaste {self.n_of_lifes} vite.")

    def change_property(self, property: str, is_increase: bool):
        if property == "energy":
            if is_increase:
                self.energy = self.energy + 1
            else:
                if self.check_en_limits():
                    self.energy = self.energy - 1
                else:
                    print("La tua energia è gia al minimo.")
        else:
            if is_increase:
                self.power = self.power + 1
            else:
                if self.check_po_limits():
                    self.power = self.power - 1
                else:
                    print("La tua forza è gia al minimo.")

    def check_en_limits(self) -> bool:
        if self.energy < 1:
            return False
        else:
            return True

    def check_po_limits(self) -> bool:
        if self.power < 1:
            return False
        else:
            return True


