from random import shuffle

def shuffle_list(example):
    shuffle(example)
    return example

def player_guess():

    guess = input("Give me number from 1 to 5 includivly: ")
    while True:
        if guess not in ['1','2','3','4','5']:
            guess = input("Please give me valid number: ")
        else:
            return int(guess)

def game(my_list, guess):
    for i in range(len(my_list)):
        if my_list[i] == '[o]':
            if i + 1 == guess:
                print("You've chosen right one !")
                print(my_list)
                break
            else:
                print("Sorry, you chose wrong ;(")
                print(my_list)
                break

# ------------------INITIALISATION OF LIST-------------

cups = ['[o]', '[ ]', '[ ]', '[ ]', '[ ]']


# ----------------SHUFFLE LIST AND PLAYER GUESS------------
my_list = shuffle_list(cups)
guess = player_guess()

game(my_list, guess)

# -----------------RESULT---------------
