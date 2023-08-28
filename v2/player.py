import items


class Player:
    max_hp = 100

    def __init__(self):
        self.inventory = [items.Sword(), items.Bread(), items.Torch()]
        self.hp = Player.max_hp
        self.equipped_weapon = None
        self.equipped_food = None
        self.gold = 3

    def show_inventory(self):
        for i, item in enumerate(self.inventory, 1):
            if item == self.equipped_food:
                print(f"{i}. {item} (equipped)")
            elif item == self.equipped_weapon:
                print(f"{i}. {item} (equipped)")
            else:
                print(f"{i}. {item}")

        print(f"{len(self.inventory) + 1}. Gold ({self.gold})")


    # List all weapons and allow the player to choose one.
    # Selected weapon is set as the equipped item
    # and a message is displayed to the player
    def choose_weapon(self):
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
        if not self.equipped_weapon:
            print("You don't have a weapon equipped. ")
            self.choose_weapon()
        print("Attack using " + str(self.equipped_weapon))

    def heal(self):
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
