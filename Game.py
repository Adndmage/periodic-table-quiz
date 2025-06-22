import pygame as pg
from Quiz import Quiz
from math import floor

"""
The Game class that is used to handle most of the games data and updating of this data.
"""


class Game:
    def __init__(self, width, height):
        # Pygame setup attributes
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Periodic Table Quiz")
        self.clock = pg.time.Clock()
        self.running = True
        self.dynamic_text = pg.sprite.Group() # Dynamic text that might get updated with new information

        # UI and navigation
        self.__screen_color = "white" # Default screen color
        self.__screen_number = 1 # 1 for main menu, 2 for question type, 3 for quiz type, -1 for settings
        self.__gamemode = None
        self.__question_type = None
        self.__time = 1500
        self.time_display = "Time: 15.0"

        # Quiz related attributes
        self.__highscores = [[0, 0, 0, 0], # Multidimensional list to store highscores for each gamemode and question type
                             [0, 0, 0, 0], 
                             [0, 0, 0, 0]]
        
        self.quiz = None # Current quiz object
        self.__current_question_number = 0 # Current question number in the quiz
    
    def get_screen_color(self):
        return self.__screen_color
    
    def get_screen_number(self):
        return self.__screen_number
    
    def get_gamemode(self):
        return self.__gamemode
    
    def get_question_type(self):
        return self.__question_type
    
    def get_highscore(self):
        return self.__highscores[self.__gamemode - 1][self.__question_type - 1]

    def get_current_question_number(self):
        return self.__current_question_number

    def set_screen(self, screen_number):
        self.__screen_number = screen_number
    
    def set_screen_and_gamemode(self, screen_number, gamemode):
        self.__screen_number = screen_number
        self.__gamemode = gamemode
    
    def set_question_type_and_start_quiz(self, question_type):
        self.__question_type = question_type
        self.start_quiz()
    
    def set_highscore(self, new_highscore):
        self.__highscores[self.__gamemode - 1][self.__question_type - 1] = max(self.__highscores[self.__gamemode - 1][self.__question_type - 1], new_highscore)

    def toggle_dark_mode(self):
        self.__screen_color = "#323339" if self.__screen_color == "white" else "white"

    def start_quiz(self):
        self.quiz = Quiz(self.__gamemode, self.__question_type)
        self.__current_question_number = 0
        self.timer = 0
    
    def check_answer(self, user_answer):
        self.quiz.check_answer(user_answer, self.__current_question_number, floor(self.__time/10))
        self.__current_question_number += 1
        self.reset_time()
    
    def reset_time(self):
        self.__time = 1500
        self.time_display = "Time: 15.0"
    
    def update_time_display(self):
        self.__time -= 100/60

        minutes = floor(self.__time / 6000)
        seconds = floor((self.__time - minutes * 6000) / 100)
        hundreths = floor(self.__time - minutes * 6000 - seconds * 100)

        if minutes <= 0:
            self.time_display = "Time: " + str(seconds) + "." + str(hundreths)
        else:
            self.time_display = "Time: " + str(minutes) + ":" + str(seconds) + "." + str(hundreths)
        
        self.check_timeout()
    
    def check_timeout(self):
        if self.__time <= 0:
            self.__current_question_number += 1
            self.reset_time()