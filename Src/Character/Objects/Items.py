from Src.Character.Object import Object


class Log(Object):
    def __init__(self):
        super().__init__()
        self.set_name("Rami")
        self.is_weapon(True)
        self.set_power(3)
        self.is_usable(True)
        self.give_property("Può essere usato sia come arma che per costruire qualche oggetto.")


class Phone(Object):
    def __init__(self):
        super().__init__()
        self.set_name("Telefono")
        self.is_usable(True)
        self.give_property("Può essere usato per chiamare aiuto, oppure smontato per usarne la batteria.")
        self.has_battery = True
        self.battery = self.Battery()
        self.charge = self.battery.charge_level
        self.connection = False

    def check_charge(self):
        if self.charge == "Scarico":
            return False
        else:
            return True

    def remove_battery(self):
        if not self.has_battery:
            self.charge = ""

    def reach_connection(self):
        self.connection = True

    def try_to_call(self):
        if self.check_charge():
            if self.connection:
                print("Stai chiamando i soccorsi.")
            else:
                print("Non c'è connessione, non si riesce a telefonare.")
        else:
            print("La batteria è troppo scarica per telefonare.")

    class Battery:
        def __init__(self):
            self.charge_level = "Scarico"

        def charge(self):
            self.charge_level = "Carico"


class Sandwhich(Object):
    def __init__(self):
        super().__init__()
        self.set_name("Panino")
        self.is_food(True)
        self.set_energy(3)
        self.is_usable(True)
        self.give_property("Può essere usato come cibo, oppure come esca/distrazione per gli animali.")


class Lighter(Object):
    def __init__(self):
        super().__init__()
        self.set_name("Accendino")
        self.is_usable(True)
        self.give_property("Può essere usato per creare il Fuoco, da cui le Torcie.")