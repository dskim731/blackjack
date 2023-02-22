from tkinter import *
import random
from PIL import Image, ImageTk


root = Tk()
root.title("Blackjack")
root.geometry("900x500")
root.configure(background="green")


def resize_cards(card):
    # Open the image
    my_card_img = Image.open(card)

    # Resize image
    card_resize_image = my_card_img.resize((150, 218))

    # Display card image
    global card_image
    card_image = ImageTk.PhotoImage(card_resize_image)

    return card_image


def shuffle():
    # Deck function
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)
    # 11=Jack, 12=Queen, 13=King, 14=Ace

    global deck
    deck = []

    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    # Create player and dealer
    global dealer, player
    dealer = []
    player = []

    # Dealer deal card
    card = random.choice(deck)
    # Remove Card From Deck
    deck.remove(card)
    # Append Card To Dealer List
    dealer.append(card)
    # Output Card To Screen
    global dealer_image
    dealer_image = resize_cards(f'images/{card}.png')
    dealer_label.config(image=dealer_image)

    # Deal player card
    card = random.choice(deck)
    # Remove Card From Deck
    deck.remove(card)
    # Append Card To Dealer List
    player.append(card)
    # Output Card To Screen
    global player_image
    player_image = resize_cards(f'images/{card}.png')
    player_label.config(image=player_image)

    # Number of cards left in the deck
    root.title(f'{len(deck)} cards left')


# Deal Out Cards
def deal_cards():
    try:
        # Get the Dealer Card
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

        # Get the Player Card
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


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

# Put cards in frames
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)


# Create a couple buttons
shuffle_button = Button(root, text="Shuffle Deck",
                        font=("Arial", 14), command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=(
    "Arial", 14), command=deal_cards)
card_button.pack(pady=20)


# Shuffle Deck On Start
shuffle()


root.mainloop()
