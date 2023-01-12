from tkinter import Tk, BOTH, Canvas

# Game board display
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Blackjack")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="green", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

class Cards:
    def __init__(self):
        pass
    
class Chips:
    def __init__(self):
        pass
