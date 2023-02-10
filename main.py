from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import random


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.root = Tk()
        self.root.title('Blackjack')
        self.root.geometry("900x500")
        self.root.configure(background="green")

        # Frames for the cards
        container = tk.Frame(self.root, bg="black", height=400, width=600)
        container.pack(pady=20)


class Dealer(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        # Dealer frame
        dealer_frame = LabelFrame(container=True, text="Dealer", bd=0)
        dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

        # Dealer label
        dealer_label = tk.Label(self)
        dealer_label.pack(pady=20)


class Player(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        # Player frame
        player_frame = LabelFrame(container=True, text="Player", bd=0)
        player_frame.grid(row=0, column=0, padx=20, ipadx=20)

        # Player label
        player_label = tk.Label(self)
        player_label.pack(pady=20)


# Suits and values for the cards
suits = ["diamonds", "clubs", "hearts", "spades"]
values = range(2, 15)
# 11=Jack, 12=Queen, 13=King, 14=Ace


class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def resize_cards(card):
        # Open image
        card_img = Image.open(card)
        # Resize image
        card_resize_image = card_img.resize((150, 218))
        # Display card
        card_image = ImageTk.PhotoImage(card_resize_image)
        # Return card
        return card_image
