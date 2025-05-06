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

# Pygame standard setup
pg.init()
game = Game(WIDTH, HEIGHT)
game.running = True

# Main menu text
main_menu_text = pg.sprite.Group()
main_menu_text.add(FontSprite(WIDTH/2, 120, "Periodic Table Quiz", "lucidasanstypewriter", 54))

# Settings text
settings_text = pg.sprite.Group()
settings_text.add(FontSprite(WIDTH/2, 60, "Settings", "lucidasanstypewriter", 54))

def main():
    # Game loop
    while game.running:
        
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                game.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    if game.screen_number == -1:
                        game.screen_number = 1
                    elif game.screen_number == 2:
                        game.screen_number = 1
                    elif game.screen_number == 3:
                        game.screen_number = 2
        

        # Draws the screen depending on the screen number
        game.screen.fill(game.screen_color)

        # Main menu screen
        if game.screen_number == 1:
            game.screen.fill(game.screen_color)
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
            onClick=lambda: game.set_screen(2) # Set screen to question type
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
            onClick=lambda: game.set_screen(-1) # Set screen to question type
            )

        elif game.screen_number == 2:            
            button_1 = None
            button_2 = None
            button_3 = None
            button_4 = None
        
        elif game.screen_number == 3:
            pass

        elif game.screen_number == -1:
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
            onClick=lambda: game.toggle_dark_mode() # Set screen to question type
            )

        
        pygame_widgets.update(events)
        pg.display.flip()

        game.clock.tick(60)  # limits FPS to 60

if __name__ == "__main__":
    main()
    pg.quit()