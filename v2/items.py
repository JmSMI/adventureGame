# durability?

class Weapon:
    def __init__(self):
        self.name = None
        self.description = None
        raise NotImplementedError("Not implemented")

    def __str__(self):
        return self.name


class Sword(Weapon):
    def __init__(self):
        self.damage = 10
        self.value = 5
        self.name = "Sword"
        self.description = "A shiny sword you can use to chop things."


class Torch(Weapon):
    def __init__(self):
        self.damage = 2
        self.value = 5
        self.name = "Torch"
        self.description = "A torch to light the way."


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
        self.name = "Bread"
        self.description = "A fresh chunk of bread."


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


class Gold(Currency):
    def __init__(self):
        self.name = "Gold"
        self.quantity = 0
        self.description = "Gold coins"



