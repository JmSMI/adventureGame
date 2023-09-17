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
    print("welcome to ESCAPE")
    print("release 0.2")
    print("find the end:\n")

    while True:
        room = world.tile_at(player.x, player.y)
        player.enableMovement = True

        # Only show enemy text when Enemy is alive
        if isinstance(room, world.ChallengeTile) and room.enemy.defeated:
            pass
        else:
            room.modify_player(player)
            print(room.show_text())

        # Show a different encounter text on the second turn with an Enemy
        room.encounter_counter()

        if not player.is_alive():
            print()
            print("you are defeated.")
            print()
            return
        if isinstance(room, world.WinTile):
            print()
            print("the end")
            print()
            return

        choose_action(room, player)


global move_history
move_history = []


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("...?\n").lower()
        action = available_actions.get(action_input)
        if action:
            player.action_history.append(action_input)
            action()
        else:
            print("\nyou think for a moment, and then...")
            return


def get_available_actions(room, player):
    last_move = player.get_last_move()
    actions = OrderedDict()
    print("...")
    print("choose an action")
    print(f"{player.hp} / {Player.max_hp} HP | weapon: {player.equipped_weapon} | "
          f"food: {player.equipped_food}")
    # todo allow the player to leave the darkTile and regain movement
    # movement should only be disabled when player in dark tile
    # and no torch equipped
    # currently, they'll walk into DT, then lose movement and
    # only be able to make the last move. Even the case when
    # reentering the DT with torch equippped!!
    if player.inventory:
        action_adder(actions, 'i', player.browse_inventory, "open inventory")
    if world.tile_at(player.x, player.y + 1) and player.enableMovement:
        action_adder(actions, 's', player.move_south, "move south")
    if world.tile_at(player.x, player.y - 1) and player.enableMovement:
        action_adder(actions, 'n', player.move_north, "move north")
    if world.tile_at(player.x + 1, player.y) and player.enableMovement:
        action_adder(actions, 'e', player.move_east, "move east")
    if world.tile_at(player.x - 1, player.y) and player.enableMovement:
        action_adder(actions, 'w', player.move_west, "move west")
    if not player.enableMovement:
        if last_move == 'e':
            action_adder(actions, 'w', player.move_west, "move west")
        elif last_move == 's':
            action_adder(actions, 'n', player.move_north, "move north")
        elif last_move == 'w':
            action_adder(actions, 'e', player.move_east, "move east")
        elif last_move == 'n':
            action_adder(actions, 's', player.move_south, "move south")
    if player.hp < Player.max_hp:
        action_adder(actions, 'h', player.heal, "heal")
    if isinstance(room, world.ChallengeTile) and room.enemy.is_alive() and not room.enemy.defeated:
        action_adder(actions, 'a', player.attack, "attack")
    if isinstance(room, world.MerchantTile):
        room.trader.interact(player)
        action_adder(actions, 't', room.trader.trade, "trade")
    return actions


def action_adder(dictionary, key, value, message):
    dictionary[key] = value
    print(f"({key}) {message}")


play()
