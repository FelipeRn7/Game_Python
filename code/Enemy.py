#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    # Class to represent an enemy in the game, inherits from 'Entity'
    def __init__(self, name: str, position: tuple, can_shot=False):
        # Initializes the enemy with a name, position, and shooting ability
            super().__init__(name, position)
            self.can_shot = can_shot
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        # Method responsible for the enemy's movement
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shot(self):
        # Method responsible for the enemy's shooting, if allowed
        enemy1_shot_sound = pygame.mixer.Sound("./asset/ShotE.ogg")
        enemy2_shot_sound = pygame.mixer.Sound("./asset/ShotE.ogg")
        if self.can_shot and self.shot_delay == 0:
            if self.name == 'Enemy1':
                enemy1_shot_sound.play()
            elif self.name == 'Enemy2':
                enemy2_shot_sound.play()
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

        if self.can_shot:
            self.shot_delay -= 1

        return None