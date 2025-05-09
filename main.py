import pygame as pg
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from Game import Game
from Question import Question, MultipleChoiceQuestion #, InputQuestion, TrueFalseQuestion
from Quiz import Quiz
from sprites import FontSprite

# Constants for game
WIDTH, HEIGHT = 720, 720
QUESTION_TITLES = {
    1: "Atomic Number",
    2: "Name",
    3: "Symbol",
    4: "Name"
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
game_selection_menu_text.add(FontSprite(WIDTH/2, 50, "Select Game Type", "lucidasanstypewriter", 54))

# Question type selection menu text
question_selection_menu_text = pg.sprite.Group()
question_selection_menu_text.add(FontSprite(WIDTH/2, 50, "Select Question Type", "lucidasanstypewriter", 54))

# Settings text
settings_text = pg.sprite.Group()
settings_text.add(FontSprite(WIDTH/2, 50, "Settings", "lucidasanstypewriter", 54))

def main():
    """
    The games game loop. Every second the game is updated 60 times (60 fps).
    Pygame_widgets buttons and inputs are used. To update these the variables must be redeclared or erased.
    This is why multiple declaration of the same variable names, but with different values are seen.
    Pygame handles the display of everything as well as key inputs from the user.
    """

    # Game loop
    while game.running:
        events = pg.event.get()
        game.dynamic_text.empty() # Empties dynamic text, so it resets every frame

        for event in events:
            if event.type == pg.QUIT:
                game.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if game.quiz:
                        game.quiz = None
                        game.set_screen(1)
                    elif game.get_screen_number() == -1:
                        game.set_screen(1)
                    elif game.get_screen_number() == 2:
                        game.set_screen(1)
                    elif game.get_screen_number() == 3:
                        game.set_screen(2)
                if event.key == pg.K_RETURN and game.get_gamemode() == 2 and input_box and game.quiz:
                    user_answer = input_box.getText()
                    game.check_answer(user_answer)
                    
                    input_box.setText("")

        # Draws the screen depending on the screen number
        game.screen.fill(game.get_screen_color())

        if game.quiz:
            try:
                game.dynamic_text.add(FontSprite(50, 100, f"Score: {game.quiz.get_score()}", "lucidasanstypewriter", 20, placement="midleft"))
                game.dynamic_text.add(FontSprite(50, 130, f"Highscore: {game.get_highscore()}", "lucidasanstypewriter", 20, placement="midleft"))
                question_title_text = QUESTION_TITLES.get(game.get_question_type(), "Error")
                game.dynamic_text.add(FontSprite(WIDTH/2, 60, f"What is the {question_title_text} for {game.quiz.get_questions()[game.get_current_question_number()].get_information()}?", "lucidasanstypewriter", 28))

                if game.get_gamemode() == 1:
                    input_box = None

                    answer_choices = game.quiz.get_questions()[game.get_current_question_number()].get_choices()

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
                    onClick=lambda: game.check_answer(answer_choices[0])
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
                    onClick=lambda: game.check_answer(answer_choices[1])
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
                    onClick=lambda: game.check_answer(answer_choices[2])
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
                    onClick=lambda: game.check_answer(answer_choices[3])
                    )

                elif game.get_gamemode() == 2:
                    button_1 = None
                    button_2 = None
                    button_3 = None
                    button_4 = None

                    if not input_box:
                        # Text input for Text Input gamemode
                        input_box = TextBox(game.screen,
                            90, 250, 540, 36, # Coordinates and size
                            borderThickness=1,
                            borderColour="#000000",
                            colour=("#D3D3D3"),
                            radius=2,
                            font=pg.font.SysFont("lucidasanstypewriterregular", 16),
                        )

            except:
                game.set_highscore(game.quiz.get_score())
                game.quiz = None
                game.set_screen(1)
                print("No more questions left")
        
        else:
            # Main menu screen
            if game.get_screen_number() == 1:
                main_menu_text.draw(game.screen)

                button_3 = None
                button_4 = None
                input_box = None
                
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

                button_3 = None
                button_4 = None
                input_box = None

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
                onClick=lambda: game.set_screen_and_gamemode(3, 1) # Set screen to question type and set gamemode to Multiple Choice
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
                onClick=lambda: game.set_screen_and_gamemode(3, 2) # Set screen to question type and set gamemode to Text Input
                )
            
            elif game.get_screen_number() == 3:
                question_selection_menu_text.draw(game.screen)

                input_box = None

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
                onClick=lambda: game.set_question_type_and_start_quiz(1) # Start quiz and set question type to name to number
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
                onClick=lambda: game.set_question_type_and_start_quiz(2) # Start quiz and set question type to number to name
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
                onClick=lambda: game.set_question_type_and_start_quiz(3) # Start quiz and set question type to name to symbol
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
                onClick=lambda: game.set_question_type_and_start_quiz(4) # Start quiz and set question type to symbol to name
                )

            elif game.get_screen_number() == -1:
                settings_text.draw(game.screen)

                button_2 = None
                button_3 = None
                button_4 = None
                input_box = None

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
        
        game.dynamic_text.draw(game.screen)
        pygame_widgets.update(events)
        pg.display.flip()
        game.clock.tick(60)  # limits FPS to 60

if __name__ == "__main__":
    main()
    pg.quit()