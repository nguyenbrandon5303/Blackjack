# FOR BETTER CODING PRACTICE, START USING __init__ FUNCTION AND SELF FOR CLASSES AND ITS PARAMETERS

# Blackjack game
import random

class deck:
    # creates a deck with # of decks (deck_size) times 52
    @staticmethod
    def create_deck(deck_size):
        
        actual_deck = {}
        
        for deck in range(deck_size * 52):
            # converts deck into a number between 1 and 13, inclusive
            value = int(deck/4) + 1
            
            # for values 11,12,13 (Jack, Queen, King) gives that key a value of 10
            if(value > 10):
                value = 10
            
            # Designates the suit of the card
            if(deck % 4 == 0):
                suit = "Diamond"
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
            actual_deck[deck] = [card, suit , value]
        
        return actual_deck
    
    # prints the whole deck
    @staticmethod
    def print_deck(actual_deck):
        print(actual_deck)

class Dealer:
    # creates the dealer with condition of hitting until 17, standing otherwise
    def __init__(self, current_deck, num_value, my_turn):
        self.current_deck = current_deck
        self.num_value = num_value
        self.my_turn = my_turn
        if(self.num_value == 1):
            self.num_value = 11
    
    def hit(self):
        print("The dealer has %d." % self.num_value)
        temp_card = self.current_deck.pop(random.choice(list(self.current_deck.keys())))
        card_value = temp_card[2]
        print(temp_card)
        
        if(card_value == 1 & self.num_value <= 10):
            card_value = 11
        
        self.num_value += card_value
        print("The dealer hits and now has %d." % self.num_value)
        return self.num_value
    
    def stand(self):
        if(self.num_value > 21):
            print("The dealer has %d. The dealer busts." % self.num_value)
        else:
            print("The dealer has %d. The dealer stands." % self.num_value)
        self.my_turn = False

class Chickens:
    # creates cpu players to play with player: Ester, Petra and Elinor

    # Three types: wildcard, aggressive, and safe
    def type():
        pass

    # random.choice(type)
    pass

class Player:
    # creates the actions for the player, attributes
    pass

# plays the game by going through each player + dealer, deals the cards, etc.
class main:
    print("Welcome to Blackjack")
    
    # User inputs # of decks but is converted to a string, int converts string to integer
    temp_decks = input("Please enter the number of decks you would like to use: ")
    num_decks = int(temp_decks)
    trial = deck()
    trial_deck = trial.create_deck(num_decks).copy()
    trial.print_deck(trial_deck)
    
    # User inputs # of players using same code as above to convert to integer
    temp_players = input("Please enter the number of players that would like to play: ")
    num_players = int(temp_players)
    
    # deals first cards
    dealer_first_card = trial_deck.pop(random.choice(list(trial_deck.keys())))
    
    # creates dealer
    test_dealer = Dealer(trial_deck, dealer_first_card[2], True)
    test_dealer.temp_deck = trial_deck
    
    # dealer's actions noting their conditions of hitting below 17, standing otherwise
    while(test_dealer.my_turn == True):
        while(test_dealer.num_value < 17):
            test_dealer.hit()
        if(test_dealer.num_value >= 17):
            test_dealer.stand()


main()
