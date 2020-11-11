import random
import emoji
import shutil
from colorama import init, Fore, Style
init()
#   CARD, SUIT, RANK, VALUE
suits = (emoji.emojize(Fore.BLACK + ':spade_suit:' + Fore.WHITE), emoji.emojize(Fore.RED + ':heart_suit:' + Fore.WHITE), emoji.emojize(Fore.RED + ':diamond_suit:' + Fore.WHITE), emoji.emojize(Fore.BLACK + ':club_suit:' + Fore.WHITE))
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}

class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create a card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# SETUP THE GAME
name_1 = input("1st player's name: ")
player_one = Player(name_1)
name_2 = input("2nd player's name: ")
player_two = Player(name_2)

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(Style.BRIGHT + Fore.CYAN + f'Round {round_num} '.center(shutil.get_terminal_size().columns) + Fore.WHITE + Style.RESET_ALL)

    if len(player_one.all_cards) == 0:
        print(Fore.RED + f"{player_one.name} out of cards.".center(shutil.get_terminal_size().columns))
        print(Fore.GREEN + f"{player_two.name} Wins !!!".center(shutil.get_terminal_size().columns))
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print(Fore.RED + f"{player_two.name} out of cards.".center(shutil.get_terminal_size().columns))
        print(Fore.GREEN + f"Player {player_one.name} Wins !!!".center(shutil.get_terminal_size().columns))
        game_on = False
        break

    # START NEW ROUND

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        print(player_one)
        print(player_two)
        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war = False

        else:
            print(emoji.emojize(':crossed_swords:  WAR :crossed_swords:').center(shutil.get_terminal_size().columns))

            if len(player_one.all_cards) < 5:
                print(emoji.emojize(f"{player_one.name} is unable to declare a war :crying_face:".center(shutil.get_terminal_size().columns)))
                print(emoji.emojize(f"Player {player_two.name} Won, Congratualtions :partying_face: :partying_face: :partying_face:".center(shutil.get_terminal_size().columns)))
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print(emoji.emojize(f"{player_two.name} is unable to declare a war :crying_face:".center(shutil.get_terminal_size().columns)))
                print(emoji.emojize(f"Player {player_one.name} Won, Congratualtions :partying_face: :partying_face: :partying_face:".center(shutil.get_terminal_size().columns)))
                game_on = False
                break
            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
