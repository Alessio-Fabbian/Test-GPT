from Src.Utils import Utils


class Bag:
    def __init__(self):
        self.size = 10
        self.items = ["Panino", "Acqua", "Cellulare_scarico"]

    def add(self, item: str):
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
                object_to_remove = str(input())
                self.swap_objects(object_to_remove, item)
            else:
                print("Va bene, l'oggetto verrà riposto a terra.")

    def swap_objects(self, object_to_remove: str, item: str):
        self.items.remove(object_to_remove)
        self.items.append(item)
        print(f"{object_to_remove} è stato scambiato con {item}.\n")
        print(f"{object_to_remove} è stato lasciato a terra.")

    def show_items(self):
        print("Ecco il contenuto del tuo zaino:")
        print(self.items)

    def check_item(self, item: str):
        if item in self.items:
            return True
        else:
            return False

