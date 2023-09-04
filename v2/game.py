import items
from player import Player
import world


def play():
    player = Player()
    god_mode = False

    print("Escape the maze")
    show_controls()
    while True:
        room = world.tile_at(player.x, player.y)

        # Only show enemy text when Enemy is alive
        if isinstance(room, world.EnemyTile) and room.enemy.defeated:
            pass
        else:
            print(room.show_text())
        room.modify_player(player)
        if player.hp <= 0:
            print()
            print("You are defeated.")
            print()
            return
        # Show a different encounter text on the second turn with an Enemy
        room.encounter_counter()
        action_input = input("Choose an action: ").lower()
        if action_input == 'n':
            print("north")
            player.move_north()
        elif action_input == 's':
            print("south")
            player.move_south()
        elif action_input == 'w':
            print("west")
            player.move_west()
        elif action_input == 'e':
            print("east")
            player.move_east()
        elif action_input == 'c':
            print("choose weapon")
            player.choose_weapon()
        elif action_input == 'i':
            player.browse_inventory()
        elif action_input == 'a':
            player.attack()
        elif action_input == 'h':
            player.heal()
        elif action_input == 'help':
            show_help()
        elif action_input == 'qwerty':
            if god_mode == False:
                print("God mode enabled!!")
                print("500 player HP, 200 sword damage")
                player.hp = 500
                for items.Sword in player.inventory:
                    items.Sword.damage = 200
                god_mode = not god_mode
            else:
                print("God mode disabled!!")
                player.hp = Player.max_hp
                for item in [x for x in player.inventory if type(x) == items.Sword]:
                    item.damage = items.Sword.sword_damage
                god_mode = not god_mode
        elif action_input == 'l':  # display location for troubleshooting map
            print(player.x)
            print(player.y)
        else:
            print("You stare ahead blankly.")


def show_controls():
    print("-------------")
    print('n/w/s/e: move'
          '\na: attack'
          '\nc: choose weapon'
          '\ni: inventory'
          '\nh: heal')


def show_help():
    print("Try to make your way through the cave.")
    show_controls()


play()
