#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

# Imports constants and classes used in the Player class
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


# Defines the Player class, inheriting from the Entity class
class Player(Entity):
    def __init__(self, name: str, position: tuple, can_shot=False):
        # Initializes the Player instance with name, position, and shooting capabilities
        super().__init__(name, position)
        self.can_shot = can_shot  # Determines if the player can shoot
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Sets the shooting delay for the player

    def move(self):
        # Handles player movement based on key presses
        pressed_key = pygame.key.get_pressed()  # Gets the current state of keyboard keys
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]  # Moves player up
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]  # Moves player down
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]  # Moves player left
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]  # Moves player right
        pass

    def shot(self):
        # Handles shooting functionality for the player
        player1_shot_sound = pygame.mixer.Sound("./asset/ShotP.ogg")  # Sound effect for Player1's shot
        player2_shot_sound = pygame.mixer.Sound("./asset/ShotP.ogg")  # Sound effect for Player2's shot

        if self.can_shot:  # Checks if the player can shoot
            self.shot_delay -= 1  # Decreases the shooting delay counter

            if self.shot_delay == 0:  # If shooting delay is over
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Resets the shooting delay

                pressed_key = pygame.key.get_pressed()  # Checks the current state of keyboard keys
                if pressed_key[PLAYER_KEY_SHOT[self.name]]:  # Checks if the shoot key is pressed
                    if self.name == 'Player1':  # Plays Player1's shooting sound
                        player1_shot_sound.play()
                    elif self.name == 'Player2':  # Plays Player2's shooting sound
                        player2_shot_sound.play()

                    # Returns a new PlayerShot object with the player's shot position
                    return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

        return None  # Returns None if shooting is not possible
