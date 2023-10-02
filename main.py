import copy

WIDTH = 10

pawns = {
    "vliegdekschip": {"Symbol": 'v', "Amount": 1, "Size": 6},
    "slagschip": {"Symbol": 's', "Amount": 2, "Size": 4},
    "onderzeeër": {"Symbol": 'o', "Amount": 3, "Size": 3},
    "Patrouilleschip": {"Symbol": 'p', "Amount": 4, "Size": 2},
}

stats = [None, copy.deepcopy(pawns), copy.deepcopy(pawns)]


def create_board(width):
    return [[None for _ in range(width)] for _ in range(width)]


def print_board(board):
    text = "  " + " ".join(str(i) for i in range(len(board))) + "\n"
    for idx, row in enumerate(board):
        row_text = str(idx) + " " + " ".join([cell if cell else '.' for cell in row])
        text += row_text + "\n"
    return text


def place_symbol(board, row, column, symbol):
    board[row][column] = symbol


def switch_turn(turn):
    return 1 if turn == 2 else 2


def is_position_valid_for_placement(board, row, column, pawn, rotation):
    size = pawn["Size"]
    if rotation == "_":
        if column + size > WIDTH:
            return False
        return all([board[row][column + i] is None for i in range(size)])
    else:
        if row + size > WIDTH:
            return False
        return all([board[row + i][column] is None for i in range(size)])


def place_pawn(board, row, column, pawn, rotation):
    size = pawn["Size"]
    symbol = pawn["Symbol"]
    for i in range(size):
        r, c = (row + i, column) if rotation == "|" else (row, column + i)
        place_symbol(board, r, c, symbol)


def total_occupied_cells():
    total = 0
    for player in stats:
        if player:
            for _, details in player.items():
                total += details["Amount"] * details["Size"]
    return total


def check_for_winner(board):
    return sum(1 for row in board for cell in row if cell == '*') == total_occupied_cells()


play_boards = [None, create_board(WIDTH), create_board(WIDTH)]
guess_boards = [None, create_board(WIDTH), create_board(WIDTH)]
turn = 1
winner = None

# Setup Phase
for player in [1, 2]:
    while True:
        print("Player", player, "setup phase")
        print(print_board(play_boards[player]))
        pawn_name = input("Which boat: " + ", ".join([f"{name}({details['Amount']} left)" for name, details in stats[player].items() if details['Amount'] > 0]) + ": ")
        if pawn_name not in stats[player] or stats[player][pawn_name]["Amount"] <= 0:
            print("Invalid choice!")
            continue
        row, column = map(int, input("Enter row, column: ").split(","))
        rotation = input("In which direction (_ or |): ")
        if is_position_valid_for_placement(play_boards[player], row, column, stats[player][pawn_name], rotation):
            place_pawn(play_boards[player], row, column, stats[player][pawn_name], rotation)
            stats[player][pawn_name]["Amount"] -= 1
        else:
            print("Invalid placement!")
        if all([details["Amount"] == 0 for _, details in stats[player].items()]):
            break

# Game Phase
while not winner:
    print("Player", turn, "guess phase")
    print(print_board(guess_boards[turn]))
    row, column = map(int, input("Enter row, column to guess: ").split(","))
    if play_boards[switch_turn(turn)][row][column]:
        print("HIT!")
        place_symbol(guess_boards[turn], row, column, '*')
        place_symbol(play_boards[switch_turn(turn)], row, column, '*')
    else:
        print("MISS!")
        place_symbol(guess_boards[turn], row, column, '-')
    if check_for_winner(guess_boards[turn]):
        winner = turn
    turn = switch_turn(turn)

print("Winner is: Player", winner)
