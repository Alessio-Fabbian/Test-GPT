


class Utils:
    def check_sn_answer(self, answer: str, function=None):
        answer = answer.strip().lower()
        if answer == "si":
            return True
        elif answer == "no":
            return False
        else:
            print("Non hai dato una risposta valida.")
            if function is not None:
                return function()
            else:
                self.end_game_corrupted()

    @staticmethod
    def end_game_corrupted():
        text = ("Mi dispiace, ma qualcosa è andato storto. \n"
                "Riavvia il programma per iniziare nuovamente la partita.")
        print(text)
        exit()

    @staticmethod
    def end_game_lifes():
        text = ("Mi dispiace, ma hai perso tutte le tue vite. \n"
                "Riavvia il programma per iniziare nuovamente la partita!")
        print(text)
        exit()
