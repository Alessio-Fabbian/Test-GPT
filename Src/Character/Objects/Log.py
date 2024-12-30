from Src.Character.Object import Weapon, Usable, Food


class Log(Weapon, Usable):
    def __init__(self):
        super().__init__()

        self.is_long_range(False)
        self.set_power(2)



class Sandwich(Food, Usable):
    def __init__(self):
        super().__init__()

        self.set_energy(1)
        self.give_function("Può essere usato per allontanare/avvicinare gli animali.")

