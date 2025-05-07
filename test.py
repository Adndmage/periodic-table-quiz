import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)
FONT = pygame.font.Font(None, 36)

# Elements Data (Symbol: Name)
elements = {
    "H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium", "B": "Boron",
    "C": "Carbon", "N": "Nitrogen", "O": "Oxygen", "F": "Fluorine", "Ne": "Neon"
}

class Question:
    def __init__(self, symbol, answer):
        self.symbol = symbol
        self.answer = answer
    
    def get_question_text(self):
        return f"What is the name of the element with symbol: {self.symbol}?"
    
    def check_answer(self, user_input):
        return user_input.lower() == self.answer.lower()

class MultipleChoiceQuestion(Question):
    def __init__(self, symbol, answer, options):
        super().__init__(symbol, answer)
        self.options = options
    
    def get_question_text(self):
        options_text = "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(self.options)])
        return f"What is the name of the element with symbol: {self.symbol}?\n{options_text}"
    
    def check_answer(self, user_input):
        try:
            return self.options[int(user_input) - 1].lower() == self.answer.lower()
        except (IndexError, ValueError):
            return False

class QuestionSprite(pygame.sprite.Sprite):
    def __init__(self, text, position):
        super().__init__()
        self.image = FONT.render(text, True, BLACK)
        self.rect = self.image.get_rect(topleft=position)
    
    def update(self, new_text):
        self.image = FONT.render(new_text, True, BLACK)

class PeriodicTableQuiz:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Periodic Table Quiz")
        self.score = 0
        self.running = True
        self.user_input = ""
        
        self.all_sprites = pygame.sprite.Group()
        self.new_question()
        
        self.question_sprite = QuestionSprite(self.question.get_question_text(), (50, 50))
        self.input_sprite = QuestionSprite(self.user_input, (50, 100))
        self.score_sprite = QuestionSprite(f"Score: {self.score}", (50, 200))
        self.all_sprites.add(self.question_sprite, self.input_sprite, self.score_sprite)
    
    def new_question(self):
        symbol, answer = random.choice(list(elements.items()))
        if random.random() > 0.5:
            options = random.sample(list(elements.values()), 3)
            if answer not in options:
                options[random.randint(0, 2)] = answer
            self.question = MultipleChoiceQuestion(symbol, answer, options)
        else:
            self.question = Question(symbol, answer)
        
        if hasattr(self, 'question_sprite'):
            self.question_sprite.update(self.question.get_question_text())
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.check_answer()
                elif event.key == pygame.K_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                else:
                    self.user_input += event.unicode
                self.input_sprite.update(self.user_input)
    
    def check_answer(self):
        if self.question.check_answer(self.user_input):
            self.score += 1
            feedback = "Correct!"
            color = GREEN
        else:
            feedback = f"Wrong! It was {self.question.answer}"
            color = RED
        
        feedback_sprite = QuestionSprite(feedback, (50, 150))
        self.all_sprites.add(feedback_sprite)
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
        pygame.time.delay(1000)
        self.all_sprites.remove(feedback_sprite)
        self.user_input = ""
        self.new_question()
        self.score_sprite.update(f"Score: {self.score}")
    
    def run(self):
        while self.running:
            self.screen.fill(WHITE)
            self.all_sprites.draw(self.screen)
            self.handle_events()
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    game = PeriodicTableQuiz()
    game.run()