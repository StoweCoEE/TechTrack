from tkinter import *
from PIL import ImageTk, Image
import sqlite3


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

        # Set frames for banner and main content
        topFrame = Frame(self, bg="#bcdfeb")
        mainFrame = Frame(self, bg="#bcdfeb",width=1280,height=523)
        mainFrame.grid_propagate(False)
        topFrame.pack(side="top")
        mainFrame.pack(side="bottom")

        # Establish a 32x18 grid. Each spot represents 40px.
        topFrame.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                              17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32),weight=1)
        topFrame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),weight=1)

        # Establish a 32x18 grid. Each spot represents 40px.
        mainFrame.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                              17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32),weight=1)
        mainFrame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),weight=1)


        global tt_logo_tk
        tt_logo = Image.open('images\\techtrack_full.png').resize((394,197))
        tt_logo_tk = ImageTk.PhotoImage(tt_logo)
        logocanvas = Canvas(topFrame, bg="#bcdfeb", bd=0, highlightthickness=0, width=394, height=197)
        logocanvas.grid(row=0,column=16)
        logocanvas.create_image(0, 0, image=tt_logo_tk, anchor=NW)

        Button(mainFrame, text="View Assets/Worksites", width=20, height=5, font=20,
               command=lambda: parent.switch_frame(ViewPage)).grid(row=0,column=16,pady=20)
        Button(mainFrame, text="Add Asset", width=20, height=5,font=20,
               command=lambda: parent.switch_frame(AddAssetPage)).grid(row=6,column=12)
        Button(mainFrame, text="Add Worksite", width=20, height=5,font=20,
               command=lambda: parent.switch_frame(AddWorksitePage)).grid(row=6,column=20)
        Button(mainFrame, text="Update Asset/Worksite", width=20, height=5,font=20,
               command=lambda: parent.switch_frame(UpdatePage)).grid(row=13,column=12,pady=20)
        Button(mainFrame, text="Delete Asset/Worksite", width=20, height=5,font=20,
               command=lambda: parent.switch_frame(DeletePage)).grid(row=13,column=20)
        
class AddAssetPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#bcdfeb")
        
        # Set frames for banner and main content
        topFrame = Frame(self, bg="#9ed1e1")
        mainFrame = Frame(self, bg="#9ed1e1")
        topFrame.pack(side="top")
        mainFrame.pack(side="bottom")

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(topFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        #banner label and return button
        Label(topFrame, text="Add Asset Page",font=20,bg="#9ed1e1",width=100).pack(side="left",fill="y")
        Button(topFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
        # Establish a 32x18 grid. Each spot represents 40px.
        mainFrame.columnconfigure((0,1,2,3,4,5,6),weight=1)
        mainFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)

        # User Entry widgets
        Label(mainFrame,text="Asset Name:",font=20,bg="#9ed1e1",justify="right").grid(row=0,column=0)
        userEntry1 = Entry(mainFrame,font=20,relief=RIDGE,width=50)
        userEntry1.grid(row=0,column=1)
        Label(mainFrame,text="Asset Type:",font=20,bg="#9ed1e1",justify="right").grid(row=1,column=0)
        userEntry2 = Entry(mainFrame,font=20,relief=RIDGE,width=50)
        userEntry2.grid(row=1,column=1)
        Label(mainFrame,text="Asset Model No.:",font=20,bg="#9ed1e1",justify="right").grid(row=2,column=0)
        userEntry3 = Entry(mainFrame,font=20,relief=RIDGE,width=50)
        userEntry3.grid(row=2,column=1)
        Label(mainFrame,text="Purchase Date:",font=20,bg="#9ed1e1",justify="right").grid(row=3,column=0)
        userEntry4 = Entry(mainFrame,font=20,relief=RIDGE,width=50)
        userEntry4.grid(row=3,column=1)
        Label(mainFrame,text="Asset Asset:",font=20,bg="#9ed1e1",justify="right").grid(row=4,column=0)
        userEntry5 = Entry(mainFrame,font=20,relief=RIDGE,width=50)
        userEntry5.grid(row=4,column=1)
        
        # Button to submit Changes
        submitBtn = Button(mainFrame, text="Add Asset", font=20)
        submitBtn.grid(row=5,column=1)
        
class AddWorksitePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#bcdfeb")

        # Set frames for banner and main content
        topFrame = Frame(self, bg="#9ed1e1")
        mainFrame = Frame(self, bg="#9ed1e1")
        topFrame.pack(side="top")
        mainFrame.pack(side="bottom")

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(topFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        #banner label and return button
        Label(topFrame, text="Add Worksite Page",font=20,bg="#9ed1e1",width=100).pack(side="left",fill="y")
        Button(topFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
class UpdatePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#bcdfeb")

        # Set frames for banner and main content
        topFrame = Frame(self, bg="#9ed1e1")
        mainFrame = Frame(self, bg="#9ed1e1")
        topFrame.pack(side="top")
        mainFrame.pack(side="bottom")

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(topFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        #banner label and return button
        Label(topFrame, text="Update Page",font=20,bg="#9ed1e1",width=100).pack(side="left",fill="y")
        Button(topFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
class DeletePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#bcdfeb")

        # Set frames for banner and main content
        topFrame = Frame(self, bg="#9ed1e1")
        mainFrame = Frame(self, bg="#9ed1e1")
        topFrame.pack(side="top")
        mainFrame.pack(side="bottom")

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(topFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        #banner label and return button
        Label(topFrame, text="Delete Page",font=20,bg="#9ed1e1",width=100).pack(side="left",fill="y")
        Button(topFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
class ViewPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#bcdfeb")

        # Set frames for banner and main content
        topFrame = Frame(self, bg="#9ed1e1")
        mainFrame = Frame(self, bg="#9ed1e1")
        topFrame.pack(side="top")
        mainFrame.pack(side="bottom")

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(topFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        #banner label and return button
        Label(topFrame, text="View Page",font=20,bg="#9ed1e1",width=100).pack(side="left",fill="y")
        Button(topFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
if __name__ == "__main__":
    tt = TechTrack()
    tt = mainloop()