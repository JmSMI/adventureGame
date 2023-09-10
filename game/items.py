# durability?

class Weapon:
    def __init__(self):
        self.name = None
        self.description = None
        raise NotImplementedError("Not implemented")

    def __str__(self):
        return self.name


class Sword(Weapon):
    def __init__(self, damage, value):
        if damage <= 0 or value <= 0:
            raise ValueError("Damage or value can't be zero.")
        self.damage = damage
        self.value = value
        self.name = "sword"
        self.description = "a shiny sword you can use to chop things."


class Torch(Weapon):
    def __init__(self):
        self.damage = 2
        self.value = 5
        self.name = "torch"
        self.description = "a torch to light the way. it's not very useful."


class Knife(Weapon):
    def __init__(self, damage):
        self.damage = damage
        self.value = 5
        self.name = "knife"
        self.description = "a small pocket knife."


class Consumable:
    def __init__(self):
        self.name = None
        self.description = None
        raise NotImplementedError("Not implemented")

    def __str__(self):
        return self.name


class Bread(Consumable):
    def __init__(self):
        self.hp = 25
        self.value = 1
        self.name = "bread"
        self.description = "a fresh chunk of bread. heals " + str(self.hp) + "HP"


class HealingPotion(Consumable):
    def __init__(self):
        self.hp = 75
        self.value = 5
        self.name = "potion"
        self.description = "a potent healing potion. heals " + str(self.hp) + "HP"


class Currency:
    def __init__(self):
        self.quantity = None
        self.name = None
        raise NotImplementedError("Not implemented")

    def __str__(self):
        return self.name + " (" + str(self.quantity) + ")"

    def deposit(self, amount):
        self.quantity += amount

    def withdraw(self, amount):
        self.quantity -= amount

    def get_balance(self):
        return self.quantity


class Gold(Currency):
    def __init__(self, quantity):
        self.quantity = quantity
        self.name = "gold"
        self.description = "some gold coins. exchange them with a merchant to buy things."
