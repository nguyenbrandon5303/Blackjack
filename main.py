# FOR BETTER CODING PRACTICE, START USING __init__ FUNCTION AND SELF FOR CLASSES AND ITS PARAMETERS
# CREATE hasAce FUNCTION IN BOTH DEALER AND PLAYER CLASSES
    # this will determine if their hand has aces
    # might make a hand list that has their current hand (THIS MIGHT SOLVE THE WHOLE ISSUE)

# Blackjack game
import random

class deck:
    # creates a deck with # of decks (deck_size) times 52
    @staticmethod
    def create_deck(deck_size):
        
        actual_deck = {}
        
        for temp in range(deck_size):
            for deck in range(52):
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
                actual_deck[str(temp) + str(deck)] = [card, suit , value]
        return actual_deck
    
    # prints the whole deck
    @staticmethod
    def print_deck(actual_deck):
        print(actual_deck)

class Dealer:
    # creates the dealer with condition of hitting until 17, standing otherwise
    # current_hand is the dealer's current hand, whenever they hit it adds on to this hand
    def __init__(self, current_deck, num_value, my_turn, current_hand):
        self.current_deck = current_deck
        self.num_value = num_value
        self.my_turn = my_turn
        self.current_hand = current_hand
        # this counts aces on the first card draw as an 11
        if(self.num_value == 1):
            self.num_value = 11
        for check in self.current_hand:
            self.num_value += check[2]

    
    def hit(self):
        print("The dealer has %d." % self.num_value)
        temp_card = self.current_deck.pop(random.choice(list(self.current_deck.keys())))
        self.current_hand.append(temp_card)
        card_value = temp_card[2]
        print(temp_card)
        
        #this resets the total value of the current hand to check for aces and changes respectively
        temp_hand_value = 0
        for ace in self.current_hand:
            if(ace[0] == 'Ace' and self.num_value < 11):
                ace[2] = 11
            elif(ace[0] == 'Ace' and self.num_value > 11):
                ace[2] = 1
            temp_hand_value += ace[2]
        self.num_value = temp_hand_value
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
    # current_hand is the dealer's current hand, whenever they hit it adds on to this hand
    
    def __init__(self, current_deck, name, num_value, my_turn, current_hand):
        self.current_deck = current_deck
        self.name = name
        self.num_value = num_value
        self.my_turn = my_turn
        self.current_hand = current_hand
        if(self.num_value == 1):
            self.num_value = 11
        for check in self.current_hand:
            self.num_value += check[2]
    
    def second_card(self, num_players):
        player_second_card = self.current_deck.pop(random.choice(list(self.current_deck.keys())))
        self.current_hand.append(player_second_card)
        self.num_value += player_second_card[2]
        
        #this resets the total value of the current hand to check for aces and changes respectively
        temp_hand_value = 0
        for ace in self.current_hand:
            if(ace[0] == 'Ace' and self.num_value < 11):
                ace[2] = 11
            elif(ace[0] == 'Ace' and self.num_value > 11):
                ace[2] = 1
            temp_hand_value += ace[2]
        self.num_value = temp_hand_value
        print("%s's second card is %s of %s. %s has %d." % (self.name, player_second_card[0], player_second_card[1], self.name, self.num_value))
        return player_second_card
    
    def hit(self):
        print("%s have %d." % (self.name, self.num_value))
        temp_card = self.current_deck.pop(random.choice(list(self.current_deck.keys())))
        self.current_hand.append(temp_card)
        card_value = temp_card[2]
        print(temp_card)
        
        #this resets the total value of the current hand to check for aces and changes respectively
        temp_hand_value = 0
        for ace in self.current_hand:
            if(ace[0] == 'Ace' and self.num_value < 11):
                ace[2] = 11
            elif(ace[0] == 'Ace' and self.num_value > 11):
                ace[2] = 1
            temp_hand_value += ace[2]
        self.num_value = temp_hand_value
        
        print("%s hits and now have %d." % (self.name, self.num_value))
        if(self.num_value > 21):
            print("%s busted with %d." % (self.name, self.num_value))
            self.my_turn = False
        return self.num_value
    
    def stand(self):
        print("%s stands with %d." % (self.name, self.num_value))
        self.my_turn = False

# plays the game by going through each player + dealer, deals the cards, etc.
class main:
    print("Welcome to Blackjack")
    
    # User inputs # of decks but is converted to a string, int converts string to integer
    temp_decks = input("Please enter the number of decks you would like to use: ")
    num_decks = int(temp_decks)
    trial = deck()
    trial_deck = trial.create_deck(num_decks).copy()
    # trial.print_deck(trial_deck)
    
    # User inputs # of players using same code as above to convert to integer
    temp_players = input("Please enter the number of players that would like to play: ")
    num_players = int(temp_players)
    
    # creates players
    list_players = []
    for player_name in range(1, num_players + 1):
        players_hand = []
        temp_name = input("Please enter Player %d's name: " % player_name)
        list_players.append(Player(trial_deck, temp_name, 0, True, players_hand))
    
    # creates dealer
    dealers_hand = []
    current_dealer = Dealer(trial_deck, 0, True, dealers_hand)
    current_dealer.temp_deck = trial_deck
    
    # deals first cards
    for first_card in range(1, num_players + 1):
        player_first_card = trial_deck.pop(random.choice(list(trial_deck.keys())))
        list_players[first_card - 1].num_value = player_first_card[2]
        list_players[first_card - 1].current_hand.append(player_first_card)
        print("%s starts with: %s of %s." % (list_players[first_card - 1].name, player_first_card[0], player_first_card[1]))
    dealer_first_card = trial_deck.pop(random.choice(list(trial_deck.keys())))
    dealers_hand.append(dealer_first_card)
    current_dealer.num_value = dealer_first_card[2]
    print("Dealer starts with: %s of %s." % (dealer_first_card[0], dealer_first_card[1]))
    
    # deals second cards
    for second_card in range(1, num_players + 1):
        list_players[second_card - 1].second_card(num_players)

    
    
    # game starts with first player and ends with the dealer
    for turn in range(0, num_players):
        while(list_players[turn].my_turn):
            action = input("Would %s like to Hit 'h' or Stand 's': " % list_players[turn].name)
            if(action == "h"):
                list_players[turn].hit()
            elif(action == "s"):
                list_players[turn].stand()
    
    # dealer's actions noting their conditions of hitting below 17, standing otherwise
    while(current_dealer.my_turn):
        while(current_dealer.num_value < 17):
            current_dealer.hit()
        if(current_dealer.num_value >= 17):
            current_dealer.stand()
    

main()




