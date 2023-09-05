import random

import enemies


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_text(self):
        raise NotImplementedError("Not implemented")

    def encounter_counter(self):
        pass

    def modify_player(self, player):
        pass


class EnemyTile(MapTile):
    def __init__(self, x, y):
        self.counter = 0
        frequency = random.random()
        if frequency > .98:
            self.enemy = enemies.Dragon()
        elif frequency > 95:
            self.enemy = enemies.Rabbit()
        elif frequency > .83:
            self.enemy = enemies.Troll()
        elif frequency > .60:
            self.enemy = enemies.Bat()
        elif frequency > .20:
            self.enemy = enemies.Ghost()
        elif frequency > 0:
            self.enemy = enemies.Goblin()

        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive() and self.check_attack_state():
            player.hp -= self.enemy.damage
            print("you have " + str(max(0, player.hp)) + "HP remaining.")

    def show_text(self):
        """
        Show different Enemy text during encounters
        :return: The Enemy character text
        """
        if not self.enemy.is_alive():
            text = self.enemy.death_text
            self.enemy.defeated = True
        elif self.check_attack_state():
            text = self.enemy.attack_text
        else:
            text = self.enemy.intro_text
        return text

    def encounter_counter(self):
        """
        Updates the enemy encounter counter.
        """
        self.counter += 1

    def check_attack_state(self):
        # could check 'aggression' here Eg:
        '''
        if self.enemy.aggression > 70
            attack
        elif
            '''
        return self.counter != 0


class StartTile(MapTile):
    def show_text(self):
        return """you stand at the entrance of a cave."""

    def __init__(self, x, y):
        super().__init__(x, y)


class NothingTile(MapTile):
    def show_text(self):
        return """there's nothing here."""

    def __init__(self, x, y):
        super().__init__(x, y)


class EndTile(MapTile):
    def show_text(self):
        return """you walk out of the maze"""

    def __init__(self, x, y):
        super().__init__(x, y)


world_map = []

world_dsl = """
|  |VT|NT|NT|NT|
|  |EN|  |  |NT|
|EN|ST|EN|NT|EN|
"""


def validate_dsl(dsl):
    if dsl.count("|VT|") != 1:
        return False
    if dsl.count("|ST|") != 1:
        return False
    lines = dsl.splitlines()
    lines = [line for line in lines if line]
    pipe_count = [line.count("|") for line in lines]
    for pipes in pipe_count:
        if pipes != pipe_count[0]:
            return False
    return True


def parse_dsl(dsl):
    if not validate_dsl(dsl):
        raise ValueError("Parsing DSL failed. Check pipe counts in world_dsl")

    lines = dsl.splitlines()
    lines = [lin for lin in lines if lin]

    for col_index, line in enumerate(lines):
        tiles = [cell for cell in line.split("|") if cell]

        row = []
        for row_index, tile in enumerate(tiles):
            tile_type = tile_dictionary[tile]
            row.append(tile_type(row_index, col_index) if tile_type else None)

        world_map.append(row)


tile_dictionary = {"ST": StartTile,
                   "VT": EndTile,
                   "NT": NothingTile,
                   "EN": EnemyTile,
                   "  ": None
                   }


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    elif y < len(world_map) and x < len(world_map[y]):
        return world_map[y][x]
