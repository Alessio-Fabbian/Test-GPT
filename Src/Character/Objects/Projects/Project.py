from Src.Character.Object import Object


class Project(Object):
    def __init__(self):
        super().__init__()


    def show_needs(self):
        print(f"Ecco il necessario per realizzare {self.title}: \n")
        print(self.needed)
