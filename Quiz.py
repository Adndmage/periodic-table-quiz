from Question import *
from random import shuffle

ELEMENTS = {
    "H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium", "B": "Boron",
    "C": "Carbon", "N": "Nitrogen", "O": "Oxygen", "F": "Fluorine", "Ne": "Neon"
}

class Quiz:
    def __init__(self, gamemode):
        self.score = 0

        self.questions = []
        for symbol, element in ELEMENTS.items():
            if gamemode == "multiple choice":
                self.questions.append(MultipleChoiceQuestion(symbol, element))
        shuffle(self.questions)
    
    def check_answer(self, user_answer, question_number, score_addition):
        if self.questions[question_number].check_answer(user_answer):
            self.score += score_addition
            print("Correct Answer")
        else:
            print("Wrong Answer!")
        print(f"Score: {self.score}")