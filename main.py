def create_board(width, board):
    for row_index in range(width):
        board.append([])
        for column_index in range(width):
            board[row_index].append(None)

    return board.copy()


def place_pawn(row, column, pawn, player):  # unsafe :(
    pawn = str(pawn)
    if player == 1:
        player1_play_board[row][column] = pawn
    elif player == 2:
        player2_play_board[row][column] = pawn
    else:
        print("Hacker D: ?")


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
    len_text = 10

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

stats = [pawns.copy(), pawns.copy()]  # Amount is now how mutch they have left


# Variables
winner = None
turn = 1

# start
player1_play_board = create_board(WIDTH, [])
player1_guess_board = create_board(WIDTH, [])
player2_play_board = create_board(WIDTH, [])
player2_guess_board = create_board(WIDTH, [])

is_setup_done_player1 = None
is_setup_done_player2 = None

while is_setup_done_player1 is None or is_setup_done_player2 is None:
    print("Its player " + str(turn) + "turn to place pawns\n")
    print("You can place: " + get_all_pawns_in_text(pawns))
    place_pawn(int(input("On which row\n")), int(input("On which column\n")), str(input("Witch board\n")), turn)
    print("Are you done ?")
    print(print_board(player1_play_board))
    if str(input()).find('y') >= 0:
        if is_setup_done_player1:
            is_setup_done_player2 = True
        else:
            is_setup_done_player1 = True
        print("Switching sides")
        turn = switch_turn(turn)

print(get_all_pawns_in_text(pawns))
