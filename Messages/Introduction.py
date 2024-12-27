import Character
import Utils


class Introduction:
    def __init__(self):
        self.character = Character.Stats()
        self.utils = Utils.Utils()

    def start_game(self):
        text = "Ciao, benvenuto in questa avventura.\n Come ti chiami?"
        print(text)
        name = str(input())
        self.character.set_init(name)

    def intro(self):
        text = (f"Ciao, {self.character.name}. Sei pronto ad iniziare questa avventura? \n"
                f"Stai per intraprendere un viaggio attraverso terre ignote, in cui il tuo \n"
                f"intelletto e il tuo ingegno verranno messi a dura prova. \n"
                f"Quando comparirà il simbolo (SI/NO) significa che dovrai rispondere SI/NO \n"
                f"per poter continuare. \n"
                f"Sei pronto? (S/N) ")
        print(text)
        response = str(input())
        if self.utils.check_sn_answer(response, self.intro):
            self.rules()
        else:
            self.end_game()

    def rules(self):
        text = ("Bene! Adesso ti spiego le regole del gioco:\n"
                "A schermo comparirà del testo con cui dovrai interagire rispondendo a tastiera.\n"
                "Cerca di rispondere sempre in minuscolo, per evitare problemi di lettura.\n"
                ""
                "Il tuo personaggio avrà 3 vite, alla fine delle quali il gioco si interromperà. \n"
                "Cerca indizi, raccogli oggetti, interagisci coi i personaggi... \n"
                "Il tuo obiettivo è riuscire a salvarti! \n"
                "Sei pronto per iniziare? (S/N)")
        print(text)
        response = str(input())
        if self.utils.check_sn_answer(response, self.rules):
            textb = "Ottimo! Buona Fortuna!"
            print(textb)

        else:
            self.end_game()

    @staticmethod
    def end_game():
        text = ("Mi dispiace, ma qualcosa è andato storto. \n"
                "Riavvia il programma per iniziare nuovamente la partita.")
        print(text)



