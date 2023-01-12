from tkinter import Tk


class Window:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Blackjack")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.geometry("1200x800")
        self.__root.configure(background="black")