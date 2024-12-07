#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, can_shoot=False):
            super().__init__(name, position)
            self.can_shoot = can_shoot
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        enemy1_shoot_sound = pygame.mixer.Sound("./asset/ShotE.ogg")
        enemy2_shoot_sound = pygame.mixer.Sound("./asset/ShotE.ogg")
        if self.can_shoot and self.shot_delay == 0:
            if self.name == 'Enemy1':
                enemy1_shoot_sound.play()
            elif self.name == 'Enemy2':
                enemy2_shoot_sound.play()
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

        if self.can_shoot:
            self.shot_delay -= 1

        return None