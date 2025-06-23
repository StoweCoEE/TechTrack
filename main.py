from tkinter import *
import sqlite3

window = Tk()
window.geometry("1280x720")
window.title("TechTrack")

window.config(background="#bcdfeb")
icon = PhotoImage(file="techtrack_logo.png")
window.iconphoto(True, icon)

window.mainloop()