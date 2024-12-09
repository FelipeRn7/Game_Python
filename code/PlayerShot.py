# Imports necessary constants and the base Entity class
from code.Const import ENTITY_SPEED
from code.Entity import Entity

# Defines the PlayerShot class, inheriting from the Entity class
class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        # Initializes the PlayerShot instance with name and position
        super().__init__(name, position)

    def move(self):
        # Moves the shot to the right based on its speed
        self.rect.centerx += ENTITY_SPEED[self.name]
