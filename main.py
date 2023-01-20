from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title("Blackjack")
canvas = Canvas(root, bg="green", height=1200, width=800)
canvas.pack(fill=BOTH, expand=1)

img = ImageTk.PhotoImage(Image.open("gui/images/cards/2_of_clubs.png"))
canvas.create_image(0, 0, image=img, anchor="nw")


def shuffle():
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    global dealer, player
    dealer = []
    player = []

    # Grab a random Card For Dealer
    card = random.choice(deck)
    # Remove Card From Deck
    deck.remove(card)
    # Append Card To Dealer List
    dealer.append(card)
    # Output Card To Screen
    global dealer_image
    dealer_image = resize_cards(f'images/cards/{card}.png')
    dealer_label.config(image=dealer_image)

    # Grab a random Card For Player
    card = random.choice(deck)
    # Remove Card From Deck
    deck.remove(card)
    # Append Card To Dealer List
    player.append(card)
    # Output Card To Screen
    global player_image
    player_image = resize_cards(f'images/cards/{card}.png')
    player_label.config(image=player_image)

    root.title(f'{len(deck)} Cards Left')


def deal_cards():
    try:
        # Dealer card
        card = random.choice(deck)
        deck.remove(card)
        # Append Card To Dealer List
        dealer.append(card)
        # Output Card To Screen
        global dealer_image
        dealer_image = resize_cards(f'images/cards/{card}.png')
        dealer_label.config(image=dealer_image)

        # Player Card
        card = random.choice(deck)
        # Remove Card From Deck
        deck.remove(card)
        # Append Card To Dealer List
        player.append(card)
        # Output Card To Screen
        global player_image
        player_image = resize_cards(f'images/cards/{card}.png')
        player_label.config(image=player_image)
        # player_label.config(text=card)

        # Put number of remaining cards in title bar
        root.title(f'{len(deck)} Cards Left')

    except:
        root.title(f'No Cards In Deck')


root.mainloop()
