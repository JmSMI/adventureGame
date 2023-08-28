import items
from player import Player

def play():
    print("Escape from a text adventure")
    print('n/w/s/e: move, a: attack, c: choose weapon, \n' 
          'i: inventory, h: heal')

    player = Player()

    while True:
        player.hp = 100
        action_input = input("Choose an action: ").lower()
        if action_input == 'n':
            print("North")
        elif action_input == 's':
            print("south")
        elif action_input == 'w':
            print("west")
        elif action_input == 'e':
            print("east")
        elif action_input == 'c':
            print("choose weapon")
            player.choose_weapon()
        elif action_input == 'i':
            player.show_inventory()
        elif action_input == 'a':
            player.attack()
        elif action_input == 'h':
            player.heal()
        else:
            print("Invalid choice")


play()
