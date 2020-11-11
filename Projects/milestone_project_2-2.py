import random
import emoji
import shutil
import time
from colorama import init, Fore, Style
init()
# Default players
player_1 = None
player_2 = None
player_3 = None
player_4 = None
player_5 = None
player_6 = None
game_on = True
#   CARD, SUIT, RANK, VALUE
suits = (emoji.emojize(Fore.BLACK + ':spade_suit:' + Fore.WHITE), emoji.emojize(Fore.RED + ':heart_suit:' + Fore.WHITE), emoji.emojize(Fore.BLACK + ':club_suit:' + Fore.WHITE), emoji.emojize(Fore.RED + ':diamond_suit:' + Fore.WHITE))
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11}
players_stickers = (emoji.emojize(':alien_monster:'), emoji.emojize(':butterfly:'), emoji.emojize(':clown_face:'), emoji.emojize(':lemon:'), emoji.emojize(':money-mouth_face:'), emoji.emojize(':high_voltage:'),emoji.emojize(':snowman_without_snow:'),emoji.emojize(':soccer_ball:'),emoji.emojize(':video_game:'))
class Card():
    # Simple Card class with suit, rank, value
    def __init__(self, suit = emoji.emojize(Fore.BLACK + ':spade_suit:' + Fore.WHITE), rank = 'A'):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return Fore.WHITE + f"{self.rank}{self.suit}"

class Deck():

    def __init__(self):
        self.cards = []
        # Creaating a deck with objects Card
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        for index, value in enumerate(self.cards):
            if index % 13 == 0:
                print()
            print(value, end = " ")
        return ""

    def shuffle(self):
        # Simply shuffling the deck
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        if card.rank == 'A':
            self.aces = self.aces + 1
        self.cards.append(card)
        self.value = self.value + card.value

    def adjust_for_aces(self):
        for _ in range(self.aces):
            if self.value > 21:
                self.value = self.value - 10

    def __str__(self):
        print(emoji.emojize("Your hand is: "), end = "")
        for card in self.cards:
            print(card, end = " ")
        print()
        print(emoji.emojize(f"Your value is: {self.value}:glowing_star:"))
        return ""

class Player(Hand):

    def __init__(self, name, sticker, balance = 100):
        super().__init__()
        self.name = name
        self.balance = balance
        self.sticker = sticker
        self.bet = 0
    def win_bet(self, amount):
        self.bet = amount

    def lose_bet(self, amount):
        self.bet = amount

    def hand(self):
        print(emoji.emojize("Your hand is: "), end = "")
        for card in self.cards:
            print(card, end = " ")
        print()
        print(emoji.emojize(f"Your value is: {self.value}:glowing_star:"))
        return ""

    def __str__(self):
        print()
        print(f"Player name: {self.name}".center(shutil.get_terminal_size().columns))
        print()
        print(f"Player's sticker: {self.sticker}".center(shutil.get_terminal_size().columns))
        print(f"Player's balance: {self.balance}$".center(shutil.get_terminal_size().columns))
        return ""

class Dealer(Hand):
    def __init__(self):
        self.name = 'Dealer'
        self.sticker = emoji.emojize(":man_judge:")
        self.cards = []
        super().__init__()

    def show_some(self):
        print(f"Dealer's hand {self.cards[0]} [*]".center(shutil.get_terminal_size().columns))

    def show_all(self):
        print("Dealer's hand: ", end = "")
        for card in self.cards:
            print(card, end = " ")
        print()


def take_info():
    global player_1
    global player_2
    global player_3
    global player_4
    global player_5
    global player_6

    check = True
    while check:
        try:
            time.sleep(0.5)
            players = int(input("How many players want to play: "))

        except ValueError:
            time.sleep(0.5)
            print("Please, enter valid value !!!")

        else:
            if players < 1 or players > 6:
                time.sleep(0.5)
                print("This amount of players can't participate, Sorry")

                check = True
            else:
                break
    if players == 1:
        time.sleep(0.5)
        name = input("Choose a nickname: ")

        for index, sticker in enumerate(players_stickers):
            print("{} -> {}".format(index + 1, sticker), end = "  |  ")
        print()
        while check:
            try:
                time.sleep(0.5)
                choise = int(input("Choose the index to assign the sticker: "))

                if choise == 1:
                    sticker = players_stickers[0]
                elif choise == 2:
                    sticker = players_stickers[1]
                elif choise == 3:
                    sticker = players_stickers[2]
                elif choise == 4:
                    sticker = players_stickers[3]
                elif choise == 5:
                    sticker = players_stickers[4]
                elif choise == 6:
                    sticker = players_stickers[5]
                elif choise == 7:
                    sticker = players_stickers[6]
                elif choise == 8:
                    sticker = players_stickers[7]
                elif choise == 9:
                    sticker = players_stickers[8]
            except:
                time.sleep(0.5)
                print("Something went wrong try again")

            else:
                if choise not in [1,2,3,4,5,6,7,8,9]:
                    time.sleep(0.5)
                    print("index our of range")

                    check = True
                else:
                    break
        player_1 = Player(name, sticker)
    elif players == 2:
        time.sleep(0.5)
        print("First Player:")
        name = input("Choose a nickname: ")

        for index, sticker in enumerate(players_stickers):
            print("{} -> {}".format(index + 1, sticker), end = "  |  ")
        print()
        while check:
            try:
                time.sleep(0.5)
                choise = int(input("Choose the index to assign the sticker: "))

                if choise == 1:
                    sticker = players_stickers[0]
                elif choise == 2:
                    sticker = players_stickers[1]
                elif choise == 3:
                    sticker = players_stickers[2]
                elif choise == 4:
                    sticker = players_stickers[3]
                elif choise == 5:
                    sticker = players_stickers[4]
                elif choise == 6:
                    sticker = players_stickers[5]
                elif choise == 7:
                    sticker = players_stickers[6]
                elif choise == 8:
                    sticker = players_stickers[7]
                elif choise == 9:
                    sticker = players_stickers[8]
            except:
                time.sleep(0.5)
                print("Something went wrong try again")

            else:
                if choise not in [1,2,3,4,5,6,7,8,9]:
                    time.sleep(0.5)
                    print("index our of range")

                    check = True
                else:
                    break
        player_1 = Player(name, sticker)
        print("Second Player:")
        name = input("Choose a nickname: ")

        for index, sticker in enumerate(players_stickers):
            print("{} -> {}".format(index + 1, sticker), end = "  |  ")
        print()
        while check:
            try:
                time.sleep(0.5)
                choise = int(input("Choose the index to assign the sticker: "))

                if choise == 1:
                    sticker = players_stickers[0]
                elif choise == 2:
                    sticker = players_stickers[1]
                elif choise == 3:
                    sticker = players_stickers[2]
                elif choise == 4:
                    sticker = players_stickers[3]
                elif choise == 5:
                    sticker = players_stickers[4]
                elif choise == 6:
                    sticker = players_stickers[5]
                elif choise == 7:
                    sticker = players_stickers[6]
                elif choise == 8:
                    sticker = players_stickers[7]
                elif choise == 9:
                    sticker = players_stickers[8]
            except:
                time.sleep(0.5)
                print("Something went wrong try again")

            else:
                if choise not in [1,2,3,4,5,6,7,8,9]:
                    time.sleep(0.5)
                    print("index our of range")
                    check = True
                else:
                    break
        player_2 = Player(name, sticker)
    elif players == 3:
        time.sleep(0.5)
        print("First Player:")
        name = input("Choose a nickname: ")

        for index, sticker in enumerate(players_stickers):
            print("{} -> {}".format(index + 1, sticker), end = "  |  ")
        print()
        while check:
            try:
                time.sleep(0.5)
                choise = int(input("Choose the index to assign the sticker: "))

                if choise == 1:
                    sticker = players_stickers[0]
                elif choise == 2:
                    sticker = players_stickers[1]
                elif choise == 3:
                    sticker = players_stickers[2]
                elif choise == 4:
                    sticker = players_stickers[3]
                elif choise == 5:
                    sticker = players_stickers[4]
                elif choise == 6:
                    sticker = players_stickers[5]
                elif choise == 7:
                    sticker = players_stickers[6]
                elif choise == 8:
                    sticker = players_stickers[7]
                elif choise == 9:
                    sticker = players_stickers[8]
            except:
                time.sleep(0.5)
                print("Something went wrong try again")

            else:
                if choise not in [1,2,3,4,5,6,7,8,9]:
                    time.sleep(0.5)
                    print("index our of range")

                    check = True
                else:
                    break
        player_1 = Player(name, sticker)
        time.sleep(0.5)
        print("Second Player:")
        name = input("Choose a nickname: ")

        for index, sticker in enumerate(players_stickers):
            print("{} -> {}".format(index + 1, sticker), end = "  |  ")
        print()
        while check:
            try:
                time.sleep(0.5)
                choise = int(input("Choose the index to assign the sticker: "))

                if choise == 1:
                    sticker = players_stickers[0]
                elif choise == 2:
                    sticker = players_stickers[1]
                elif choise == 3:
                    sticker = players_stickers[2]
                elif choise == 4:
                    sticker = players_stickers[3]
                elif choise == 5:
                    sticker = players_stickers[4]
                elif choise == 6:
                    sticker = players_stickers[5]
                elif choise == 7:
                    sticker = players_stickers[6]
                elif choise == 8:
                    sticker = players_stickers[7]
                elif choise == 9:
                    sticker = players_stickers[8]
            except:
                time.sleep(0.5)
                print("Something went wrong try again")

            else:
                if choise not in [1,2,3,4,5,6,7,8,9]:
                    time.sleep(0.5)
                    print("index our of range")

                    check = True
                else:
                    break
        player_2 = Player(name, sticker)
        print("Third Player:")
        name = input("Choose a nickname: ")

        for index, sticker in enumerate(players_stickers):
            print("{} -> {}".format(index + 1, sticker), end = "  |  ")
        print()
        while check:
            try:
                time.sleep(0.5)
                choise = int(input("Choose the index to assign the sticker: "))

                if choise == 1:
                    sticker = players_stickers[0]
                elif choise == 2:
                    sticker = players_stickers[1]
                elif choise == 3:
                    sticker = players_stickers[2]
                elif choise == 4:
                    sticker = players_stickers[3]
                elif choise == 5:
                    sticker = players_stickers[4]
                elif choise == 6:
                    sticker = players_stickers[5]
                elif choise == 7:
                    sticker = players_stickers[6]
                elif choise == 8:
                    sticker = players_stickers[7]
                elif choise == 9:
                    sticker = players_stickers[8]
            except:
                time.sleep(0.5)
                print("Something went wrong try again")

            else:
                if choise not in [1,2,3,4,5,6,7,8,9]:
                    time.sleep(0.5)
                    print("index our of range")
                    check = True
                else:
                    break
        player_3 = Player(name, sticker)
    return players

def take_bet(player):
    check = True
    while check:
        try:
            time.sleep(0.5)
            bet = int(input("How much money you want to bet: "))

        except ValueError:
            time.sleep(0.5)
            print("Please, enter a valid number!!!")

        else:
            if player.balance - bet < 0:
                check = True
                time.sleep(0.5)
                print(f"You can not bet {bet}$ !!!")

            else:
                player.bet = bet
                player.balance  = player.balance - bet
                break

def hit(deck, player):
    player.add_card(deck.deal_one())
    player.adjust_for_aces()
    if player.value > 21:
        return False
    else:
        return True

def hit_or_stand(deck, player, dealer):
    global game_on
    choise = "WRONG"
    player.hand()
    while choise != 'hit' or choise != 'stand':
        time.sleep(0.5)
        choise = input("What is your action ('hit/stand'): ")

        if choise == 'hit' or choise == 'stand':
            break
        else:
            time.sleep(0.5)
            print("I don't understand you, try again")

    if choise == 'hit':
        if hit(deck, player):
            time.sleep(0.5)
            print(f"Here is your new CARD: {player.cards[-1]}")
            game_on = True
        else:
            player.hand()
            print("Sorry, your cards out of 21, you lost")
            game_on = False
    elif choise == 'stand':
        while dealer.value < player.value:
            dealer.add_card(deck.deal_one())
            dealer.adjust_for_aces()

        if dealer.value == player.value:
            print("It's a draw!!!")
            dealer.show_all()

        elif dealer.value > 21:
            player.balance += player.bet * 2
            print(f"{player.name} wins {player.bet * 2} !!! ")
            dealer.show_all()

        elif dealer.value <= 21:
            print("Dealer wins !!!")
            dealer.show_all()

        game_on = False




# Initialization of Game
check = True
game_on = True
time.sleep(0.5)
print(100 * "\n")
print("Welcome to BlackJack Game !!!".center(shutil.get_terminal_size().columns))
print(12 * "\n")
play = take_info()
if play == 1:
    while game_on:
        time.sleep(0.5)
        deck = Deck()
        deck.shuffle()
        dealer = Dealer()

        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())

        player_1.add_card(deck.deal_one())
        player_1.add_card(deck.deal_one())

        print(player_1)
        take_bet(player_1)
        dealer.show_some()
        while game_on:
            hit_or_stand(deck, player_1, dealer)



        answer = input("Would you like to play more? (y/n)")
        if answer == 'y':
            game_on = True
            del deck
            del dealer
            player_1.cards = []
            player_1.value = 0
            player_1.aces = 0
        elif answer == 'n':
            game_on = False
if play == 2:
    while game_on:
        time.sleep(0.5)
        deck = Deck()
        deck.shuffle()
        dealer = Dealer()

        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())

        player_1.add_card(deck.deal_one())
        player_1.add_card(deck.deal_one())

        player_2.add_card(deck.deal_one())
        player_2.add_card(deck.deal_one())

        print(player_1, player_2)
        print(f"First {player_1.name} bets:")
        take_bet(player_1)
        print(f"Second {player_2.name} bets:")
        take_bet(player_2)
        time.sleep(0.5)
        print(100 * "\n")
        print("We can start now!".center(shutil.get_terminal_size().columns))
        print(10 * "\n")
        time.sleep(0.5)

        print(f"{player_1.name} goes")
        dealer.show_some()
        while game_on:
            hit_or_stand(deck, player_1, dealer)

        del dealer
        dealer = Dealer()
        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())
        time.sleep(3)
        game_on = True
        print(100 * "\n")

        print(f"{player_2.name} goes")
        dealer.show_some()
        while game_on:
            hit_or_stand(deck, player_2, dealer)


        answer = input("Would you like to play more? (y/n)")
        if answer == 'y':
            game_on = True
            del deck
            del dealer
            player_1.cards = []
            player_1.value = 0
            player_1.aces = 0
            player_2.cards = []
            player_2.value = 0
            player_2.aces = 0
            print(100 * "\n")
        elif answer == 'n':
            game_on = False
if play == 3:
    while game_on:
        time.sleep(0.5)
        deck = Deck()
        deck.shuffle()
        dealer = Dealer()

        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())

        player_1.add_card(deck.deal_one())
        player_1.add_card(deck.deal_one())

        player_2.add_card(deck.deal_one())
        player_2.add_card(deck.deal_one())

        player_3.add_card(deck.deal_one())
        player_3.add_card(deck.deal_one())

        print(player_1, player_2, player_3)
        print(f"First {player_1.name} bets:")
        take_bet(player_1)
        print(f"Second {player_2.name} bets:")
        take_bet(player_2)
        print(f"Third {player_3.name} bets:")
        take_bet(player_3)
        time.sleep(0.5)
        print(100 * "\n")
        print("We can start now!".center(shutil.get_terminal_size().columns))
        print(10 * "\n")
        time.sleep(0.5)

        print(f"{player_1.name} goes")
        dealer.show_some()
        while game_on:
            hit_or_stand(deck, player_1, dealer)

        del dealer
        dealer = Dealer()
        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())
        time.sleep(3)
        game_on = True
        print(100 * "\n")

        print(f"{player_2.name} goes")
        dealer.show_some()
        while game_on:
            hit_or_stand(deck, player_2, dealer)

        del dealer
        dealer = Dealer()
        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())
        time.sleep(3)
        game_on = True
        print(100 * "\n")
        print(f"{player_3.name} goes")
        dealer.show_some()
        while game_on:
            hit_or_stand(deck, player_3, dealer)
        answer = input("Would you like to play more? (y/n)")
        if answer == 'y':
            game_on = True
            del deck
            del dealer
            player_1.cards = []
            player_1.value = 0
            player_1.aces = 0
            player_2.cards = []
            player_2.value = 0
            player_2.aces = 0
            player_3.cards = []
            player_3.value = 0
            player_3.aces = 0
            print(100 * "\n")
        elif answer == 'n':
            game_on = False
