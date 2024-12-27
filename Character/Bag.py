from Messages.Utils import Utils


class Bag:
    def __init__(self):
        self.size = 10
        self.items = []

    def add(self, item):
        if len(self.items) < self.size:
            self.items.append(item)
            print("L'oggetto è stato aggiunto alla borsa.")
        else:
            print("La tua borsa è piena.\n"
                  "Vuoi eliminare un oggetto per far posto a questo? (S/N)")
            response = input()
            utils = Utils()
            if utils.check_sn_answer(response, self.add):
                print("Quale oggetto vuoi eliminare?\n")
                print(self.items)
                object_to_remove = input()
                self.swap_objects(object_to_remove, item)
            else:
                print("Va bene, l'oggetto verrà riposto a terra.")

    def swap_objects(self, object_to_remove: str, item: str):
        self.items.remove(object_to_remove)
        self.items.append(item)
        print(f"{object_to_remove} è stato scambiato con {item}.")

    def show_items(self):
        print(self.items)