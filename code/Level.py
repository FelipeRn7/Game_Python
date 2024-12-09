#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import required libraries and modules
import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

# Import game-specific constants and classes
from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


# Class to manage individual game levels
class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        # Initialize level attributes
        self.timeout = TIMEOUT_LEVEL  # Set initial timeout duration
        self.window = window  # Main game window
        self.name = name  # Level name
        self.game_mode = game_mode  # Selected game mode
        self.entity_list: list[Entity] = []  # List of entities in the level
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'bg'))  # Add level background
        player = EntityFactory.get_entity('Player1')  # Create Player1
        player.score = player_score[0]  # Set Player1 score
        self.entity_list.append(player)  # Add Player1 to entity list
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:  # Check for Co-op or Versus mode
            player = EntityFactory.get_entity('Player2')  # Create Player2
            player.score = player_score[1]  # Set Player2 score
            self.entity_list.append(player)  # Add Player2 to entity list

        # Set timers for spawning enemies and reducing timeout
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

        # Filter out entities that are out of bounds or have no health
        self.entity_list = [
            ent for ent in self.entity_list if ent.health > 0 and ent.rect.colliderect(self.window.get_rect())
        ]

    def run(self, player_score: list[int]):
        # Main game loop for the level
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')  # Load level-specific music
        pygame.mixer_music.play(-1)  # Play music in a loop
        clock = pygame.time.Clock()  # Initialize clock for managing FPS

        while True:
            clock.tick(60)  # Maintain 60 FPS
            for ent in self.entity_list:
                # Draw each entity and handle movement
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                # Handle entity shots (e.g., Player and Enemy)
                if isinstance(ent, (Player, Enemy)) and getattr(ent, 'can_shot', False):
                    shot = ent.shot()
                    if shot is not None:
                        self.entity_list.append(shot)

                # Display Player1 and Player2 stats
                if ent.name == 'Player1':
                    self.level_text(7, f'Player1 - Health: {ent.health} | Score: {ent.score}', C_WHITE, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(7, f'Player2 - Health: {ent.health} | Score: {ent.score}', C_WHITE, (10, 45))

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Quit the game
                    sys.exit()  # Terminate the program
                if event.type == EVENT_ENEMY:
                    # Spawn a random enemy
                    choice = random.choice(('Meteor1', 'Meteor2', 'Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    # Decrease timeout
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        # Update scores and end level
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] += ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] += ent.score
                        return True

            # Check if any players are still alive
            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True
            if not found_player:
                return False

            # Display level text (timeout, FPS, number of entities)
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()  # Update the screen

            # Handle collisions and check entity health
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        # Display text on the level screen
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)  # Set font style and size
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Render text
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])  # Position the text
        self.window.blit(source=text_surf, dest=text_rect)  # Draw text on the screen
