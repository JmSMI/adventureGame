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
                          'Gold(5)', items.FreshBread(), items.OldBread()]
        self.hp = 100
        self.x = 1
        self.y = 2
        self.max_hp = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.y -= 1

    def move_south(self):
        self.y += 1

    def move_east(self):
        self.x += 1

    def move_west(self):
        self.x -= 1

    def attack(self):
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy

        best_weapon = self.most_powerful_weapon()
        enemy.hp -= best_weapon.damage

        print("You use {}({}) against {}!".format(best_weapon.name, best_weapon.damage, enemy.name))

        if not enemy.is_alive():
            print("You destroyed " + enemy.name)
        else:
            print("{} has {} HP remaining.".format(enemy.name, enemy.hp))

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]

        if not consumables:
            print("You have no items to heal with")
            return

        print("What do you want to heal with?")
        for index, value in enumerate(consumables, 1):
            print(str(index) + ".", value)

        valid = False
        while not valid:
            choice = input("")
            try:
                food = consumables[int(choice) - 1]
                if self.hp == self.max_hp:
                    print("You already have full health.")
                    return
                self.hp = min(self.max_hp, self.hp + food.healing_value)
                self.inventory.remove(food)
                print("You healed " + str(food.healing_value) + " HP. You have " + str(
                    self.hp) + " HP")
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice. Try again.")

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

    def print_health(self):
        print(f"You have {self.hp} HP.")

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"* {str(item)}")

        best_weapon = self.most_powerful_weapon()
        print("Your most powerful weapon is a " + str(best_weapon))
