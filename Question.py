from random import sample, shuffle

class Question:
    def __init__(self, information, answer):
        self.__information = information
        self.__answer = answer
    
    def __str__(self):
        return f"Information: {self.__information}\nAnswer: {self.__answer}"

    def get_information(self):
        return self.__information
    
    def get_answer(self):
        return self.__answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.__answer.lower()


class MultipleChoiceQuestion(Question):
    def __init__(self, information, answer, choices):
        super().__init__(information, answer)
        self.__choices = choices
    
    def get_choices(self):
        return self.__choices

    def display(self):
        print(self.__information)
        for i, choice in enumerate(self.__choices):
            print(f"{i + 1}. {choice}")