
# Blackjack game
import random

class deck():
    # creates a deck with # of decks (deck_size) times 52
    @staticmethod
    def create_deck(deck_size):
        
        actual_deck = {}

        for temp in range(deck_size):
            first_char = str(temp)
            for deck in range(52):
                # converts deck into a number between 1 and 13, inclusive
                value = int(deck/4) + 1

                # for values 11,12,13 (Jack, Queen, King) gives that key a value of 10
                if(value > 10):
                    value = 10

                # Designates the suit of the card
                if(deck % 4 == 0):
                    suit = "Diamonds"
                elif(deck % 4 == 1):
                    suit = "Clubs"
                elif(deck % 4 == 2):
                    suit = "Hearts"
                elif(deck % 4 == 3):
                    suit = "Spades"

                # Displays the card number (ace, one, two, ..., king)
                card = str(int(deck/4) + 1)

                if(card == "1"):
                    card = "Ace"
                elif(card == "11"):
                    card = "Jack"
                elif(card == "12"):
                    card = "Queen"
                elif(card == "13"):
                    card = "King"

                second_char = str(deck)
                actual_deck[first_char + second_char] = [card, suit, value]

        return actual_deck
    
    # prints the whole deck
    @staticmethod
    def print_deck(actual_deck):
        print(actual_deck)

class Dealer():
    # creates the dealer with condition of hitting until 17, standing otherwise
    pass

class Chickens():
    # creates cpu players to play with player: Ester, Petra and Elinor

    # Three types: wildcard, aggressive, and safe
    def type:


    random.choice(type)
    pass

class Player():
    # creates the actions for the player, attributes
    pass

# plays the game by going through each player + dealer, deals the cards, etc.
class main():
    print("Welcome to Blackjack")
    
    # User inputs # of decks but is converted to a string, ord converts string to integer
    temp_decks = input("Please enter the number of decks you would like to use: ")
    num_decks = int(temp_decks)
    trial = deck()
    trial_deck = trial.create_deck(num_decks).copy()
    trial.print_deck(trial_deck)
    
    # returns and removes a random card from trial_deck
    print(trial_deck.pop(random.choice(list(trial_deck.keys()))))
    print(trial_deck.pop(random.choice(list(trial_deck.keys()))))

Main()
