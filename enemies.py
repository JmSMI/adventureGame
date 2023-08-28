class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create Enemy objects")

    #def __str__(self):
     #   return self.name

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 30
        self.damage = 10


class AntColony(Enemy):
    def __init__(self):
        self.name = "Ant Colony"
        self.hp = 20
        self.damage = 5


class Scorpion(Enemy):
    def __init__(self):
        self.name = "Scorpion"
        self.hp = 35
        self.damage = 20


class Ogre(Enemy):
    def __init__(self):
        self.name = "Ogre"
        self.hp = 35
        self.damage = 20
