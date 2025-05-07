from random import sample, shuffle

ELEMENTS = {
    "H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium", "B": "Boron",
    "C": "Carbon", "N": "Nitrogen", "O": "Oxygen", "F": "Fluorine", "Ne": "Neon"
}

class Question:
    def __init__(self, information, answer):
        self.information = information
        self.answer = answer
    
    def __str__(self):
        return f"Information: {self.information}\nAnswer: {self.answer}"

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()

    
class MultipleChoiceQuestion(Question):
    def __init__(self, information, answer):
        super().__init__(information, answer)
        self.choices = sample([information for information, answer in ELEMENTS.items() if information != self.information], 3) # List comprehension used to get a list of symbol to pick from
        self.choices.append(self.information)
        shuffle(self.choices)

    def display(self):
        print(self.information)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")