# Describes the items in the game. Each item is a class or subclass
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create Weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist sized rock, suitable for attacking."
        self.damage = 5
        self.value = 5


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger."
        self.damage = 10
        self.value = 20


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "A rusty sword. " \
                           "It doesn't look very sharp, but it's heavy."
        self.damage = 20
        self.value = 80


class RoyalSword(Weapon):
    def __init__(self):
        self.name = "Royal Sword"
        self.description = "A sharp sword used by the castle army. "
        self.damage = 50
        self.value = 150


class Stick(Weapon):
    def __init__(self):
        self.name = "Stick"
        self.description = "A small branch useful for whacking things."
        self.damage = 5
        self.value = 5


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create Consumable objects.")

    def __str__(self):
        return f"{self.name} (+{self.healing_value}HP)"


class FreshBread(Consumable):
    def __init__(self):
        self.name = "Fresh Bread"
        self.healing_value = 50
        self.value = 20


class OldBread(Consumable):
    def __init__(self):
        self.name = "Old Bread"
        self.healing_value = 25
        self.value = 10


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 75
        self.value = 50
