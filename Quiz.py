from Question import *

class Quiz:
    def __init__(self, type=0, score=0):
        self.type = type
        self.score = score

        self.questions = []
        if self.type == 0:
            self.questions.append(MultipleChoiceQuestion("What is the atomic number of Hydrogen?", "1", ["1", "2", "6", "8"]))
