#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    # Class representing the background in the game, inherits from the Entity class.

    def __init__(self, name: str, position: tuple):
        # Initializes the background entity, setting its name and position.
        super().__init__(name, position)

    def move(self, ):
        # Moves the background horizontally, resetting its position when it moves out of the screen.

        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
