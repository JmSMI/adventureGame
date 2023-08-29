import items
from player import Player
import world


def play():
    player = Player()
    print("Escape the maze")
    print("Type (help) to show controls: ")
    tutorial = input().lower()
    print()
    if tutorial == 'help':
        show_controls()
    while True:
        room = world.tile_at(player.x, player.y)
        room.modify_player(player)
        # Only show enemy text when Enemy is alive
        if isinstance(room, world.EnemyTile) and room.enemy.defeated:
            pass
        else:
            print(room.show_text())

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
        elif action_input == 'l':  # display location for troubleshooting map
            print(player.x)
            print(player.y)
        else:
            print("Invalid choice")


def show_controls():
    print("-------------")
    print('n/w/s/e: move'
          '\na: attack'
          '\nc: choose weapon'
          '\ni: inventory'
          '\nh: heal')


def show_help():
    print("Try to make your way out of the maze.")
    show_controls()


play()
