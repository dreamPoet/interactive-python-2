# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
dealer_hand = None
player_hand = None
outcome = "Hit or stand?"
result = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []      

    def __str__(self):
        # return a string representation of a hand
        string = "Hand contains "
        for i in range(len(self.cards)):
            string = string + self.cards[i].suit + str(self.cards[i].rank) + " "
        
        return string
            
    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        existed_Ace = False
        
        for card in self.cards:
            value += VALUES[card.rank]
            if card.rank == 'A':
                existed_Ace = True
                
        if existed_Ace and value + 10 <= 21:
            value += 10
        
        return value
            
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        if len(self.cards) > 5:
            n = 5
        else:
            n = len(self.cards)
            
        for i in range(n):
            # print pos
            # as draw is a continuous func, 
            # if use list, then the position  will change in each draw until final loop
            # X pos[0] = pos[0] + CARD_SIZE[0] + 10
            self.cards[i].draw(canvas, (pos[0] + i * CARD_SIZE[0] + i * 10, pos[1]))
    
  
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank)) 
        

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        string = "Deck contains "
        for i in range(len(self.cards)):
            string += str(self.cards[i]) + " "
            
        return string



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, score, result

    # your code goes here
    global dealer_hand, player_hand
    dealer_hand = Hand()
    player_hand = Hand()
    
    deck = Deck()
    deck.shuffle()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    if in_play:
        score -= 1
        result = "You lose."
        
    in_play = True
    result = ""
    outcome = "Hit or stand?"
    print "dealer: " + str(dealer_hand.get_value())
    print "player: " + str(player_hand.get_value())
    print

def hit():
    # replace with your code below
    global player_hand, dealer_hand
    global in_play, score, deck, outcome, result
    
    if not in_play:
        outcome = "New deal?"
        result = ""
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())
        outcome = "Hit or stand?"
        
    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "New deal?"
            score -= 1
            in_play = False
            result = "You went bust and lose."
       
        print "dealer: " + str(dealer_hand.get_value())
        print "player: " + str(player_hand.get_value())

    
def stand():
    # replace with your code below
    global player_hand, dealer_hand
    global in_play, score, deck, outcome, result
    
    if not in_play:
        outcome = "New deal?"
        result = ""
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
    
        if dealer_hand.get_value() > 21:
            outcome = "New deal?"
            score += 1
            in_play = False
            result = "Dealer went bust and you win."
    
        elif dealer_hand.get_value() >= player_hand.get_value():
            outcome = "New deal?"
            score -= 1
            result = "You lose."
        else:
            outcome = "New deal?"
            score += 1
            result = "You win."
        
    
        in_play = False
    
        print "dealer: " + str(dealer_hand.get_value())
        print "player: " + str(player_hand.get_value())
        print result
        print
    
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    
    canvas.draw_text("Blackjack", (120, 80), 35, 'Aqua')
    canvas.draw_text("Score " + str(score), (400, 80), 25, 'Black')
    
    canvas.draw_text("Dealer", (60, 150), 25, 'Black')
    canvas.draw_text(result, (260, 150), 25, 'Black')
    dealer_hand.draw(canvas, (60, 170))
    
    canvas.draw_text("Player", (60, 400), 25, 'Black')
    canvas.draw_text(outcome, (260, 400), 25, 'Black')
    player_hand.draw(canvas, (60, 420))

            
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [60 + CARD_BACK_CENTER[0], 170 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
             

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric