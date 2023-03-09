from random import randint


# establish number of pencils in game
# returns number of pencils in the pot
def pick_starting_pencils():
    print("How many pencils would you like to use:")

    while True:
        try:
            pencil_count = int(input())
        except ValueError:
            print("The number of pencils should be numeric")
            continue

        if pencil_count < 0:
            print("The number of pencils should be numeric")  # This was a project requirement
            continue

        if pencil_count == 0:
            print("The number of pencils should be positive")
            continue
        else:
            return pencil_count


# query which player should go first
# return initial 'active_player'
def pick_starting_player():
    players = ["Jack", "John"]  # Jack is the name of the AI player

    print("Who will be the first (John, Jack):")

    while True:
        starting_player = input()

        if starting_player not in players:
            print(f"Choose between Jack and John")
        else:
            return starting_player


# switch players
# returns name of active player
def player_switcher(player):
    if player == "Jack":
        return "John"
    else:
        return "Jack"


# AI turn
# returns number of pencils removed
def jack_turn(pencil_count):
    print("|" * pencil_count)
    print("Jack's turn:")

    losing_positions = range(1, (pencil_count + 1), 4)
    if pencil_count not in losing_positions:
        for position in losing_positions:
            if position + 1 == pencil_count:
                print(1)
                return 1
            elif position + 2 == pencil_count:
                print(2)
                return 2
            elif position + 3 == pencil_count:
                print(3)
                return 3
    else:
        if pencil_count == 1:
            print(1)
            return 1
        else:
            taken = randint(1, 3)
            print(taken)
            return taken


# Human turn
# returns number of pencils removed
def john_turn(pencil_count):
    print("|" * pencil_count)
    print("John's turn!")

    while True:
        remove_count = input()
        valid_answer = ["1", "2", "3"]

        if remove_count in valid_answer:
            if int(remove_count) <= pencil_count:
                return int(remove_count)
            else:
                print("Too many pencils were taken")
                continue
        else:
            print("Possible values: '1', '2' or '3'")
            continue


# play the game
pencils = pick_starting_pencils()  # Global
active_player = pick_starting_player()  # Global

while True:
    if pencils > 0:
        if active_player == "Jack":
            pencils -= jack_turn(pencils)
            active_player = player_switcher(active_player)
        else:
            pencils -= john_turn(pencils)
            active_player = player_switcher(active_player)
    else:
        print(f"{active_player} won!")
        break
