from Src.Character.Object import Object
from Src.Character.Objects.Projects.Project import Project
from Src.Utils import Utils
from Src.Character.Objects.Items import Sandwhich, Phone, Lighter
from Src.Character.Objects.Projects.Instruments import Fire, Shield, Torch


class Bag:
    def __init__(self):
        self.size = 10
        self.utils = Utils()
        self.items = self.utils.init_object([Sandwhich, Phone, Lighter])
        self.pro_list = [Fire, Shield, Torch]
        self.actions = {
            "1": self.show_items,
            "2": self.property_check,
            "3": self.build,
            "4": self.see_projects
        }
        self.projects_open = self.utils.init_object(self.pro_list)

    def add(self, item: str, objects: list[Object]):
        if len(self.items) < self.size:
            for element in objects:
                if element.name == item:
                    self.items.append(element)
            print(f"L'oggetto {item} è stato aggiunto alla borsa.")
        else:
            print("La tua borsa è piena.\n"
                  "Vuoi eliminare un oggetto per far posto a questo? (S/N)")
            response = input()
            if self.utils.check_sn_answer(response, self.add):
                print("Quale oggetto vuoi eliminare?\n")
                self.show_items()
                object_to_remove = str(input())
                self.swap_objects(object_to_remove, item, objects)
            else:
                print(f"Va bene, {item} verrà riposto a terra.")

    def swap_objects(self, object_to_remove: str, item: str, objects: list[Object]):
        to_remove = self.from_name_to_object(object_to_remove, self.items)
        to_insert = self.from_name_to_object(item, objects)
        self.items.remove(to_remove)
        self.items.append(to_insert)
        print(f"{object_to_remove} è stato scambiato con {item}.\n")
        print(f"{object_to_remove} è stato lasciato a terra.")

    def show_items(self, text: str = None, objects: list[str] = None):
        print("Ecco il contenuto del tuo zaino:")
        for element in self.items:
            print(f'- {element.name}')

    def property_check(self, text: str = None, objects: list[str] = None):
        print("Ecco le proprietà dei tuoi oggetti:.\n")
        for element in self.items:
            print(f'- {element.name}:\n'
                  f'{element.property}\n')

    def build(self, text: str = None, objects: list[str] = None):
        print("Che progetto voi costruire?\n")
        for element in self.projects_open:
            print(f'{element.title}')

        response = str(input())
        titles = [element.title for element in self.projects_open]

        if response in titles:
            proj = [element for element in self.projects_open if response == element.title]
            needs = proj[0].needed

            check_list = []
            for item in needs:
                if not self.is_in_bag(item):
                    print(f"Non hai tutti gli oggetti necessari per la costruzione di {response}.")
                    check_list.append(False)
                else:
                    check_list.append(True)

            if all(check_list):
                print(f"L'oggetto {response} è stato costruito.")
                self.items = [item for item in self.items if item.name not in needs]
                self.items.append(proj[0])
        else:
            print(f"Non esiste il progetto {response}")
            self.build()

    def see_projects(self, text: str = None, objects: list[str] = None):
        print("Ecco gli oggetti che puoi costruire: \n")
        for element in self.projects_open:
            print(f"- {element.title}")
            print(f"Necessario: {element.needed}")
            print(f"{element.property}\n")

    def is_in_bag(self, item: str):
        name = self.utils.check_typing(item)
        for element in self.items:
            if element.name == name:
                return True
            else:
                continue

        return False

    def from_name_to_object(self, name: str, box: list[Object]) -> Object:
        name = self.utils.check_typing(name)
        for element in box:
            if element.name == name:
                return element
            else:
                continue

    @staticmethod
    def proj_wrapper(project: str) -> Project:
        wrap = {
            "Fuoco": Fire,
            "Scudo": Shield
        }

        return wrap[project]
