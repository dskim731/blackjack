from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Blackjack")
canvas = Canvas(root, bg="green", height=800, width=1200)
canvas.pack(fill=BOTH, expand=1)

img = ImageTk.PhotoImage(Image.open("images/2_of_clubs.png"))
canvas.create_image(0, 0, image=img, anchor="nw")

root.mainloop()
