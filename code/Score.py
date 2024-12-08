import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_WHITE, C_DARKVIOLET, SCORE_POS, MENU_OPTION
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/Scorebg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!', C_DARKVIOLET, SCORE_POS['Title'])

            # Determinar o vencedor com base no game_mode e score
            if game_mode == MENU_OPTION[0]:  # Single Player
                score = player_score[0]
                text = 'Digite seu nome (4 caracteres):'
            elif game_mode == MENU_OPTION[1]:  # Co-op
                score = (player_score[0] + player_score[1]) / 2
                text = 'Digite o nome da equipe (4 caracteres):'
            elif game_mode == MENU_OPTION[2]:  # Versus
                if player_score[0] > player_score[1]:
                    score = player_score[0]
                    text = 'Player 1 venceu! Digite o nome (4 caracteres):'
                elif player_score[1] > player_score[0]:
                    score = player_score[1]
                    text = 'Player 2 venceu! Digite o nome (4 caracteres):'
                else:
                    score = player_score[0]
                    text = 'Empate! Digite um nome (4 caracteres):'

            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_WHITE, SCORE_POS['Title'])
        self.score_text(20, 'NAME      SCORE          DATE', C_WHITE, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score :05d}          {date}', C_WHITE,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()
            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M')
    current_date = current_datetime.strftime('%d/%m/%y')
    return f'{current_time} - {current_date}'