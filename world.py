import random
import enemies
import npc


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


class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def intro_text(self):
        return """
        A trader stands by the side of the road.
        """

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print(f"{i}. {item} ({item.value} Gold)")

        while True:
            user_input = input("Make your choice: ")
            print("Press Q to quit")
            if user_input.lower() == 'q':
                return
            try:
                choice = int(user_input) - 1
                to_swap = seller.inventory[choice]
                self.swap(seller, buyer, to_swap)
            except IndexError:
                print("That's not for sale!")
            except ValueError:
                print("That's not an option!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("You don't have enough gold.")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        buyer.gold -= item.value
        seller.gold += item.value
        print("Item traded.")

    def check_if_trade(self, player):
        while True:
            print("Are you (b)uying or (s)elling?")
            print("Press q to quit.")
            user_input = input().lower()
            if user_input == 'q':
                return
            if user_input == 'b':
                print("Here's what I've got: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input == 's':
                print("Let's see what you've got!")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("You can't do that.")


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
|  |VT|BT|BT|BT|  |
|  |EN|  |  |EN|BT|
|TT|ST|EN|BT|BT|  |
|  |EN|  |  |EN|  |
"""


def parse_world_dsf():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("Error: Invalid DSL.")
    # Split the DSL into seperate lines
    rows = world_dsl.splitlines()
    # Only include lines that contain something
    rows = [x for x in rows if x]
    # Provide an index value (y) for each new row
    # Use a delimeter to split the rows into non-empty cells
    for y, rows in enumerate(rows):
        # Store tiles in a list
        tiles = []
        cell = rows.split("|")
        cell = [c for c in cell if c]
        # Provide an index value (x) to each new cell
        # Convert DSL abbreviations to classes
        # Store the tile_type in a row, then add the finished row to the world map
        for x, cell in enumerate(cell):
            tile_type = tile_type_dict[cell]
            tiles.append(tile_type(x, y) if tile_type else None)
        world_map.append(tiles)


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
                  "BT": BoringTile,
                  "TT": TraderTile,
                  "  ": None}

# Define all the tiles in the world map
# Note that world_map[] are rows and world_map[][] are columns
world_map = []


# Retrieve a tile at a given location
def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
