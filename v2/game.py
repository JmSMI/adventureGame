import items
from player import Player
import world
from collections import OrderedDict


def play():
    player = Player()

    print("Escape the maze")

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

        if player.hp <= 0:
            print()
            print("You are defeated.")
            print()
            return

        choose_action(room, player)


def show_controls():
    print("-------------")
    print('n/w/s/e: move'
          '\na: attack'
          '\nc: choose weapon'
          '\ni: inventory'
          '\nh: heal')


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action")
    if player.inventory:
        action_adder(actions, 'i', player.open_inventory, "Show inventory")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive() and not room.enemy.defeated:
        action_adder(actions, 'a', player.attack, "Attack")
    if world.tile_at(player.x, player.y + 1):
        action_adder(actions, 's', player.move_south, "Move south")
    if world.tile_at(player.x, player.y - 1):
        action_adder(actions, 'n', player.move_north, "Move north")
    if world.tile_at(player.x + 1, player.y):
        action_adder(actions, 'e', player.move_east, "Move east")
    if world.tile_at(player.x - 1, player.y):
        action_adder(actions, 'w', player.move_west, "Move west")
    if player.hp < Player.max_hp:
        action_adder(actions, 'h', player.heal, "Heal")
    return actions


def action_adder(dictionary, key, value, message):
    dictionary[key] = value
    print(key + ": " + message)


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ").lower()
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("You can't do that.")


def show_help():
    print("Try to make your way through the cave.")
    show_controls()


play()
