import pygame as pg

class Game:
    def __init__(self, width, height):
        # Pygame setup attributes
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Periodic Table Quiz")
        self.clock = pg.time.Clock()
        self.running = True

        # UI and navigation
        self.screen_color = "white" # Default screen color
        self.screen_number = 1 # 1 for main menu, 2 for question type, 3 for quiz type, -1 for settings
        self.game_type = None

        # Quiz related attributes
        self.highscores = [] # Multidimensional list to store highscores for each quiz type
        
        self.current_quiz = None # Current quiz object
        self.current_question = None # Current question object
        self.current_question_number = 0 # Current question number in the quiz
    
    def set_screen(self, screen_number):
        self.screen_number = screen_number
    
    def set_screen_and_quiz_type(self, screen_number, game_type):
        self.screen_number = screen_number
        self.game_type = game_type
    
    def toggle_dark_mode(self):
        self.screen_color = "#323339" if self.screen_color == "white" else "white"