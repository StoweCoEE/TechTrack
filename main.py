from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# Open tkinter GUI window and set dimensions and title
root = Tk()
root.geometry('1280x720')
root.title("TechTrack")

# Set GUI window icon and background color
root.config(background="#bcdfeb")
icon = PhotoImage(file='images\\techtrack_logo.png')
root.iconphoto(True, icon)

# Creates graphic with name and logo
tt_logo = Image.open('images\\techtrack_full.png').resize((394,197))
tt_logo_tk = ImageTk.PhotoImage(tt_logo)
logocanvas = Canvas(root, bg="#bcdfeb", bd=0, highlightthickness=0, width=394, height=197)
logocanvas.pack(pady=15)
logocanvas.create_image(0, 0, image=tt_logo_tk, anchor=NW)

# tkinter GUI loop runs application
root.mainloop()