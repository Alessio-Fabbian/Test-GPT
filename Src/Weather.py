import random


class Weather:
    def __init__(self):
        self.season = random.choice(["Estate", "Inverno"])
        self.weather = random.choice(["Sereno", "Nuvoloso", "Piovoso", "Nevoso"])
        self.daytime = random.choice(["Giorno", "Notte"])