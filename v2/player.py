import items
import world


class Player:
    max_hp = 100

    def __init__(self):
        gold = items.Gold()
        gold.deposit(5)
        self.inventory = [items.Sword(), items.Bread(), items.Torch(),
                          gold]
        self.hp = Player.max_hp
        self.equipped_weapon = None
        self.equipped_food = None
        self.x = 1
        self.y = 2

    def show_inventory(self):
        '''
        Displays the player inventory to the console.
        Equipped items are labelled and can be used for
        healing, attacking, etc.
        '''
        for i, item in enumerate(self.inventory, 1):
            if item == self.equipped_food:
                print(f"{i}. {item} (equipped)")
            elif item == self.equipped_weapon:
                print(f"{i}. {item} (equipped)")
            else:
                print(f"{i}. {item}")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(0, -1)

    def move_south(self):
        self.move(0, 1)

    def move_west(self):
        self.move(-1, 0)

    def move_east(self):
        self.move(1, 0)

    def browse_inventory(self):
        print(f"Health: {self.hp} HP")
        self.show_inventory()
        print("-----------")
        print("Go (b)ack")
        print("Select item to view details")

        while True:
            choice = input().lower()
            if choice == 'b':
                return
            else:
                try:
                    print(self.inventory[int(choice) - 1].description)
                    self.show_inventory()
                except ValueError:
                    self.show_inventory()
                except IndexError:
                    self.show_inventory()

    def choose_weapon(self):
        '''
        Prompt the player to equip a weapon from their inventory.
        Prompts the player to equip a different weapon if one
        is already equipped.
        '''
        weapons = []
        weapon_counter = 0
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                weapons.append(item)
                weapon_counter += 1
                print(f"{weapon_counter}. {item}")
        choosing = True
        while choosing:
            choice = input("Select a weapon to equip: ")
            try:
                self.equipped_weapon = weapons[int(choice) - 1]
                print("You equipped the " + str(self.equipped_weapon))
                choosing = False
            except ValueError:
                print()
            except IndexError:
                print()

    def attack(self):
        """
        Allows the player to attack an enemy using
        their equipped weapon
        """
        if not self.equipped_weapon:
            print("You don't have a weapon equipped. ")
            self.choose_weapon()

        room = world.tile_at(self.x, self.y)
        if isinstance(room, world.EnemyTile):
            enemy = room.enemy
        else:
            print("There's nothing to attack.")
            return
        if not enemy.is_alive():
            print("The enemy isn't a threat.")
            return
        else:
            print(f"You attack using a {str(self.equipped_weapon)} "
                  f"dealing {self.equipped_weapon.damage} damage")
            enemy.hp -= self.equipped_weapon.damage

    def heal(self):
        """
        Allows the player to heal using their equipped
        consumable.
        """
        healed = False
        while not healed:
            if self.equipped_food:
                print("Heal using " + str(self.equipped_food) + "?")
                heal_choice = input("y/n? ").lower()
                if heal_choice == 'y' and self.hp < Player.max_hp:
                    self.hp += self.equipped_food.hp
                    self.equipped_food = None
                    print("Consumed ... to heal ... HP")
                    healed = True
                elif heal_choice == 'y' and self.hp >= Player.max_hp:
                    print("You already have max hp")
                    return
                elif heal_choice == 'n':
                    return
            elif not self.equipped_food:
                self.choose_consumable()

    def choose_consumable(self):
        """
        Prompts the player to equip a Consumable from their
        inventory
        """
        consumables = []
        consumables_counter = 0
        for item in self.inventory:
            if isinstance(item, items.Consumable):
                consumables.append(item)
                consumables_counter += 1
                print(f"{consumables_counter}. {item}")
        choosing = True
        while choosing:
            choice = input("Select a food to equip: ")
            try:
                self.equipped_food = consumables[int(choice) - 1]
                print("You equipped " + str(self.equipped_food))
                choosing = False
            except ValueError:
                print()
            except IndexError:
                print()
