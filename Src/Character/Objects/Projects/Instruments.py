from Src.Character.Objects.Projects.Project import Project


class Fire(Project):
    def __init__(self):
        super().__init__()
        self.title = "Fuoco"
        self.needed = ["Rami", "Accendino"]
        self.property = "Serve per cucinare il cibo ed allontanare gli animali."


class Shield(Project):
    def __init__(self):
        super().__init__()
        self.title = "Scudo"
        self.needed = ["Rami", "Laccio"]
        self.property = "Serve per difendersi dagli attacchi."
