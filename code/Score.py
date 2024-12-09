# Import necessary libraries and modules
import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

# Import constants and database proxy
from code.Const import C_WHITE, C_DARKVIOLET, SCORE_POS, MENU_OPTION
from code.DBProxy import DBProxy


# Class to handle the score screen and save scores
class Score:
    def __init__(self, window: Surface):
        # Initialize the score screen with the provided window

        self.window = window
        self.surf = pygame.image.load('./asset/Scorebg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        # Handles saving scores and collecting player/team names

        pygame.mixer_music.load('./asset/Score.mp3')  # Load background music
        pygame.mixer_music.play(-1)  # Loop music
        db_proxy = DBProxy('DBScore')  # Initialize database proxy
        name = ''  # Initialize name input

        while True:
            # Draw the score screen
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!', C_DARKVIOLET, SCORE_POS['Title'])

            # Determine score and input text based on game mode
            if game_mode == MENU_OPTION[0]:  # Single Player
                score = player_score[0]
                text = 'Enter Your Name (4 characters):'
            elif game_mode == MENU_OPTION[1]:  # Co-op
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team Name (4 characters):'
            elif game_mode == MENU_OPTION[2]:  # Versus
                if player_score[0] > player_score[1]:
                    score = player_score[0]
                    text = 'Player 1 Wins! Enter Your Name (4 characters):'
                elif player_score[1] > player_score[0]:
                    score = player_score[1]
                    text = 'Player 2 Wins! Enter Your Name (4 characters):'
                else:
                    score = player_score[0]
                    text = 'Tie! Enter Name (4 characters):'

            # Display the input prompt
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    # Handle return key to save the name and score
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()  # Show top scores
                        return
                    elif event.key == K_BACKSPACE:  # Handle backspace to remove last character
                        name = name[:-1]
                    else:  # Add character to the name if it's under 4 characters
                        if len(name) < 4:
                            name += event.unicode

            # Display the entered name
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        # Displays the top 10 scores
        pygame.mixer_music.load('./asset/Score.mp3')  # Load background music
        pygame.mixer_music.play(-1)  # Loop music
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_WHITE, SCORE_POS['Title'])
        self.score_text(20, 'NAME      SCORE          DATE', C_WHITE, SCORE_POS['Label'])

        db_proxy = DBProxy('DBScore')  # Initialize database proxy
        list_score = db_proxy.retrieve_top10()  # Retrieve top scores
        db_proxy.close()  # Close the database connection

        for player_score in list_score:
            # Display each score in the top 10

            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score :05d}          {date}', C_WHITE,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            # Wait for user interaction to close the top score screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Renders and displays text at the specified position

        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    # Returns the current date and time in a formatted string

    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M')
    current_date = current_datetime.strftime('%d/%m/%y')
    return f'{current_time} - {current_date}'
