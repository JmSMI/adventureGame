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
            print("You have " + str(max(0, player.hp)) + "HP remaining.")

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
        return """You stand at the entrance of a cave."""

    def __init__(self, x, y):
        super().__init__(x, y)


class EmptyTile(MapTile):
    def show_text(self):
        pass

    def __init__(self, x, y):
        super().__init__(x, y)


class EndTile(MapTile):
    def show_text(self):
        return """You walk out of the maze"""

    def __init__(self, x, y):
        super().__init__(x, y)


world_map = [
    [None, EndTile(1, 0), None],
    [None, EmptyTile(1, 2), None],
    [EnemyTile(0, 2), StartTile(1, 2), None],
    [None, EmptyTile(1, 3), None], ]


def tile_at(x, y):
    if x < 0 or y < 0:
        raise IndexError("Coordinates do not exist in world map")
    elif x < len(world_map) and y < len(world_map[x]):
        return world_map[y][x]
