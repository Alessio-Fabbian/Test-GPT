from Src import Introduction
from Src.Stage_1.Simulation_stage_1 import Simulation1


def start_game():

    mexxages = Introduction.Introduction()

    mexxages.start_game()

    mexxages.intro()

    chapter1 = Simulation1()

    chapter1.play_chapter_1()


if __name__ == "__main__":
    start_game()
