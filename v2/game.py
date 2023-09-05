import items
from player import Player
import world
from collections import OrderedDict


def play():
    player = Player()
    world.parse_dsl(world.world_dsl)
    player.x = world.start_tile_location[0]
    player.y = world.start_tile_location[1]
    print('''
@@@@@@@@@@@@@@@@@@  @@@@@@@@@@
@@  @@  @@      @@          @@
@@  @@  @@  @@  @@  @@@@@@  @@
@@  @@      @@      @@      @@
@@  @@@@@@@@@@@@@@@@@@  @@@@@@
@@      @@          @@  @@  @@
@@  @@  @@@@@@@@@@  @@  @@  @@
@@  @@              @@      @@
@@  @@@@@@@@@@  @@@@@@@@@@  @@
@@  @@      @@  @@          @@
@@  @@  @@  @@@@@@  @@@@@@@@@@
@@  @@  @@  @@      @@      @@
@@  @@  @@  @@  @@@@@@  @@  @@
@@      @@              @@  @@
    ''')
    print("welcome to ESCAPE THE MAZE")
    print("release 0.2")
    print("navigate your way through to the other side:\n")


    while True:
        room = world.tile_at(player.x, player.y)

        # Only show enemy text when Enemy is alive
        if isinstance(room, world.EnemyTile) and room.enemy.defeated:
            pass
        else:
            print(room.show_text())

        room.modify_player(player)
        # Show a different encounter text on the second turn with an Enemy
        room.encounter_counter()

        if not player.is_alive():
            print()
            print("you are defeated.")
            print()
            return

        choose_action(room, player)


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("...?").lower()
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("\nyou think for a moment, and then...")
            return


def get_available_actions(room, player):
    actions = OrderedDict()
    print("-----------------------------------------------")
    print(f"\n{player.hp} / {Player.max_hp} HP ")
    print("choose an action")
    if player.inventory:
        action_adder(actions, 'i', player.browse_inventory, "open inventory")
    if world.tile_at(player.x, player.y + 1):
        action_adder(actions, 's', player.move_south, "move south")
    if world.tile_at(player.x, player.y - 1):
        action_adder(actions, 'n', player.move_north, "move north")
    if world.tile_at(player.x + 1, player.y):
        action_adder(actions, 'e', player.move_east, "move east")
    if world.tile_at(player.x - 1, player.y):
        action_adder(actions, 'w', player.move_west, "move west")
    if player.hp < Player.max_hp:
        action_adder(actions, 'h', player.heal, "heal")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive() and not room.enemy.defeated:
        action_adder(actions, 'a', player.attack, "attack")
    if isinstance(room, world.TraderTile):
        room.trader.interact(player)
        action_adder(actions, 't', room.trader.trade, "trade")
    return actions


#

def action_adder(dictionary, key, value, message):
    dictionary[key] = value
    print(f"({key}) {message}")


play()
