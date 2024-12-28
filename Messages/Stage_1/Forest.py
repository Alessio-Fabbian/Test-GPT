import random

from Messages.Stage_1.Animals import Animals
from Messages.Chapter import Chapter


class Forest(Chapter):
    def __init__(self):
        self.season = random.choice(["Estate", "Inverno"])
        self.weather = random.choice(["Sereno", "Nuvoloso", "Piovoso", "Nevoso"])
        self.daytime = random.choice(["Giorno", "Notte"])
        self.animals = Animals()
        self.objects = ["Ramo", "Sasso", "Foglia"]

        if self.season == "Estate":
            self.animals = self.animals.bear
        else:
            self.animals = self.animals.wolfs


