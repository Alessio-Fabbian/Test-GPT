from Utils import Utils

class Chapter:
    def __init__(self):
        self.utils = Utils()
        self.stats =

    def move_choice(self, voice: str = None):
        text = ("Cosa vuoi fare?\n"
                "1) Guardati attorno\n"
                "2) Vai avanti\n"
                "3) Torna indietro\n"
                "4) Esplora lo zaino\n"
                )
        print(text)
        choice = int(input())
        self.check_choice(choice, self.move_choice)


    def check_choice(self, choice: int, function):
        if choice < 1 or choice > 4:
            print("Azione non valida. Riprova.")
            return function()
        else:
            self.action_wrapper(choice)

    def action_wrapper(self, choice: int):
        actions_list = {"1": self.look_around,
                   "2": self.go_on,
                   "3": self.go_back,
                   "4": self.see_bag}

        action = actions_list[str(choice)]
        action()


    def look_around(self, text: str = None, objects: list[str] = None):
        print("Ti stai guardando attorno.\n")
        if text is not None:
            print(text)
        if objects is not None:
            print("Ci sono degli oggetti a terra:\n"
                  f"{objects}"
                  f"Vuoi raccoglierne uno? (S/N)")
            response = str(input())
            if self.utils.check_sn_answer(response, self.look_around):


        else:
            print("Non sembra esserci nulla di interessante.")


    def go_on(self):


    def go_back(self):


    def see_bag(self):
        print("Ecco il contenuto della tua borsa:")
        print()






