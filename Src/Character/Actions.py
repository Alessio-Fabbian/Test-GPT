from Src.Utils import Utils


class Actions:
    def __init__(self):
        self.utils = Utils()
        self.unlock = {
            "build": self.build_something,
            "attack": self.attack,
            "run_away": self.run_away,
            "interact": self.interact
        }


    @staticmethod
    def eat_some(food: str) -> int:
        eatable_food = {"Panino": 2, "Vegetali": 1, "Carne": 3}
        if food in eatable_food:
            return eatable_food[food]
        else:
            print(f"{food} non è commestibile.")
            return 0

    @staticmethod
    def drink_some(beverage: str) -> int:
        eatable_beverage = {"Acqua": 1, "Powerade": 3, "The": 2}
        if beverage in eatable_beverage:
            return eatable_beverage[beverage]
        else:
            print(f"{beverage} non è potabile.")
            return 0


    def go_on(self):
        pass


    def go_back(self):
        pass


    def see_bag(self):
        print("Cosa vuoi vedere?\n")
        text = (
                "1) Guarda il contenuto della borsa\n"
                "2) Controlla le proprietà di un oggetto\n"
                "3) Usa un oggetto\n"
                "4) Vedi lista dei progetti\n"
                "5) Chiudi la borsa\n"
                )
        print(text)
        response = int(input())
        return response

    def use_object(self, object: str):
        pass

    def new_action_number(self, new_one: str) -> int:
        if new_one in self.unlock.keys():
            return self.new_wrapper(new_one)

    @staticmethod
    def new_wrapper(new_one: str) -> int:
        list = {
            "build": 5,
            "attack": 6,
            "run_away": 7,
            "interact": 8
        }

        if new_one in list.keys():
            return list[new_one]

    def remove_action(self, number: int = None):
        if number is not None:
            self.default_actions.pop(str(number))
        else:
            for key in self.default_actions.keys():
                if int(key) > 4:
                    self.default_actions.pop(key)

    def build_something(self):
        pass

    def attack(self):
        pass

    def run_away(self):
        pass

    def interact(self):
        pass

