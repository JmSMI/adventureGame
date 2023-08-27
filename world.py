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

    def modify_player(self, player):
        pass


# Tiles

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()

        if r < 0.50:
            # Using self ensures that the enemy object is
            # created alongside the tile
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider drops down to attack."
            self.dead_text = "The spider is dead."
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = "An ogre lunges at you."
            self.dead_text = "The ogre has been killed."
        elif r < 95:
            self.enemy = enemies.AntColony()
            self.alive_text = "A colony of ants attacks you."
            self.dead_text = "The colony is dispersed"
        else:
            self.enemy = enemies.Scorpion()
            self.alive_text = "A scorpion jumps at you."
            self.dead_text = "The scorpion has been squashed."

        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp -= self.enemy.damage
            print("{} does {} damage. You have {} HP.".format(self.enemy.name, self.enemy.damage, player.hp))

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text


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


world_dsl = """
|  |VT|  |
|  |EN|  |
|EN|ST|EN|
|  |EN|  |
"""


def is_dsl_valid(dsl):
    if "VT" not in dsl or "ST" not in dsl:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [l.count("|") for l in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True


tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "  ": None}

# Define all the tiles in the world map
# Note that world_map[] are rows and world_map[][] are columns
world_map = [
    [None, VictoryTile(1, 0), None],
    [None, EnemyTile(1, 1), None],
    [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
    [None, EnemyTile(1, 3), None]
]


def parse_world_dsf():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("Error: Invalid DSL.")


# Retrieve a tile at a given location
def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
