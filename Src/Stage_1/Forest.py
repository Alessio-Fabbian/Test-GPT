from Src.Stage_1.Animals import Animals
from Src.Chapter import Chapter
from Src.Weather import Weather
from Src.Character.Objects.Items import Log, Lighter


class Forest(Chapter):
    def __init__(self):
        super().__init__()
        self.animals = Animals()
        self.weather = Weather()
        self.ob_list = [Log, Lighter]
        self.objects = self.utils.init_object(self.ob_list)
        self.unlockable = ["Fungo", "Vegetali", "Accendino", "Occhiali", "Laccio", "Vaso"]
        self.blocks = []

        if self.weather.season == "Estate":
            self.animals = self.animals.bear
            #self.unlockable.append("Frutto")
        else:
            self.animals = self.animals.wolfs
            #self.objects.append("Neve")

        self.init_blocks()




