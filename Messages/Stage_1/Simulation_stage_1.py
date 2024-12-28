from Messages.Stage_1.Forest import Forest

class Simulation1:
    def __init__(self):
        self.forest = Forest()
        self.blocks = 20

    def play_chapter_1(self):
        self.forest.chapter_1_intro()
