from random import randint

def display_board(board):
    print("Here is your board: ")
    for i in range(7):
        if i % 2 == 0:
            print("-------------")
        else:
            print("|", end = " ")
            for j in range(3):
                print(board[i // 2][j], end = " | ")
            print()

def player_input():
    choice = "WRONG"
    while choice not in ['X', 'O']:
        choice = input("Choose one 'X' or 'O' \n Choice: ")
        if choice not in ['X', 'O']:
            print("Please, enter a valid character: ")

    if choice == 'X':
        return 'X'
    elif choice == 'O':
        return 'O'

def place_marker(board, character, position):

    if position in [1,2,3]:
        board[0][position - 1] = character
    elif position in [4,5,6]:
        board[1][position - 4] = character
    elif position in [7,8,9]:
        board[2][position - 7] = character

def win_check(board, mark):
    if board[0][0] == mark:
        if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
            return True
        elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            return True
        elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
            return True
    if board[2][0] == mark:
        if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
            return True
        if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
            return True
    if board[0][2] == mark:
        if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
            return True
    if board[0][1] == mark:
        if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
            return True
    if board[1][0] == mark:
        if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
            return True
    return False


def choose_first():
    print("We will randomize from 0 to 100 to know who goes first, if its odd number -> 'X' goes first. If it's not odd 'O' -> goes first")
    choice = randint(0,100)
    print("Randomized number: {}".format(choice))
    if choice % 2 != 0:
        return 'X'
    else:
        return 'O'

def space_check(board, position):
    if position in [1,2,3]:
        if board[0][position - 1] == " ":
            return True
    elif position in [4,5,6]:
        if board[1][position - 4] == " ":
            return True
    elif position in [7,8,9]:
        if board[2][position - 7] == " ":
            return True
    return False

def full_board_check(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                return False
    return True

def player_choice(board):
     choice = "wrong"
     acceptable_values = ['1','2','3','4','5','6','7','8','9']
     while choice not in acceptable_values:
         choice = input("Please enter the index in range (1-9): ")

         if choice in acceptable_values:
             if space_check(board, int(choice)):
                 return int(choice)
         else:
             print("Please enter valid value! ")

def replay():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Do you want to play again? (Y, N): ")

        if choice not in ['Y','N']:
            print("Sorry, I don't understand you!")
    if choice == 'Y':
        return True
    else:
        return False

# display_board(board)
# player_input()
# place_marker(board, 'X', 1)
# place_marker(board, 'X', 2)
# place_marker(board, 'X', 3)
# display_board(board)
# print(win_check(board, 'X'))

print('Welcome to Tic Tac Toe!')

while True:
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = choose_first()
    if player == 'X':
        first_player = 'X'
        print("'",player,"'","goes first")
        second_player = 'O'
    else:
        first_player = 'O'
        second_player = 'X'
        print("'",player,"'", "goes first")

    display_board(board)
    game_on = True


    while game_on:
# ----------------------------FIRST PLAYER MOVE-------------------------------
        index = player_choice(board)
        while space_check(board, index) == False:
            print("It's not the free case to put!")
            index = player_choice(board)
        else:
            place_marker(board, first_player, index)
        if win_check(board, first_player):
            print(first_player, "Won!!! Congratulations ))")
            display_board(board)
            game_on = False
            break
        display_board(board)

        if full_board_check(board):
            print("It's a draw!")
            display_board(board)
            game_on = False
            break
# ---------------------------SECOND PLAYER MOVE-----------------------------------
        index = player_choice(board)
        while space_check(board, index) == False:
            print("It's not the free case to put!")
            index = player_choice(board)
        else:
            place_marker(board, second_player, index)
        if win_check(board, second_player):
            print(second_player, "Won!!! Congratulations ))")
            display_board(board)
            game_on = False
            break
        display_board(board)

    if not replay():
        break
