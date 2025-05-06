class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def __str__(self):
        return f"Question: {self.question}\nAnswer: {self.answer}"

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()

    
class MultipleChoiceQuestion(Question):
    def __init__(self, question, answer, choices):
        super().__init__(question, answer)
        self.choices = choices

    def display(self):
        print(self.question)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")