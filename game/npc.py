import items


class NonPlayableCharacter():
    def __init__(self):
        self.name = None
        raise NotImplementedError("Not implemented")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.human = None
        self.name = "Trader"
        self.swaps = 0
        self.hp = 25
        self.gold = items.Gold(20)
        self.inventory = [items.Sword(15, 8), items.Bread(), items.HealingPotion()]

    def interact(self, human):
        if not self.human:
            self.human = human

    def trade(self):
        if not self.human:
            raise ValueError("Pass me a player to interact with.")
        print("\n--MERCHANT--")
        print("(b) buy")
        print("(s) sell")
        print("(z) go back")
        while True:
            choice = input().lower()
            if choice == 'z':
                return
            elif choice == 'b' or choice == 'buy':
                print("have a look at what i have")
                self.buy(self.human)
            elif choice == 's':
                print("what have you got?")
                self.sell(self.human)
            else:
                print("do you want to buy or sell?")

    def sell(self, player):
        """
        Allows a player sell items from their inventory.

        :param player: The player that will be interacting with this merchant
        """
        for index, item in enumerate(player.inventory, 1):
            print(f"{index}. {item} ({item.value} gold)")
        print("(z) go back")

        choice = input().lower()
        while True:
            if choice == 'z':
                return
            try:
                thing = player.inventory[int(choice) - 1]
                if self.gold.get_balance() < thing.value:
                    print("i don't have enough gold to buy that from you\n")
                    return
                self.inventory.append(thing)
                self.gold.withdraw(thing.value)

                player.gold.deposit(thing.value)
                player.inventory.remove(thing)
                print(f"you removed {thing} to your inventory\n")
                return
            except IndexError:
                pass
            except ValueError:
                pass

    def buy(self, player):
        """
        Allows the player to buy items from the shop's inventory.

        :param player: The player object making the purchase.
        :return: None
        """
        for index, item in enumerate(self.inventory, 1):
            print(f"{index}. {item} ({item.value} gold)")
        print("(z) go back")

        choice = input().lower()
        while True:
            if choice == 'z':
                return
            try:
                thing = self.inventory[int(choice) - 1]
                if player.gold.get_balance() < thing.value:
                    print("you don't have enough gold to buy that from me\n")
                    return
                player.inventory.append(thing)
                player.gold.withdraw(thing.value)

                self.gold.deposit(thing.value)
                self.inventory.remove(thing)
                print(f"you added {thing} to your inventory\n")
                return
            except IndexError:
                pass
            except ValueError:
                pass
