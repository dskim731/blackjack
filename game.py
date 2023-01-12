from deck import Deck, Hand
import random


class Game:
    user_score = 0
    dealer_score = 0
    
    def __init__(self):
        self.deck = Deck()
        self.user_hand = Hand()
        self.dealer_hand = Hand()
        