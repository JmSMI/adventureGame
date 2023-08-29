class Enemy:
    def __init__(self):
        # attribute for 'aggression' that is random? higher
        # aggression results in enemy attack more likely in 0th encounter
        self.hp = 0
        raise NotImplementedError("Not implemented")

    def is_alive(self):
        return self.hp > 0


class Bat(Enemy):
    def __init__(self):
        self.name = "Bat"
        self.defeated = False
        self.hp = 6
        self.damage = 10
        self.attack_text = '''A bat swoops down and attacks'''
        self.death_text = '''The bat flies away'''
        self.intro_text = '''A colony of bats hangs from the ceiling'''
