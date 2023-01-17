from main import Cards
from deck import Deck
import random

class Player:
    def __init__(self):
        self.hand = []

class Dealer:
    def __init__(self):
        self.hand = []
    
class Deal_Card:    
    def deal_cards(self):
        try:
            # Get the Dealer Card
            card = random.choice(deck)
            # Remove Card From Deck
            deck.remove(card)
            # Append Card To Dealer List
            dealer.append(card)
            # Output Card To Screen
            global dealer_image
            dealer_image = resize_cards(f'images/cards/{card}.png')
            dealer_label.config(image=dealer_image)
            #dealer_label.config(text=card)

            # Get the player Card
            card = random.choice(deck)
            # Remove Card From Deck
            deck.remove(card)
            # Append Card To Dealer List
            player.append(card)
            # Output Card To Screen
            global player_image
            player_image = resize_cards(f'images/cards/{card}.png')
            player_label.config(image=player_image)
            #player_label.config(text=card)


            # Put number of remaining cards in title bar
            root.title(f'{len(deck)} Cards Left')

        except:
            root.title("No Cards In Deck")