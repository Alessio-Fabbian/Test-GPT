from Src.Utils import Utils
from Src.Character.Profile import Profile

import random

class Chapter:
    def __init__(self):
        self.utils = Utils()
        self.profile = Profile()

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
            function()
        else:
            self.action_wrapper(choice)

    def action_wrapper(self, choice: int):
        action = self.profile.actions.default_actions[str(choice)]
        return action()

    def unlock_item(self, item: str = None):
        if item is not None:
            if item in self.unlockable:
                self.objects.append(item)
        else:
            self.objects.append(random.choice(self.unlockable))

    def lock_item(self, item: str):
        if not self.profile.stats.eye:
            self.objects.pop(item)
        else:
            pass




    # def unlock_action(self):









