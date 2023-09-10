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
        self.hp = 6
        self.defeated = False
        self.damage = 12
        self.attack_text = '''
A bat swoops down and attacks
'''
        self.death_text = '''
The bat flies away
'''
        self.intro_text = '''
A colony of bats hangs from the ceiling
'''


class Rabbit(Enemy):
    def __init__(self):
        self.name = "Rabbit"
        self.hp = 5
        self.defeated = False
        self.damage = 4
        self.attack_text = '''
The rabbit darts forward with lightning speed, 
delivering a swift nibble before darting away.
'''
        self.death_text = '''
With a graceful leap, the rabbit disappears into the underbrush,
leaving a sense of fleeting wonder
'''
        self.intro_text = '''
A curious rabbit nibbles on some vegetation nearby, 
its innocence a comforting presence amidst the mystery
'''


class Dragon(Enemy):
    def __init__(self):
        self.name = "Dragon"
        self.hp = 100
        self.defeated = False
        self.damage = 60
        self.attack_text = '''
A dragon's fiery breath engulfs you, 
scorching the ground and the air around you
'''
        self.death_text = '''
The mighty dragon collapses, its scales 
cooling into an immense, lifeless beast
'''
        self.intro_text = '''
A colossal dragon guards its hoard, its 
eyes gleaming with avarice
'''


class Troll(Enemy):
    def __init__(self):
        self.name = "Troll"
        self.hp = 10
        self.defeated = False
        self.damage = 25
        self.attack_text = '''
A massive troll swings a tree trunk-sized club, 
the ground trembling with each blow
'''
        self.death_text = '''
The troll roars in agony, its gargantuan frame 
crashing down in a cloud of dust
'''
        self.intro_text = '''
A towering troll guards the cavern entrance, 
its brutish demeanor evident
'''


class Goblin(Enemy):
    def __init__(self):
        self.name = "Goblin"
        self.hp = 8
        self.defeated = False
        self.damage = 8
        self.attack_text = '''
The mischievous goblin brandishes a stolen 
dagger, aiming for your guts
'''
        self.death_text = '''
The goblin lets out a final, spiteful 
laugh before collapsing in defeat
'''
        self.intro_text = '''
A goblins scampers around the corner, its beady eyes fixated on you
'''


class Ghost(Enemy):
    def __init__(self):
        self.name = "Ghost"
        self.hp = 10
        self.defeated = False
        self.damage = 40
        self.attack_text = '''
The ghost envelops you in a chilling ethereal grasp, 
draining your warmth
'''
        self.death_text = '''
With a whisper, the ghost fades into the void, 
leaving behind a lingering coldness
'''
        self.intro_text = '''
An eerie figure materializes before you, 
its translucent form radiating an otherworldly presence
'''
