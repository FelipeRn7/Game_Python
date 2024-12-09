#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import necessary libraries and modules
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

# Import constants
from code.Const import WIN_WIDTH, C_WHITE, MENU_OPTION, C_DARKVIOLET


# Class to handle the game menu
class Menu:
    def __init__(self, window):
        # Initialize the menu with the provided window
        self.window = window
        self.surf = pygame.image.load('./asset/Backimage.jpg').convert_alpha()  # Load background image
        self.rect = self.surf.get_rect(left=0, top=0)  # Position background image

    def run(self):
        # Display and handle menu navigation
        menu_option = 0  # Default starting menu option
        pygame.mixer_music.load('./asset/Background.mp3')  # Load background music
        pygame.mixer_music.play(-1)  # Play music in a loop

        while True:
            # DRAW IMAGES AND MENU TEXT
            self.window.blit(source=self.surf, dest=self.rect)  # Draw background image
            self.menu_text(50, 'Exclusion', C_WHITE, ((WIN_WIDTH / 2), 50))  # Title part 1
            self.menu_text(50, 'Zone', C_DARKVIOLET, ((WIN_WIDTH / 2), 100))  # Title part 2

            # Loop through menu options to display them
            for i in range(len(MENU_OPTION)):
                if i == menu_option:  # Highlight selected option
                    self.menu_text(20, MENU_OPTION[i], C_DARKVIOLET, ((WIN_WIDTH / 2), 170 + 30 * i))
                else:  # Display other options normally
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 170 + 30 * i))

            pygame.display.flip()  # Update the screen

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close the game window
                    quit()  # Terminate the program
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN key to navigate menu
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0  # Loop back to the first option
                    if event.key == pygame.K_UP:  # UP key to navigate menu
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1  # Loop to the last option
                    if event.key == pygame.K_RETURN:  # ENTER key to select an option
                        return MENU_OPTION[menu_option]  # Return the selected option

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Render and display text on the menu
        text_font: Font = pygame.font.SysFont(name='Creepster', size=text_size)  # Set font style and size
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Render text
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # Center the text
        self.window.blit(source=text_surf, dest=text_rect)  # Draw text on the screen
