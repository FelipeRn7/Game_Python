# C
import pygame

C_WHITE = (255, 255, 255)
C_GOLD = (238, 155, 45)
C_VIOLET = (147, 112, 219)
C_GREEN = (0, 128, 0)
C_CYAN = (0,128,128)

# E

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_HEALTH = {'Level1bg0': 999,
                 'Level1bg1': 999,
                 'Level1bg2': 999,
                 'Level1bg3': 999,
                 'Level1bg4': 999,
                 'Level2bg0': 999,
                 'Level2bg1': 999,
                 'Level2bg2': 999,
                 'Level2bg3': 999,
                 'Level2bg4': 999,
                 'Player1': 100,
                 'Player1Shot': 1,
                 'Player2': 100,
                 'Player2Shot': 1,
                 'Meteor1': 15,
                 'Meteor2': 25,
                 'Enemy1': 20,
                 'Enemy1Shot': 1,
                 'Enemy2': 22,
                 'Enemy2Shot': 1,
                 }

ENTITY_SPEED = {
    'Level1bg0': 0,
    'Level1bg1': 1,
    'Level1bg2': 2,
    'Level1bg3': 3,
    'Level1bg4': 4,
    'Level2bg0': 0,
    'Level2bg1': 1,
    'Level2bg2': 2,
    'Level2bg3': 3,
    'Level2bg4': 4,
    'Player1': 3,
    'Player1Shot': 3,
    'Player2': 3,
    'Player2Shot': 3,
    'Meteor1': 3,
    'Meteor2': 2,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}

ENTITY_SHOT_DELAY = {
                  'Player1': 18,
                  'Player2': 20,
                  'Enemy1': 80,
                  'Enemy2': 95,
                  'Meteor1': 0,
                  'Meteor2': 0,
                  }

ENTITY_DAMAGE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,
    'Level1bg4': 0,
    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,
    'Level2bg3': 0,
    'Level2bg4': 0,
    'Player1': 1,
    'Player1Shot': 6,
    'Player2': 1,
    'Player2Shot': 5,
    'Enemy1': 1,
    'Enemy1Shot': 8,
    'Enemy2': 1,
    'Enemy2Shot': 5,
    'Meteor1': 10,
    'Meteor2': 12,
}

ENTITY_SCORE = {
    'Level1bg0': 0,
    'Level1bg1': 0,
    'Level1bg2': 0,
    'Level1bg3': 0,
    'Level1bg4': 0,
    'Level2bg0': 0,
    'Level2bg1': 0,
    'Level2bg2': 0,
    'Level2bg3': 0,
    'Level2bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 80,
    'Enemy2Shot': 0,
    'Meteor1': 65,
    'Meteor2': 43,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               "EXIT")

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 3000

# T
TIMEOUT_STEP = 100 # 100 ms
TIMEOUT_LEVEL = 20000 # 20 s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
