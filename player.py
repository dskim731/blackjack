from main import Cards
from deck import Deck
import random

class Player:
    def __init__(self):
        self.hand = []

class Dealer:
    def __init__(self):
        self.hand = []
    
    def deal_card(self):
        card = random.choice(deck)
    # Remove Card From Deck
    deck.remove(card)
    # Append Card To Dealer List
    dealer.append(card)
    # Output Card To Screen
    global dealer_image
    dealer_image = resize_cards(f'images/cards/{card}.png')
    dealer_label.config(image=dealer_image)