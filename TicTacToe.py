import os

clear = lambda: os.system("cls")

current_player = " X "
game_status = ["(0)", "(1)", "(2)", "(3)", "(4)", "(5)", "(6)", "(7)", "(8)"]
winning_conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]
have_won = False


def display_screen():
    clear()
    print("---------------")
    print(f"{game_status[0]} | {game_status[1]} | {game_status[2]}")
    print(f"{game_status[3]} | {game_status[4]} | {game_status[5]}")
    print(f"{game_status[6]} | {game_status[7]} | {game_status[8]}")
    print("---------------")


def place_cell(cell):
    global current_player
    global game_status
    global winning_conditions
    global have_won

    game_status[cell] = f"{current_player}"
    for winning_condition in winning_conditions:
        if (
            game_status[winning_condition[0]] == current_player
            and game_status[winning_condition[1]] == current_player
            and game_status[winning_condition[2]] == current_player
        ):
            display_screen()
            print(f'WINNER!: Player {"1" if current_player == " X " else "2"}')
            have_won = True

    current_player = " O " if current_player == " X " else " X "


while not have_won:
    display_screen()
    while True:
        try:
            selected_cell = int(input(f"Select a cell to place (): "))

            # if invalid / already taken
            if (selected_cell > 8 or selected_cell < 0) or (
                game_status[selected_cell] == " X "
                or game_status[selected_cell] == " O "
            ):
                display_screen()
                continue

        except:
            display_screen()
            continue
        else:
            break
    place_cell(selected_cell)
