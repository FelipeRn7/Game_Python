from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    # Checks if the entity has collided with the window boundaries
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):  # If it's an enemy
            if ent.rect.right <= 0:  # Check if the enemy has gone off-screen
                ent.health = 0  # Destroy the enemy

        if isinstance(ent, PlayerShot):  # If it's a player's shot
            if ent.rect.left >= WIN_WIDTH:  # Check if the shot has gone off the screen
                ent.health = 0  # Destroy the shot

        if isinstance(ent, EnemyShot):  # If it's an enemy's shot
            if ent.rect.right <= 0:  # Check if the shot has gone off-screen
                ent.health = 0  # Destroy the shot

    # Checks for collision between two entities and applies damage
    @staticmethod
    def verify_collision_entity(ent1, ent2):
        valid_interaction = False
        # Determine valid interactions between entities
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        # If a valid interaction occurred, check for collision
        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):  # Rectangular collision detection
                ent1.health -= ent2.damage  # Apply damage
                ent2.health -= ent1.damage  # Apply damage
                ent1.last_dmg = ent2.name  # Record who dealt the damage
                ent2.last_dmg = ent1.name  # Record who dealt the damage

    # Awards score to the player who dealt the last damage to the enemy
    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':  # Add score to Player1
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':  # Add score to Player2
                    ent.score += enemy.score

    # Checks collisions for all entities in the list
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)  # Check window bounds
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.verify_collision_entity(entity1, entity2)  # Check entity collisions

    # Checks health and removes entities with 0 health from the list
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)  # Give score if enemy is destroyed
                entity_list.remove(ent)  # Remove entity from the list

