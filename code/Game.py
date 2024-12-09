#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import required modules
import pygame

# Import game-specific constants and classes
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


# Main Game Class
class Game:
    def __init__(self):
        # Initialize Pygame and create the game window
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Set window size

    def run(self):
        # Main game loop
        while True:
            score = Score(self.window)  # Initialize the score screen
            menu = Menu(self.window)  # Initialize the menu
            menu_return = menu.run()  # Display the menu and get the user's selection

            # If the user selects a playable game mode
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # Initialize player scores

                # Start Level 1
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                if level_return:  # If Level 1 is successfully completed
                    # Start Level 2
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

                    if level_return:  # If Level 2 is successfully completed
                        score.save(menu_return, player_score)  # Save scores to the database

            # If the user selects the "Score" option
            elif menu_return == MENU_OPTION[3]:
                score.show()  # Display the top scores

            # If the user selects "Exit"
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Quit Pygame
                quit()  # Exit the program

            # Handle unexpected cases
            else:
                pass
