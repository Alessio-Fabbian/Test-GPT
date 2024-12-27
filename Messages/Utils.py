
class Utils:

    @staticmethod
    def check_sn_answer(answer: str, function=None):
        answer = answer.strip().lower()
        if answer == "si":
            return True
        elif answer == "no":
            return False
        else:
            print("Non hai dato una risposta valida. Riprova, grazie.")
            return function()

    @staticmethod
    def end_game():
        text = ("Mi dispiace, ma qualcosa è andato storto. \n"
                "Riavvia il programma per iniziare nuovamente la partita.")
        print(text)