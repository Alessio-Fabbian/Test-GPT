import random


class Animals:

    def __init__(self):
        self.bear = self.Bear()
        self.wolfs = self.Wolfs()

    class Bear:
        def __init__(self):
            self.power = 8
            self.energy = 5

    class Wolfs:
        def __init__(self):
            self.power = 4
            self.energy = 8
            self.n_of_elements = random.choice([4, 5, 6, 7])

