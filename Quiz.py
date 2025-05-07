from Question import *
from random import shuffle

ELEMENTS = {
    "H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium", "B": "Boron",
    "C": "Carbon", "N": "Nitrogen", "O": "Oxygen", "F": "Fluorine", "Ne": "Neon"
}

class Quiz:
    def __init__(self, gamemode):
        self.__score = 0

        self.questions = []
        for symbol, element in ELEMENTS.items():
            if gamemode == 1:
                self.questions.append(MultipleChoiceQuestion(symbol, element))
            else:
                self.questions.append(Question(symbol, element))
        shuffle(self.questions)
    
    def get_score(self):
        return self.__score
    
    def check_answer(self, user_answer, question_number, score_addition):
        if self.questions[question_number].check_answer(user_answer):
            self.__score += score_addition
            print("Correct Answer")
        else:
            print("Wrong Answer!")
        print(f"Score: {self.__score}")