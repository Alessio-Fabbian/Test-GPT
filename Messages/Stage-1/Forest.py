from Messages import Utils
from Animals import Animals
import json

class Forest:
    def __init__(self):
        self.daytime = ""
        self.weather = ""
        self.animals = Animals()

    def init_day(self):
        day_data = json.load(open("daytime.json"))
        if day_data:
