import random

from Messages import Utils
from Animals import Animals
from ..Chapter import Chapter


class Forest(Chapter):
    def __init__(self):
        self.season = random.choice(["Estate", "Inverno"])
        self.weather = random.choice(["Sereno", "Nuvoloso", "Piovoso", "Nevoso"])
        self.daytime = random.choice(["Giorno", "Notte"])
        self.animals = Animals()

        if self.season == "Estate":
            self.animals = self.animals.bear
        else:
            self.animals = self.animals.wolfs

    def chapter_1_intro(self):
        text = ("La tua avventura inizia in una foresta. \n"
                f"E' {self.season}, il cielo è {self.weather}. E' {self.daytime}.\n"
                f"Ti trovi su un sentiero, ma non ti ricordi più la direzione di casa.\n"
                f"Gli unici oggetti che hai con te sono un celluare scarico, un panino ed una bottiglia d'acqua.\n"
                f"(Si trovano tutti all'interno del tuo zaino. Nel tuo zaino c'è posto ancora per 7 oggetti)"
                f""
                f"Guardati attorno e cerca un modo per uscire da questa foresta!"
                f"Ma fai attenzioni ai pericoli che potresti incontrare...")
        print(text)

