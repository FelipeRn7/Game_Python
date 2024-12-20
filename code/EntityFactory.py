#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(5):  # Level 1 bg images number
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2bg':
                list_bg = []
                for i in range(5):  # Level 2 bg images number
                    list_bg.append(Background(f'Level2bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            # Creating Players, Enemies and Meteors
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30), can_shot=True)
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30), can_shot=True)
            case 'Meteor1':
                return Enemy('Meteor1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), can_shot=False)
            case 'Meteor2':
                return Enemy('Meteor2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), can_shot=False)
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), can_shot=True)
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)), can_shot=True)
