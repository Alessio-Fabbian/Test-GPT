from Messages.Stage_1.Forest import Forest
from Messages.Utils import Utils


class Simulation1:
    def __init__(self):
        self.forest = Forest()
        self.utils = Utils()
        self.end_index = 20
        self.counter = 0
        self.animal_crossing = False

    def play_chapter_1(self):
        self.chapter_1_intro()

        while self.counter < 3:
            self.forest.move_choice()
            self.increase_counter()

        self.animal_shows()



    def chapter_1_intro(self):
        text = ("La tua avventura inizia in una foresta. \n"
                f"E' {self.forest.season}, il cielo è {self.forest.weather}. E' {self.forest.daytime}.\n"
                f"Ti trovi su un sentiero, ma non ti ricordi più la direzione di casa.\n"
                f"Gli unici oggetti che hai con te sono un celluare scarico, un panino ed una bottiglia d'acqua.\n"
                f"(Si trovano tutti all'interno del tuo zaino. Nel tuo zaino c'è posto ancora per 7 oggetti)\n"
                f""
                f"Guardati attorno e cerca un modo per uscire da questa foresta!\n"
                f"Ma fai attenzioni ai pericoli che potresti incontrare...\n")
        print(text)


    def animal_shows(self):
        text = ("In lontananza si sentono dei rumori tra gli alberi...\n"
                "Forse sono degli animali che si muovono."
                "Vuoi andare in quella direzione? (S/N)")
        print(text)
        response = str(input())
        if self.utils.check_sn_answer(response, self.animal_shows):
            print("Ti dirigi verso il fruscio tra gli alberi")
            self.animal_encounter()
        else:
            print("Ti dirigi dalla parte opposta.")


    def animal_encounter(self):
        self.animal_crossing = True
        text = (f"Dopo qualche passo, intravedi in lontananza un {self.forest.animals.name}.\n"
                f"Non sembra che ti abbia ancora notato.\n"
                f"Cosa vuoi fare?")
        print(text)






    def increase_counter(self):
        self.counter = self.counter + 1


    def check_n_blocks(self):
        if self.counter == self.end_index:
            self.chapter1_end()
        else:
            pass

    def chapter1_end(self):
        pass
