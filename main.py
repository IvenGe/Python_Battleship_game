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


# board settings
WIDTH = 10
turn = 1
pawns = {
    "vliegdekschip": {
        "Amount": 1,
        "Size": 6
    },
    "slagschip": {
        "Amount": 2,
        "Size": 4
    },
    "onderzeeër": {
        "Amount": 3,
        "Size": 3
    }, "Patrouilleschip": {
        "Amount": 4,
        "Size": 2
    },

}
# Variables
Winner = None

# start
player1_play_board = create_board(WIDTH, [])
player1_guess_board = create_board(WIDTH, [])
player2_play_board = create_board(WIDTH, [])
player2_guess_board = create_board(WIDTH, [])

while Winner is None:
