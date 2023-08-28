class Weapon:
    def __init__(self):
        self.name = None
        raise NotImplementedError("Not implemented")

    def __str__(self):
        return self.name


class Sword(Weapon):
    def __init__(self):
        self.damage = 10
        self.value = 5
        self.name = "Sword"


class Torch(Weapon):
    def __init__(self):
        self.damage = 2
        self.value = 5
        self.name = "Torch"


class Consumable:
    def __init__(self):
        self.name = None
        raise NotImplementedError("Not implemented")

    def __str__(self):
        return self.name


class Bread(Consumable):
    def __init__(self):
        self.hp = 25
        self.value = 1
        self.name = "Bread"
