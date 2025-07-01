from tkinter import *
from PIL import ImageTk, Image
import sqlite3

#Label(self,text="Test",bg="red")

class TechTrack(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('1280x720')
        self.title("TechTrack")
        self.config(background="#bcdfeb")
        self.resizable(False,False)
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
        self.config(background="#bcdfeb")

        # Establish a 32x18 grid. Each spot represents 40px.
        self.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                              17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32),weight=1)
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),weight=1)

        self.create_logo()
        Label(self, text="This is the start page").grid(row=1,column=16)
        Button(self, text="Add Asset",
               command=lambda: parent.switch_frame(AddAssetPage)).grid(row=8,column=16)
        Button(self, text="Add Worksite",
               command=lambda: parent.switch_frame(AddWorksitePage)).grid(row=10,column=10)
        Button(self, text="Update Asset/Worksite",
               command=lambda: parent.switch_frame(UpdatePage)).grid(row=10,column=20)
        Button(self, text="Delete Asset/Worksite",
               command=lambda: parent.switch_frame(DeletePage)).grid(row=13,column=10)
        Button(self, text="View Assets/Worksites",
               command=lambda: parent.switch_frame(ViewPage)).grid(row=13,column=20)
        
        
    def create_logo(self):
        global tt_logo_tk
        tt_logo = Image.open('images\\techtrack_full.png').resize((394,197))
        tt_logo_tk = ImageTk.PhotoImage(tt_logo)
        logocanvas = Canvas(self, bg="#bcdfeb", bd=0, highlightthickness=0, width=394, height=197)
        logocanvas.grid(row=0,column=16)
        logocanvas.create_image(0, 0, image=tt_logo_tk, anchor=NW)
        
class AddAssetPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#bcdfeb")
        
        # Establish a 32x18 grid. Each spot represents 40px.
        self.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                              17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32),weight=1)
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),weight=1)

        self.pin_icon()
        Label(self, text="Add Asset Page",font=20,bg="#9ed1e1",width=100).grid(row=0,column=2,sticky=NSEW)
        Button(self, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).grid(row=0,column=24,columnspan=8,sticky=NSEW)
        
    def pin_icon(self):
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(self, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.grid(row=0,column=0,sticky=NW)
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