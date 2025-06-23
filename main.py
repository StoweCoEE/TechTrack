from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# Open tkinter GUI window and set dimensions and title
root = Tk()
root.geometry("1280x720")
root.title("TechTrack")

# Set GUI window icon and background color
root.config(background="#bcdfeb")
icon = PhotoImage(file='images\\techtrack_logo.png')
root.iconphoto(True, icon)

# Creates graphic with name and logo
logo = PhotoImage(file='images\\techtrack_full.png')
logocanvas = Canvas(root, bg="#bcdfeb")
logocanvas.pack()
logocanvas.create_image(0,0,image=logo)

# tkinter GUI loop runs application
root.mainloop()