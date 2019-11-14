import random


# creates card class that haves the parameters: number value, name of card (ie "Three"), suit, and if it's an ace
# the card itself is a list of length 4 of the above parameters in the same order
# [number value, name, suit, if ace]
class Card:
    def __init__(self, numValue, name, suit, isAce):
        self.numValue = numValue
        self.name = name
        self.suit = suit
        self.isAce = isAce

    def createCard(self):
        # creates empty list for card parameters
        whole_card = []

        # create suit depending on position of card in deck (order is diamonds -> clubs -> hearts -> spades)
        if self.numValue % 4 == 1:
            self.suit = "Diamonds"
        elif self.numValue % 4 == 2:
            self.suit = "Clubs"
        elif self.numValue % 4 == 3:
            self.suit = "Hearts"
        elif self.numValue % 4 == 0:
            self.suit = "Spades"

        # create the value of card (order is ace -> 2 -> 3 ... -> jack -> queen -> king)
        self.numValue = int(self.numValue/4) +1

        # create name of card depending on above value (1 = Ace, 2 = Two, etc.)
        if self.numValue == 1:
            self.name = "Ace"
        if self.numValue == 2:
            self.name = "Two"
        if self.numValue == 3:
            self.name = "Three"
        if self.numValue == 4:
            self.name = "Four"
        if self.numValue == 5:
            self.name = "Five"
        if self.numValue == 6:
            self.name = "Six"
        if self.numValue == 7:
            self.name = "Seven"
        if self.numValue == 8:
            self.name = "Eight"
        if self.numValue == 9:
            self.name = "Nine"
        if self.numValue == 10:
            self.name = "Ten"
        if self.numValue == 11:
            self.name = "Jack"
        if self.numValue == 12:
            self.name = "Queen"
        if self.numValue == 13:
            self.name = "King"

        # reformat the value of card if jack, queen, or king to 10
        if self.numValue > 10:
            self.numValue = 10

        # identifies if card is an ace
        if self.name == "Ace":
            self.isAce = True
            self.numValue = 11

        # appends the parameters creating a single card
        whole_card.append(self.numValue)
        whole_card.append(self.name)
        whole_card.append(self.suit)
        whole_card.append(self.isAce)

        return whole_card


# creates deck class that initializes values for each card in that deck (one deck = 52 cards)
class Deck:
    def __init__(self, numDeck):
        self.numDeck = numDeck

    def createDeck(self):
        deck_list = []
        for i in range(self.numDeck):
            for j in range(52):
                # temp_card is an "empty" card that takes the j value to determine what card it is going to be
                temp_card = Card(j, "", "", False)
                deck_list.append(temp_card.createCard())

        return deck_list


# creates player class that gives the user to hit/stand, stores their hand, and calculates their hand value
class Player:

    # initializes the starting value of the player's hand to be zero as a variable usable across the class
    hand_value = 0

    def __init__(self, player_name, hand, current_deck, turn):
        self.player_name = player_name
        self.hand = hand
        self.current_deck = current_deck
        self.turn = turn

        # this will change the first ace into a 1 instead of 11 in case the starting hand contain aces
        if self.handValue() > 21:
            self.changeAce()

    # removes a card from the deck and puts it into the player's hand
    def hit(self):
        hit_card = self.current_deck.pop(int(random.uniform(0, len(self.current_deck))))
        self.hand.append(hit_card)
        print("%s hits and receives %s of %s." % (self.player_name, hit_card[1], hit_card[2]))

        # checks if hand is over 21 and doesn't contain any aces
        if self.handValue() > 21:
            if self.checkAce11():
                self.changeAce()
            else:
                self.bust()

    # ends the player's turn
    def stand(self):
        self.handValue()
        print("%s stands with %d." % (self.player_name, self.handValue()))
        self.turn = False

    # calculates the value of the player's hand
    def handValue(self):
        self.hand_value = 0
        for x in self.hand:
            self.hand_value += x[0]
        return self.hand_value

    # checks if there is an ace in hand and if the ace is valued at an 11
    def checkAce11(self):
        for x in self.hand:
            if x[3] and x[0] == 11:
                return True
        return False

    # used when hand value is over 21 to see if an ace can be changed into a 1
    def changeAce(self):
        while self.handValue() > 21 and self.checkAce11():
            for x in self.hand:
                if x[3] and x[0] == 11:
                    x[0] = 1
                    break

    def bust(self):
        print("%s has busted with %d." % (self.player_name, self.hand_value))
        self.turn = False

    def display(self):
        self.handValue()
        print("%s has %d." % (self.player_name, self.hand_value))


# creates dealer class that hits when it's hand is less than 17, stands otherwise
class Dealer:

    # initializes the starting value of the dealer's hand to be zero as a variable usable across the class
    hand_value = 0

    def __init__(self, hand, current_deck, turn):
        self.hand = hand
        self.current_deck = current_deck
        self.turn = turn

    # removes a card from the deck and puts it into the dealer's hand
    def hit(self):
        hit_card = self.current_deck.pop(int(random.uniform(0, len(self.current_deck))))
        self.hand.append(hit_card)
        print("Dealer hits and receives %s of %s." % (hit_card[1], hit_card[2]))

        # checks if hand is over 21 and doesn't contain any aces
        if self.handValue() > 21:
            if self.checkAce11():
                self.changeAce()
            else:
                self.bust()

    # ends the dealer's turn
    def stand(self):
        self.handValue()
        print("Dealer stands with %d." % self.handValue())
        self.turn = False

    # calculates the value of the dealer's hand
    def handValue(self):
        self.hand_value = 0
        for x in self.hand:
            self.hand_value += x[0]
        return self.hand_value

    # checks if there is an ace in hand and if the ace is valued at an 11
    def checkAce11(self):
        for x in self.hand:
            if x[3] and x[0] == 11:
                return True
        return False

    # used when hand value is over 21 to see if an ace can be changed into a 1
    def changeAce(self):
        while self.handValue() > 21 and self.checkAce11():
            for x in self.hand:
                if x[3] and x[0] == 11:
                    x[0] = 1
                    break

    def bust(self):
        print("Dealer has busted with %d." % self.hand_value)
        self.turn = False

    def display(self):
        self.handValue()
        print("Dealer has %d." % self.hand_value)


def main():

    # creates number of decks on player input
    num_deck = int(input("Enter number of decks: "))
    deck_class = Deck(num_deck)
    deck = deck_class.createDeck()

    # creates an empty list that will hold the player objects
    player_list = []

    # creates number of players and gives them a name on player input
    num_players = int(input("Enter number of players: "))

    # creates empty list of player names of type string
    player_names = []

    # uses user input to hold the value of the number of players (0 means the dealer is the only player)
    for x in range(num_players):
        player_names.append(input("Enter player %d's name: " % (x + 1)))

    # gives each player their starting hand with 2 cards each
    for x in range(num_players):
        temp_hand = []
        for y in range(2):
            temp_hand.append(deck.pop(int(random.uniform(0, len(deck)))))
        player_list.append(Player(player_names[x], temp_hand, deck, True))
        print("%s starts with %s of %s and %s of %s." % (player_list[x].player_name, temp_hand[0][1], temp_hand[0][2], temp_hand[1][1], temp_hand[1][2]))

    # creates the dealer with 1 card as it's starting hand
    dealer_hand = [deck.pop(int(random.uniform(0, len(deck))))]
    dealer = Dealer(dealer_hand, deck, True)
    print("Dealer starts with %s of %s." % (dealer_hand[0][1], dealer_hand[0][2]))
    print("Dealer has %d." % dealer.handValue())

    # creates the "turn based" aspect of the game starting with player 1 until the end of player_list
    for x in range(num_players):
        while player_list[x].turn:
            print("%s has %d." % (player_list[x].player_name, player_list[x].handValue()))
            player_choice = input("What would %s like to do? (h/s)" % player_list[x].player_name)
            if player_choice == 'h':
                player_list[x].hit()
            elif player_choice == 's':
                player_list[x].stand()

    # dealer plays (always hit until at least 17)
    while dealer.turn:
        if dealer.handValue() < 17:
            dealer.hit()
            dealer.display()
        else:
            dealer.stand()


main()
