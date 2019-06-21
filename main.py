

# Blackjack game
import random

class Deck():
    # creates a deck with # of decks (deck_size) times 52
    @staticmethod
    def create_deck(deck_size):
        
        actual_deck = []
        
        for multi_deck in range(deck_size):
            for single_deck in range(52):
                actual_deck.append(single_deck+1)
        
        # shuffles the whole deck
        random.shuffle(actual_deck)
        return actual_deck
    
    # prints the whole deck
    @staticmethod
    def print_deck(actual_deck):
        print(actual_deck)

class Dealer():
    # creates the dealer with condition of hitting until 17, standing otherwise
    pass

# plays the game by going through each player + dealer, deals the cards, etc.
class Main():
    print("Welcome to Blackjack")
    
    # User inputs # of decks but is converted to a string, ord converts string to integer
    temp_decks = input("Please enter the number of decks you would like to use: ")
    num_decks = int(temp_decks)
    trial = deck()
    trial_deck = trial.create_deck(num_decks)
    trial.print_deck(trial_deck)
    print(trial_deck.pop())
    print(trial_deck.pop()) 


main()