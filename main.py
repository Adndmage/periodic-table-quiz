import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.button import ButtonArray
from Game import Game
from Question import Question, MultipleChoiceQuestion #, InputQuestion, TrueFalseQuestion
from Quiz import Quiz
from sprites import FontSprite

# Constants
WIDTH, HEIGHT = 720, 720
ELEMENT_NAMES = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
    "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
    ]
ELEMENT_SYMBOLS = [
    "H", "He", "Li", "Be", "B",
    "C", "N", "O", "F", "Ne",
    ]
ELEMENT_NUMBERS = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    ]

ELEMENTS = {
    "H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium", "B": "Boron",
    "C": "Carbon", "N": "Nitrogen", "O": "Oxygen", "F": "Fluorine", "Ne": "Neon"
}

# Pygame standard setup
pg.init()
game = Game(WIDTH, HEIGHT)
game.running = True

# Main menu text
main_menu_text = pg.sprite.Group()
main_menu_text.add(FontSprite(WIDTH/2, 120, "Periodic Table Quiz", "lucidasanstypewriter", 54))

# Quiz type selection menu text
game_selection_menu_text = pg.sprite.Group()
game_selection_menu_text.add(FontSprite(WIDTH/2, 60, "Select Game Type", "lucidasanstypewriter", 54))

# Question type selection menu text
question_selection_menu_text = pg.sprite.Group()
question_selection_menu_text.add(FontSprite(WIDTH/2, 60, "Select Question Type", "lucidasanstypewriter", 54))

# Settings text
settings_text = pg.sprite.Group()
settings_text.add(FontSprite(WIDTH/2, 60, "Settings", "lucidasanstypewriter", 54))

# Question text
question_text = pg.sprite.Group()

def main():
    # Game loop
    while game.running:
        events = pg.event.get()
        question_text.empty() # Empties question text, so it resets every frame

        for event in events:
            if event.type == pg.QUIT:
                game.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    if game.quiz:
                        game.quiz = None
                        game.set_screen(1)
                    elif game.get_screen_number() == -1:
                        game.set_screen(1)
                    elif game.get_screen_number() == 2:
                        game.set_screen(1)
                    elif game.get_screen_number() == 3:
                        game.set_screen(2)

        # Draws the screen depending on the screen number
        game.screen.fill(game.screen_color)

        if game.quiz:
            try:
                if game.get_gamemode() == "multiple choice":
                    question_text.add(FontSprite(WIDTH/2, 60, f"What is the symbol of {game.quiz.questions[game.current_question_number].answer}?", "lucidasanstypewriter", 32))

                    # if game.get_gamemode == "multiple choice":
                    answer_choices = game.quiz.questions[game.current_question_number].choices

                    button_1 = Button(game.screen,
                    85, 235, 250, 100, # Coordinates and size
                    text=answer_choices[0],
                    font=pg.font.SysFont("lucidasanstypewriterregular", 16),
                    margin=10,
                    borderRadius=2,
                    borderThickness=2,
                    colour="#D3D3D3",
                    borderColour="#000000",
                    inactiveColour="#FFFFFF",
                    pressedColour="#C1E1C1",
                    radius=2,
                    onClick=lambda: game.check_answer(ELEMENTS.get(answer_choices[0]))
                    )

                    button_2 = Button(game.screen,
                    385, 235, 250, 100, # Coordinates and size
                    text=answer_choices[1],
                    font=pg.font.SysFont("lucidasanstypewriterregular", 16),
                    margin=10,
                    borderRadius=2,
                    borderThickness=2,
                    colour="#D3D3D3",
                    borderColour="#000000",
                    inactiveColour="#FFFFFF",
                    pressedColour="#C1E1C1",
                    radius=2,
                    onClick=lambda: game.check_answer(ELEMENTS.get(answer_choices[1]))
                    )

                    button_3 = Button(game.screen,
                    85, 385, 250, 100, # Coordinates and size
                    text=answer_choices[2],
                    font=pg.font.SysFont("lucidasanstypewriterregular", 16),
                    margin=10,
                    borderRadius=2,
                    borderThickness=2,
                    colour="#D3D3D3",
                    borderColour="#000000",
                    inactiveColour="#FFFFFF",
                    pressedColour="#C1E1C1",
                    radius=2,
                    onClick=lambda: game.check_answer(ELEMENTS.get(answer_choices[2]))
                    )

                    button_4 = Button(game.screen,
                    385, 385, 250, 100, # Coordinates and size
                    text=answer_choices[3],
                    font=pg.font.SysFont("lucidasanstypewriterregular", 16),
                    margin=10,
                    borderRadius=2,
                    borderThickness=2,
                    colour="#D3D3D3",
                    borderColour="#000000",
                    inactiveColour="#FFFFFF",
                    pressedColour="#C1E1C1",
                    radius=2,
                    onClick=lambda: game.check_answer(ELEMENTS.get(answer_choices[3]))
                    )
            except:
                game.quiz = None
                game.set_screen(1)
                print("No more questions left")
        
        else:
            # Main menu screen
            if game.get_screen_number() == 1:
                main_menu_text.draw(game.screen)

                button_3 = None
                button_4 = None
                
                # Buttons
                button_1 = Button(game.screen,
                100, 235, WIDTH - 200, 100, # Coordinates and size
                text="Start Game",
                font=pg.font.SysFont("lucidasanstypewriterregular", 30),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.set_screen(2) # Set screen to game type
                )

                button_2 = Button(game.screen,
                100, 385, WIDTH - 200, 100, # Coordinates and size
                text="Settings",
                font=pg.font.SysFont("lucidasanstypewriterregular", 30),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.set_screen(-1) # Set screen to settings
                )

            elif game.get_screen_number() == 2:
                game_selection_menu_text.draw(game.screen)

                button_4 = None

                button_1 = Button(game.screen,
                85, 235, 250, 100, # Coordinates and size
                text="Multiple Choice",
                font=pg.font.SysFont("lucidasanstypewriterregular", 20),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.set_screen_and_gamemode(3, "multiple choice") # Set screen to question type and set game to Multiple Choice
                )

                button_2 = Button(game.screen,
                385, 235, 250, 100, # Coordinates and size
                text="Text Input",
                font=pg.font.SysFont("lucidasanstypewriterregular", 20),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.set_screen_and_gamemode(3, "text input") # Set screen to question type and set game to Text Input
                )

                button_3 = Button(game.screen,
                235, 385, 250, 100, # Coordinates and size
                text="True or False",
                font=pg.font.SysFont("lucidasanstypewriterregular", 20),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.set_screen_and_gamemode(3, "true or false") # Set screen to question type and set game to True or False
                )
            
            elif game.get_screen_number() == 3:
                question_selection_menu_text.draw(game.screen)

                button_1 = Button(game.screen,
                85, 235, 250, 100, # Coordinates and size
                text="Name -> Atomic Number",
                font=pg.font.SysFont("lucidasanstypewriterregular", 16),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.set_screen_and_question_type_and_start_quiz(3, "name to number") # Set screen to question type and set game to Multiple Choice
                )

                button_2 = Button(game.screen,
                385, 235, 250, 100, # Coordinates and size
                text="Atomic Number -> Name",
                font=pg.font.SysFont("lucidasanstypewriterregular", 16),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.set_screen_and_question_type_and_start_quiz(3, "number to name") # Set screen to question type and set game to Text Input
                )

                button_3 = Button(game.screen,
                85, 385, 250, 100, # Coordinates and size
                text="Name -> Symbol",
                font=pg.font.SysFont("lucidasanstypewriterregular", 16),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.set_screen_and_question_type_and_start_quiz(3, "symbol to number") # Set screen to question type and set game to True or False
                )

                button_4 = Button(game.screen,
                385, 385, 250, 100, # Coordinates and size
                text="Symbol -> Name",
                font=pg.font.SysFont("lucidasanstypewriterregular", 16),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.set_screen_and_question_type_and_start_quiz(3, "number to symbol") # Set screen to question type and set game to True or False
                )

            elif game.get_screen_number() == -1:
                settings_text.draw(game.screen)
                button_2 = None
                button_3 = None
                button_4 = None

                button_1 = Button(game.screen,
                100, 235, WIDTH - 200, 100, # Coordinates and size
                text="Toggle Dark Mode",
                font=pg.font.SysFont("lucidasanstypewriterregular", 30),
                margin=10,
                borderRadius=2,
                borderThickness=2,
                colour="#D3D3D3",
                borderColour="#000000",
                inactiveColour="#FFFFFF",
                pressedColour="#C1E1C1",
                radius=2,
                onClick=lambda: game.toggle_dark_mode() # Set screen to main menu
                )
        
        question_text.draw(game.screen)
        pygame_widgets.update(events)
        pg.display.flip()
        game.clock.tick(60)  # limits FPS to 60

if __name__ == "__main__":
    main()
    pg.quit()