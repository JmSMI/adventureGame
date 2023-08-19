import items
import world

# Defines the player inventory and starting location.
# The player always has a position, and the world
# knows what tiles are in what position. Game is controller between
# the player and the world.
class Player:
    # player starts off with an inventory
    def __init__(self):
        self.inventory = [items.Stick(), items.Rock(),
                          'Gold(5)', 'Fresh Bread', 'Old Bread']
        self.hp = 100
        self.x = 1
        self.y = 2

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        enemy.hp -= best_weapon.damage

        print("You use {}:{} against {}!".format(best_weapon.name, best_weapon.damage, enemy.name))

        if not enemy.is_alive():
            print("You destroyed " + enemy.name)
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    max_damage = item.damage
                    best_weapon = item
            except AttributeError:
                pass

        return best_weapon

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"* {str(item)}")

        best_weapon = self.most_powerful_weapon()
        print("Your most powerful weapon is: " + str(best_weapon))
