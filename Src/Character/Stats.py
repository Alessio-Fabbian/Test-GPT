import random
from Src.Character.Bag import Bag
from Src.Utils import Utils


class Stats:
    def __init__(self, utils: Utils):
        self.name = ""
        self.energy = random.choice([4, 5, 6])
        self.power = random.choice([3, 4, 5])
        self.eye = True
        self.n_of_lifes = 3
        self.bag = Bag(utils)

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

    def change_props(self, props: str, is_increase: bool):
        wrapper = {
            "energy": self.energy,
            "power": self.power
        }

        if is_increase:
            wrapper[props] = wrapper[props] + 1
        else:
            if self.check_en_limits():
                wrapper[props] = wrapper[props] - 1
            else:
                print(f"La tua {props} è gia al minimo.")

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


