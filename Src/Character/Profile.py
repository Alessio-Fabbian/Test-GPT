from Src.Character.Stats import Stats
from Src.Character.Actions import Actions


class Profile:
    def __init__(self):
        self.stats = Stats()
        self.actions = Actions()

    def eat(self, food: str):
        energy_increase = self.actions.eat_some(food)
        self.stats.energy = self.stats.energy + energy_increase

    def drink(self, beverage: str):
        energy_increase = self.actions.drink_some(beverage)
        self.stats.energy = self.stats.energy + energy_increase

    def use(self, object: str):
        if self.stats.bag.check_item(object):
            self.actions.use_object(object)
        else:
            print(f"Non hai {object} all'interno dello zaino.")

