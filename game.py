import npc
from player import Player
import world
from collections import OrderedDict


# Describes the state of the game. Allows the player to
# move around the map
def play():
    print("Escape from Cave Terror!")

    world.parse_world_dsl()
    player = Player()

    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print()
        print(room.intro_text())
        room.modify_player(player)

        if player.is_alive() and not player.victory:
            choose_action(room, player)
        else:
            print("Your journey has come to an end!")

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
    if isinstance(room, world.TraderTile):
        action_adder(actions, "t", player.trade, "Interact with NPC")
    if player.hp < player.max_hp:
        action_adder(actions, "h", player.heal, "Heal")
    return actions


def action_adder(dictionary, hotkey, action, message):
    dictionary[hotkey] = action
    print(hotkey + ": " + message)


def choose_action(room, player):
    print()
    print("What do you want to do? ")
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
