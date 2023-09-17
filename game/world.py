import random

import enemies
import npc
import items


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


class DarkTile(MapTile):
    def __init__(self, x, y):
        self.light = False
        super().__init__(x, y)

    def show_text(self):
        if self.light:
            return """you light up the path using your torch"""
        else:
            return """it's too dark to see anything"""

    def modify_player(self, player):
        # check if the player has a torch equipped
        if not player.torch_equipped():
            # stop the player from proceeding
            player.enableMovement = False
            self.light = False
        else:
            player.enableMovement = True
            self.light = True


class ChallengeTile(MapTile):
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
            print("you have " + str(max(0, player.hp)) + "hp remaining.")

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


class WinTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def show_text(self):
        return """you walk out of the maze"""


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = None
        self.claimed = False
        self.generate_gold()
        super().__init__(x, y)

    def generate_gold(self):
        rand = random.random()
        if rand > .99:
            amount = 30
        elif rand > .95:
            amount = 15
        else:
            amount = random.randint(2, 8)
        self.gold = items.Gold(amount)

    def modify_player(self, player):
        if not self.claimed:
            player.gold.deposit(self.gold.get_balance())
            print(f"you find {self.gold.get_balance()} gold")
        self.generate_gold()

    def show_text(self):
        if self.claimed:
            return """there's nothing else to find here"""
        return """you stumble on some loot"""


class MerchantTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def show_text(self):
        return """a merchant has set up shop here"""


world_map = []

world_dsl = """
|FG|  |  |CT|WT|NO|
|FG|  |  |CT|NO|NO|
|NO|  |NO|NO|CT|NO|
|CT|  |  |CT|NO|FG|
|ST|DT|MT|NO|NO|NO|
"""


def validate_dsl(dsl):
    if dsl.count("|WT|") != 1:
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


start_tile_location = None


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
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = row_index, col_index

            row.append(tile_type(row_index, col_index) if tile_type else None)

        world_map.append(row)


tile_dictionary = {"ST": StartTile,
                   "WT": WinTile,
                   "NO": NothingTile,
                   "CT": ChallengeTile,
                   "MT": MerchantTile,
                   "FG": FindGoldTile,
                   "DT": DarkTile,
                   "  ": None
                   }


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    elif y < len(world_map) and x < len(world_map[y]):
        return world_map[y][x]
