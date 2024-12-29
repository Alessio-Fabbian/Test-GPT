from Src.Stage_1.Animals import Animals
from Src.Chapter import Chapter
from Src.Weather import Weather


class Forest(Chapter):
    def __init__(self):
        super().__init__()
        self.animals = Animals()
        self.weather = Weather()
        self.objects = ["Ramo", "Sasso", "Foglie"]
        self.unlockable = ["Fungo", "Vegetali", "Accendino", "Occhiali", "Laccio", "Vaso"]

        if self.weather.season == "Estate":
            self.animals = self.animals.bear
            self.unlockable.append("Frutto")
        else:
            self.animals = self.animals.wolfs
            self.objects.append("Neve")




