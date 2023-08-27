from player import Player
import world
from collections import OrderedDict


# Describes the state of the game. Allows the player to
# move around the map
def play():
    world.parse_world_dsf()
    player = Player()

    print("Escape from Cave Terror!")
    print()

    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        choose_action(room, player)
        room.modify_player(player)


def get_available_actions(room, player):
    actions = OrderedDict()
    if player.inventory:
        action_adder(actions, "i", player.print_inventory, "Inventory")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
    if world.tile_at(player.x, player.y - 1):
        action_adder(actions, "n", player.move_north, "Move North")
    if world.tile_at(player.x, player.y + 1):
        action_adder(actions, "s", player.move_south, "Move South")
    if world.tile_at(player.x + 1, player.y):
        action_adder(actions, "e", player.move_east, "Move East")
    if world.tile_at(player.x - 1, player.y):
        action_adder(actions, "w", player.move_west, "Move West")
    if player.hp < player.max_hp:
        action_adder(actions, "h", player.heal, "Heal")

    return actions


def action_adder(dictionary, hotkey, action, message):
    dictionary[hotkey] = action
    print(hotkey + ": " + message)


def choose_action(room, player):
    print("Choose an action: ")
    action = None
    while not action:
        possible_actions = get_available_actions(room, player)
        choice = input("Action: ").lower()
        action = possible_actions.get(choice)
        if action:
            action()
        else:
            print("Invalid action")


play()
