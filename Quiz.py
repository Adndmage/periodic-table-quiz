from Question import *
from random import sample, shuffle

# Quiz question constants
ELEMENT_NAMES = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
    "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
    ]
ELEMENT_SYMBOLS = [
    "H", "He", "Li", "Be", "B",
    "C", "N", "O", "F", "Ne",
    ]
ELEMENT_NUMBERS = [
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "10",
    ]

class Quiz:
    def __init__(self, gamemode, question_type):
        self.__score = 0

        qna_tuple = zip(ELEMENT_NAMES, ELEMENT_NUMBERS) if question_type == 1 else zip(ELEMENT_NUMBERS, ELEMENT_NAMES) if question_type == 2 else zip(ELEMENT_NAMES, ELEMENT_SYMBOLS) if question_type == 3 else zip(ELEMENT_SYMBOLS, ELEMENT_NAMES) if question_type == 4 else None
        self.__qna_dictionary = {information:answer for (information, answer) in qna_tuple}

        self.__questions = []
        for information, answer in self.__qna_dictionary.items():
            if gamemode == 1:
                choices = sample([answer_option for information_option, answer_option in self.__qna_dictionary.items() if answer_option != answer], 3)
                choices.append(answer)
                shuffle(choices)
                self.__questions.append(MultipleChoiceQuestion(information, answer, choices))
            else:
                self.__questions.append(Question(information, answer))
        shuffle(self.__questions)
    
    def get_score(self):
        return self.__score

    def get_questions(self):
        return self.__questions
    
    def check_answer(self, user_answer, question_number, score_addition):
        if self.__questions[question_number].check_answer(user_answer):
            self.__score += score_addition
            print("Correct Answer")
        else:
            print("Wrong Answer!")
        print(f"Score: {self.__score}")