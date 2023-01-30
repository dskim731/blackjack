from tkinter import *
from PIL import Image, ImageTk


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Blackjack')
        self.root.geometry("900x500")
        self.root.configure(background="green")


class Card:
    def __init__(self):
        pass

    def resize_cards(self, card):
        # Open image
        card_img = Image.open(card)
        # Resize image
        card_resize_image = card_img.resize((150, 218))
        # Card
        self.card_image = ImageTk.PhotoImage(card_resize_image)
        # Return card
        return self.card_image

    # Frame
    my_frame = Frame(self.root, bg="green")
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
    shuffle_button = Button(self.root, text="Shuffle Deck",
                            font=("Helvetica", 14), command=shuffle)
    shuffle_button.pack(pady=20)

    card_button = Button(self.root, text="Get Cards", font=(
        "Helvetica", 14), command=deal_cards)
    card_button.pack(pady=20)

    # Shuffle Deck On Start
    shuffle()

    root.mainloop()
