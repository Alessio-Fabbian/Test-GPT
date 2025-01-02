from Src.Character.Stats import Stats
from Src.Character.Actions import Actions
from Src.Utils import Utils
from Src.Character.Object import Object


class Profile:
    def __init__(self):
        self.stats = Stats()
        self.actions = Actions()
        self.utils = Utils()

        self.default_actions = {
            "1": self.look_around,
            "2": self.eat,
            "3": self.eat,
            "4": self.open_bag
        }

    def eat(self, food: str):
        energy_increase = self.actions.eat_some(food)
        self.stats.energy = self.stats.energy + energy_increase
        print(f"La tua energia è aumentata di +{energy_increase}.")

    def drink(self, beverage: str):
        energy_increase = self.actions.drink_some(beverage)
        self.stats.energy = self.stats.energy + energy_increase
        print(f"La tua energia è aumentata di +{energy_increase}.")

    def use(self, object: str):
        if self.stats.bag.is_in_bag(object):
            self.actions.use_object(object)
        else:
            print(f"Non hai {object} all'interno dello zaino.")

    def open_bag(self, text: str = None, objects: list[str] = None):
        print("Hai aperto la tua borsa.\n")
        while True:
            response = self.actions.see_bag()
            if response == 5:
                print("Hai chiuso la borsa.\n")
                break
            else:
                self.utils.check_choice(response, self.open_bag, self.stats.bag.actions)

    def unlock_action(self, new_one: str):
        number = self.actions.new_action_number(new_one)
        self.default_actions[str(number)] = self.actions.unlock[new_one]

    def look_around(self, text: str = None, objects: list[Object] = None):
        print("Ti stai guardando attorno.\n")
        if text is not None:
            print(text)
        if objects is not None:
            print("Ci sono degli oggetti a terra:\n")
            for element in objects:
                print(f"{element.name} - ")
            print("\n")
            print(f"Vuoi raccoglierne uno? (S/N)")
            response = str(input())
            if self.utils.check_sn_answer(response, self.look_around):
                self.pick_up(text, objects)
            else:
                print("Ok, nessun oggetto raccolto.")
        else:
            print("Non sembra esserci nulla di interessante.")

    def pick_up(self, text: str = None, objects: list[Object] = None):
        print("Che oggetto vuoi raccogliere?\n")
        response = str(input())
        for element in objects:
            if response == element.name:
                if not self.stats.bag.is_in_bag(response):
                    self.stats.bag.add(response, objects)
                else:
                    print(f"L'oggetto {response} si trova già nel tuo zaino.")
            else:
                print(f"L'oggetto {response} non esiste, riprova.")
                self.pick_up(objects)

    # @property
    # def bag(self):
    #     return self.stats.bag


