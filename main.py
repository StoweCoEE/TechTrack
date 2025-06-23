from tkinter import *
import sqlite3

window = Tk()
window.geometry("1280x720")
window.title("TechTrack")

window.config(background="#bcdfeb")
icon = PhotoImage(file='images\\techtrack_logo.png')
window.iconphoto(True, icon)

logo = PhotoImage(file='images\\techtrack_full.png')
logocanvas = Canvas(window, bg="#bcdfeb")
logocanvas.pack()

logocanvas.create_image(0,0,image=logo)
#testing to see if you see anything

window.mainloop()