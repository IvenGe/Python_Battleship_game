import copy


def create_board(width, board):
    for row_index in range(width):
        board.append([])
        for column_index in range(width):
            board[row_index].append(None)

    return board.copy()


def place_symbol(row, column, symbol, player, board):  # unsafe :(
    board[player][row][column] = symbol


def place_pawn(row, column, pawn, player, rotation, stats):
    if check_if_pawn_place_is_valid(row, column, pawn, player, rotation, stats):
        if rotation == '_':
            for i in range(stats[player][pawn].get("Size")):
                place_symbol(row + i, column, stats[player][pawn].get("Symbol"), player, play_boards)
            stats[player][pawn]["Amount"] -= 1
        else:
            for i in range(stats[player][pawn].get("Size")):
                place_symbol(row, column + i, stats[player][pawn].get("Symbol"), player, play_boards)
            stats[player][pawn]["Amount"] -= 1
    else:
        print("You cant place this pawn here or you dont have that pawn left!")


def check_if_pawn_place_is_valid(row, column, pawn, player, rotation, stats):
    print(column + stats[player][pawn].get("Size") - WIDTH)
    if (stats[player][pawn].get("Amount") > 0 and WIDTH > (
            WIDTH - (row + stats[player][pawn].get("Size"))) > 0) and rotation == '_':

        return not check_if_something_is_already_in_use(row, column, pawn, player, rotation, stats)

    elif (stats[player][pawn].get("Amount") > 0 and WIDTH > (
            WIDTH - (column + stats[player][pawn].get("Size"))) > 0) and rotation == '|':
        return not check_if_something_is_already_in_use(row, column, pawn, player, rotation, stats)

    else:
        return False


def check_if_something_is_already_in_use(row, column, pawn, player, rotation, stats):
    if rotation == '_':
        for i in range(stats[player][pawn].get("Size")):
            if play_boards[player][row + i][column] is not None:
                return True
    if rotation == '|':
        for i in range(stats[player][pawn].get("Size")):
            if play_boards[player + i][row][column] is not None:
                return True
    return False


def switch_turn(turn=None):
    if turn == 1:
        turn = 2
    else:
        turn = 1
    return turn


def get_all_pawns_in_text(pawns):
    text = ""
    for pawn in pawns.keys():
        text += str(pawns[pawn].get("Amount")) + " " + pawn + "'s from size " + str(pawns[pawn].get("Size")) + ', '

    return text


def print_board(board):
    text = ""
    for counter in range(len(board)):
        for index in range(len(board)):
            if board[index][counter] is not None:
                text += str(board[index][counter] + " ")
            else:
                text += ". "
        text += '\n'
    return text


def guess(row, column, player_who_take_guess, board):
    if board[switch_turn(player_who_take_guess)][row][column] is not None:
        place_symbol(row, column, '*', switch_turn(player_who_take_guess), play_boards)
        place_symbol(row, column, '*', player_who_take_guess, guess_boards)
        print("HIT")
    else:
        place_symbol(row, column, '-', switch_turn(player_who_take_guess), play_boards)
        place_symbol(row, column, '-', player_who_take_guess, guess_boards)
        print("MISS")


# board settings
WIDTH = 10

pawns = {
    "vliegdekschip": {
        "Symbol": 'v',
        "Amount": 1,
        "Size": 6
    },
    "slagschip": {
        "Symbol": 's',
        "Amount": 2,
        "Size": 4
    },
    "onderzeeër": {
        "Symbol": 'o',
        "Amount": 3,
        "Size": 3
    }, "Patrouilleschip": {
        "Symbol": 'p',
        "Amount": 4,
        "Size": 2
    },

}

stats = [None, copy.deepcopy(pawns),
         copy.deepcopy(pawns)]  # Amount is now how much they have left & player 0 do not exist
play_boards = [None, create_board(WIDTH, []), create_board(WIDTH, [])]  # player one and 2
guess_boards = [None, create_board(WIDTH, []), create_board(WIDTH, [])]

# Variables
winner = None
turn = 1

# setup

is_player_setup_done = [None, None, None]  # index 1 is player 1

while is_player_setup_done[turn] is None:
    print("Its player " + str(turn) + " turn to place pawns\n")
    print("You can place: " + get_all_pawns_in_text(stats[turn]))
    place_pawn(int(input("On which row\n")), int(input("On which column\n")), str(input("Witch boat\n")), turn,
               str(input("How do it have to place\n")), stats)

    print("Are you done ? Type yes ")
    print(print_board(play_boards[turn]))

    if str(input()).lower().find('e') >= 0:
        is_player_setup_done[turn] = True
        switch_turn(turn)
        print("Switching sides")
        turn = switch_turn(turn)

# running

while winner is None:
    print("Its player " + str(turn) + " turn to place guess\n")
    print(print_board(guess_boards[turn]))
    print("-" * WIDTH)
    print(print_board(play_boards[turn]))
    guess(int(input("On which row\n")), int(input("On which column\n")), turn, play_boards)
    print(print_board(guess_boards[turn]))
    turn = switch_turn(turn)
