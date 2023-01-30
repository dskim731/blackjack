from main import Card
import random

dealer = []
player = []

suits = ["diamonds", "clubs", "hearts", "spades"]
values = range(2, 15)
# 11 = Jack, 12=Queen, 13=King, 14 = Ace


class Deck:
    def __init__(self):
        pass

    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    # Grab a random Card For Dealer
    card = random.choice(deck)
    # Remove Card From Deck
    deck.remove(card)
    # Append Card To Dealer List
    dealer.append(card)
    # Output Card To Screen
    global dealer_image
    dealer_image = resize_cards(f'images/{card}.png')
    dealer_label.config(image=dealer_image)

    # Grab a random Card For Player
    card = random.choice(deck)
    # Remove Card From Deck
    deck.remove(card)
    # Append Card To Dealer List
    player.append(card)
    # Output Card To Screen
    global player_image
    player_image = resize_cards(f'images/{card}.png')
    player_label.config(image=player_image)

    # player_label.config(text=card)

    # Put number of remaining cards in title bar
    root.title(f'{len(deck)} Cards Left')


# Deal Out Cards
def deal_cards():
    try:
        # Get the deler Card
        card = random.choice(deck)
        # Remove Card From Deck
        deck.remove(card)
        # Append Card To Dealer List
        dealer.append(card)
        # Output Card To Screen
        global dealer_image
        dealer_image = resize_cards(f'images/{card}.png')
        dealer_label.config(image=dealer_image)
        # dealer_label.config(text=card)

        # Get the player Card
        card = random.choice(deck)
        # Remove Card From Deck
        deck.remove(card)
        # Append Card To Dealer List
        player.append(card)
        # Output Card To Screen
        global player_image
        player_image = resize_cards(f'images/{card}.png')
        player_label.config(image=player_image)
        # player_label.config(text=card)

        # Put number of remaining cards in title bar
        root.title(f'{len(deck)} Cards Left')

    except:
        root.title(f'No Cards In Deck')
