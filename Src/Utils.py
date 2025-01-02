from typing import Any

from Src.Character.Object import Object


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
    def init_object(box: list[Object]):
        output = []
        for element in box:
            component = element()
            output.append(component)

        return output


    @staticmethod
    def check_typing(word: str):
        word_lower = word.strip().lower()
        return word_lower.capitalize()

    @staticmethod
    def check_choice(choice: int, function, wrapper: dict[str, Any], text: str = None, voice: list[str] = None):
        if choice < 1 or choice > 4:
            print("Azione non valida. Riprova.")
            function()
        else:
            wrapper[str(choice)](text, voice)

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
