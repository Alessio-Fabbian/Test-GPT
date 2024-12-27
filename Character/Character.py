import random
from Bag import Bag

class Stats:
    def __init__(self):
        self.name = ""
        self.energy = random.choice([3,4,5])
        self.power = random.choice([3,4,5])
        self.n_of_lifes = 3
        self.bag = Bag()

    def set_init(self, name: str):
        self.name = name

