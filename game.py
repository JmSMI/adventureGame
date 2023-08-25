from player import Player
import world


# Describes the state of the game. Allows the player to
# move around the map
def play():
    player = Player()

    print("Escape from Cave Terror!")
    print()
    print("Controls".center(30))
    print("i: Inventory")
    print("n: Move North one block")
    print("s: Move South one block")
    print("w: Move West one block")
    print("e: Move East one block")
    print("a: Attack")

    room = world.tile_at(player.x, player.y)
    print(room.intro_text())

    while True:

        action_input = get_player_command()
        if action_input == 'n':
            print("Go North!")

            player.move(0, -1)
            room = world.tile_at(player.x, player.y)
            print(room.intro_text())
            # Check position
            print(f"{player.x} {player.y}")

        elif action_input == 'w':
            print("Go West!")

            player.move(-1, 0)
            room = world.tile_at(player.x, player.y)
            print(room.intro_text())
        elif action_input == 'e':
            print("Go East!")

            player.move(1, 0)
            room = world.tile_at(player.x, player.y)
            print(room.intro_text())
        elif action_input == 's':
            print("Go South!")

            player.move(0, 1)
            room = world.tile_at(player.x, player.y)
            print(room.intro_text())
        elif action_input == 'i':
            player.print_inventory()
            player.print_health()
        elif action_input == 'a':
            player.attack()
            room.modify_player(player)
        elif action_input == 'h':
            player.heal()
        else:
            print("Invalid input.")


def get_player_command():
    return input('Action: ')


play()
