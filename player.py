from deck import Deck, Hand

class Player:
    def __init__(self):
        self.hand = Hand()
    
    def draw_card(self, deck):
        single_card = deck.draw()
        self.hand.add_card(single_card)
        self.hand.adjust_for_ace()

class Dealer:
    def __init__(self):
        self.hand = Hand()
    
    def draw_card(self, deck):
        single_card = deck.draw()
        self.hand.add_card(single_card)
        self.hand.adjust_for_ace()

def show_cards(player,dealer):
    print("Player's Hand:")
    print(" ")
    print('',player.hand.cards[2])  
    print("\n")
    print("Dealer's Hand:")
    print(" <card hidden>")
    print('',dealer.hand.cards[1])  
    print("\n")

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
