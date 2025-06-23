from tkinter import *
from PIL import ImageTk, Image
import sqlite3

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
        Label(self, text="This is the start page").pack()
        Button(self, text="Add Asset",
               command=lambda: parent.switch_frame(AddAssetPage)).pack()
        Button(self, text="Add Worksite",
               command=lambda: parent.switch_frame(AddWorksitePage)).pack()
        Button(self, text="Update Asset/Worksite",
               command=lambda: parent.switch_frame(UpdatePage)).pack()
        Button(self, text="Delete Asset/Worksite",
               command=lambda: parent.switch_frame(DeletePage)).pack()
        Button(self, text="View Assets/Worksites",
               command=lambda: parent.switch_frame(ViewPage)).pack()
        
        
    def create_logo(self):
        global tt_logo_tk
        tt_logo = Image.open('images\\techtrack_full.png').resize((394,197))
        tt_logo_tk = ImageTk.PhotoImage(tt_logo)
        logocanvas = Canvas(self, bg="#bcdfeb", bd=0, highlightthickness=0, width=394, height=197)
        logocanvas.pack()
        logocanvas.create_image(0, 0, image=tt_logo_tk, anchor=NW)
        
class AddAssetPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pin_icon()
        Label(self, text="Add Asset Page").pack(side="top", fill="x", pady=10)
        Button(self, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack()
        
    def pin_icon(self):
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((150,150))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(self, bg="#bcdfeb", bd=0, highlightthickness=0, width=150, height=150)
        iconcanvas.pack()
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)
        
class AddWorksitePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pin_icon()
        Label(self, text="Add Worksite Page").pack(side="top", fill="x", pady=10)
        Button(self, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack()
        
    def pin_icon(self):
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((150,150))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(self, bg="#bcdfeb", bd=0, highlightthickness=0, width=150, height=150)
        iconcanvas.pack()
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)
        
class UpdatePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pin_icon()
        Label(self, text="Update Page").pack(side="top", fill="x", pady=10)
        Button(self, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack()
        
    def pin_icon(self):
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((150,150))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(self, bg="#bcdfeb", bd=0, highlightthickness=0, width=150, height=150)
        iconcanvas.pack()
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)
        
class DeletePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pin_icon()
        Label(self, text="Delete Page").pack(side="top", fill="x", pady=10)
        Button(self, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack()
        
    def pin_icon(self):
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((150,150))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(self, bg="#bcdfeb", bd=0, highlightthickness=0, width=150, height=150)
        iconcanvas.pack()
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)
        
class ViewPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pin_icon()
        Label(self, text="View Page").pack(side="top", fill="x", pady=10)
        Button(self, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack()
        
    def pin_icon(self):
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((150,150))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(self, bg="#bcdfeb", bd=0, highlightthickness=0, width=150, height=150)
        iconcanvas.pack()
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)
        
if __name__ == "__main__":
    tt = TechTrack()
    tt = mainloop()