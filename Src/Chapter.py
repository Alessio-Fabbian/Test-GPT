from Src.Utils import Utils
from Src.Character.Profile import Profile
from Src.Structure import Structure

import random


class Chapter:
    def __init__(self):
        self.utils = Utils()
        self.profile = Profile()
        self.structure = Structure()

    def move_choice(self, comment: str = None, voice: list[str] = None):
        text = ("Cosa vuoi fare?\n"
                "1) Guardati attorno\n"
                "2) Vai avanti\n"
                "3) Torna indietro\n"
                "4) Esplora lo zaino\n"
                )
        print(text)
        choice = int(input())
        self.utils.check_choice(choice, self.move_choice, self.profile.default_actions, comment, voice)

        if self.check_moving_action(choice):
            self.make_step(choice)

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

    def init_blocks(self):
        dim = random.choice([24, 27, 30])
        for number in range(dim):
            var = self.structure
            var.order_block = number
            if number == 0:
                var.active = True
            self.blocks.append(var)

    def make_step(self, choice: int):
        index = self.give_block_index()
        if self.check_borders(index, choice):
            self.blocks[index].active = False
            if choice == 2:
                self.blocks[index + 1].active = True
            else:
                self.blocks[index - 1].active = True

    def give_block_index(self) -> int:
        for num, block in enumerate(self.blocks):
            if block.active:
                return num
            else:
                continue

    def check_borders(self, index: int, choice: int):
        if index == 0 and choice == 3:
            print("La strada è bloccata, non puoi tornare indietro.")
            return False

        elif index == len(self.blocks) and choice == 2:
            self.end_chapter()
            return False

        else:
            return True

    @staticmethod
    def check_moving_action(choice: int):
        if choice == 2 or choice == 3:
            return True
        else:
            return False










