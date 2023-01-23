from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Blackjack")
canvas = Canvas(root, bg="green", height=800, width=1200)
canvas.pack(fill=BOTH, expand=1)

ImageTk.PhotoImage(Image.open("Images/2_of_clubs.png"))
canvas.create_image(300, 400, image="Images/2_of_clubs.png")

root.mainloop()
