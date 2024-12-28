from Messages import Introduction
from Messages.Stage_1.Forest import Forest

def start_game():

    mexxages = Introduction.Introduction()

    mexxages.start_game()

    mexxages.intro()

    chapter1 = Forest()

    chapter1.chapter_1_intro()


if __name__ == "__main__":
    start_game()
