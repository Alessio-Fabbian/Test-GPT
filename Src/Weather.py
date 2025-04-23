import random


class Weather:
    def __init__(self):
        self._seasons = ["Estate", "Inverno"]
        self._weathers = ["Sereno", "Nuvoloso", "Piovoso", "Nevoso"]
        self._daytimes = ["Giorno", "Notte"]

        self.season = random.choice(self._seasons)
        self.weather = random.choice(self._weathers)
        self.daytime = random.choice(self._daytimes)

    def change_daytime(self):
        actual = self.daytime
        new_daytime = [day for day in self._daytimes if day != actual]
        self.daytime = new_daytime[0]
        print(f"Siamo passati da {actual} a {self.daytime}")

    def change_weather(self):
        actual = self.weather
        new_weather = [day for day in self._weather if day != actual]
        self.weather = new_weather[0]
        print(f"Il clima è passato da {actual} a {self.weather}")

