from tkinter import *
from PIL import ImageTk, Image
import sqlite3

"""
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
"""


class TechTrack(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('1280x720')
        self.title("TechTrack")
        self.config(background="#bcdfeb")
        icon = PhotoImage(file='images\\techtrack_logo.png')
        self.iconphoto(True, icon)

        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class HomePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.create_logo()
        Label(self, text="This is the start page").pack(pady=10)
        Button(self, text="Add Asset",
               command=lambda: parent.switch_frame(AddAssetPage)).pack()
        Button(self, text="Add Worksite",
               command=lambda: parent.switch_frame(AddWorksitePage)).pack()
        
        
    def create_logo(self):
        tt_logo = Image.open('images\\techtrack_full.png').resize((394,197))
        tt_logo_tk = ImageTk.PhotoImage(tt_logo)
        logocanvas = Canvas(self, bg="#bcdfeb", bd=0, highlightthickness=0, width=394, height=197)
        logocanvas.pack()
        logocanvas.create_image(0, 0, image=tt_logo_tk, anchor=NW)
        
class AddAssetPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="Add Asset Page").pack(side="top", fill="x", pady=10)
        Button(self, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack()
        
class AddWorksitePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        Label(self, text="Add Worksite Page").pack(side="top", fill="x", pady=10)
        Button(self, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack()
        
if __name__ == "__main__":
    tt = TechTrack()
    tt = mainloop()