import random
import enemies


# Describes tiles on the map and the map grid using
# x, y coordinates
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_tile(self):
        raise NotImplementedError("Create a subclass.")


# Tiles

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()

        if r < 0.50:
            # Using self ensures that the enemy object is
            # created alongside the tile
            self.enemy = enemies.GiantSpider()
        elif r < 0.80:
            self.enemy = enemies.Ogre()
        elif r < 95:
            self.enemy = enemies.AntColony()
        else:
            self.enemy = enemies.Scorpion()

        super().__init__(x, y)

    def intro_tile(self):
        if self.enemy.is_alive():
            print("You've come across an enemy.")
        else:
            print("You defeated an enemy.")

    def intro_text(self):
        return """
        You've encountered an enemy.
        """


class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch
        on the wall. 
        You can make out four paths. They all look the same.
        """


class BoringTile(MapTile):
    def intro_text(self):
        return """
        There is nothing in this part of the cave.
        """


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a light in the distance... 
        ... you close in... it's sunlight!
        
        Escaped!
        """


# Define all the tiles in the world map
# Note that world_map[] are rows and world_map[][] are columns
world_map = [
    [None, VictoryTile(1, 0), None],
    [None, EnemyTile(1, 1), None],
    [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
    [None, EnemyTile(1, 3), None]
]


# Retrieve a tile at a given location
def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
