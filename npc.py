import items


class NPC:
    def __init__(self):
        raise NotImplementedError("Don't create objects from this class")

    def __str__(self):
        return self.name

    def interact(self):
        pass


class Trader(NPC):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.Stick(), items.HealingPotion(), items.RoyalSword()]
