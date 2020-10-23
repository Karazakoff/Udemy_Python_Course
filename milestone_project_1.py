
def display(game_list):
    print("Here is the current list: ")
    print(game_list)

def position_choice():

    choice = 'wrong'

    while choice not in ['0', '1', '2']:

        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice!")
    return int(choice)

def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y','N']:

        choice = input("Keep playing? (Y or N) ")

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please enter Y or N   ")

    if choice == 'Y':
        return True
    else:
        return False


def replacement_choise(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list



# -----------------            GAME INIT
game_on =  True
game_list = [0,1,2]
# ---------------               THE GAME
while game_on:
    display(game_list)
    position = position_choice()
    game_list = replacement_choise(game_list, position)
    display(game_list)
    game_on = gameon_choice()
