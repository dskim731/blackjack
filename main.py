from tkinter import *
import random
from PIL import Image, ImageTk


# Game board display
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Blackjack")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.geometry("1200x800")
        self.__root.configure(background="green")
        

class Cards:
    def __init__(self):
        pass
    
    # Resize Cards
    def resize_cards(card):
        # Open the Image
        card_img = Image.open(card)

        # Resize The Image
        card_resize_image = card_img.resize((150, 218))
        
        global card_image
        card_image = ImageTk.PhotoImage(card_resize_image)

        return card_image
    
class Chips:
    def __init__(self):
        pass
