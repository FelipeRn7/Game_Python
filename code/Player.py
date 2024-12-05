#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple, can_shoot=False):
            super().__init__(name, position)
            self.can_shoot = can_shoot
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        # Verifica se o player pode atirar e se o delay chegou a zero
        if self.can_shoot:
            # Decrementa o delay a cada chamada do metodo
            self.shot_delay -= 1

            # Quando o delay chega a zero, verifica se a tecla de disparo foi pressionada
            if self.shot_delay == 0:
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # Reinicia o delay com base no nome do player

                # Verifica se a tecla associada ao disparo está pressionada
                pressed_key = pygame.key.get_pressed()
                if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                    # Retorna o disparo (shot) do player
                    return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

        # Caso contrário, nenhum disparo é retornado
        return None
