def create_board(width, board):
    for row_index in range(width):
        board.append([])
        for column_index in range(width):
            board[row_index].append(None)

    return board.copy()


def place_symbol(row, column, pawn, player):  # unsafe :(
    pawn = str(pawn)
    play_boards[player][row][column] = stats[player][pawn].get("Symbol")


def place_pawn(row, column, pawn, player, rotation, stats):
    if rotation == '_':
        for i in range(stats[player][pawn].get("Size")):
            place_symbol(row + i, column, pawn, player)
    else:
        for i in range(stats[player][pawn].get("Size")):
            place_symbol(row, column + i, pawn, player)


def switch_turn(turn=None):
    if turn == 1:
        turn = 2

    else:
        turn = 1
    return turn


def get_all_pawns_in_text(pawns):
    text = ""
    for pawn in pawns.keys():
        text += pawn + ', '

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

stats = [None, pawns.copy(), pawns.copy()]  # Amount is now how much they have left & player 0 do not exist
play_boards = [None, create_board(WIDTH, []), create_board(WIDTH, [])]
guess_boards = [None, create_board(WIDTH, []), create_board(WIDTH, [])]

# Variables
winner = None
turn = 1

# start

is_player_setup_done = [None, None, None]  # index 1 is player 1

while is_player_setup_done[turn] is None:
    print("Its player " + str(turn) + " turn to place pawns\n")
    print("You can place: " + get_all_pawns_in_text(pawns))
    place_pawn(int(input("On which row\n")), int(input("On which column\n")), str(input("Witch boat\n")), turn,
               str(input("How do it have to place")), stats)

    print("Are you done ?")
    print(print_board(play_boards[turn]))

    if str(input()).find('y') >= 0:
        is_player_setup_done[turn] = True
        switch_turn(turn)
    print("Switching sides")
    turn = switch_turn(turn)
