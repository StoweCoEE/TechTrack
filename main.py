from tkinter import *
from PIL import ImageTk, Image
import sqlite3


##
## SQLITE DATABASE INITIATION (TO BE ADDED LATER)
##

#dataBase = sqlite3.connect('TechTrackDB')
#cursor = dataBase.cursor()


##
## WIDGET FUNCTION DEFINITIONS
##

def EntitySearchClick():
    print("EntitySearchClick")

def AssetSearchClick():
    print("AssetSearchClick")

def WorksiteSearchClick():
    print("WorksiteSearchClick")

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

        ##
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#bcdfeb")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=197)
        contentFrame.config(width=1220,height=503)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        contentFrame.pack(side="bottom")
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
        contentFrame.rowconfigure((0,1,2,3,4,5,6),weight=1)


        ##
        ## WIDGET SETTINGS
        ##

        # banner icon creation
        global tt_logo_tk
        tt_logo = Image.open('images\\techtrack_full.png').resize((394,197))
        tt_logo_tk = ImageTk.PhotoImage(tt_logo)
        logocanvas = Canvas(headerFrame, bg="#bcdfeb", bd=0, highlightthickness=0, width=394, height=197)
        logocanvas.pack()
        logocanvas.create_image(0, 0, image=tt_logo_tk, anchor=NW)

        # Create and Place Navigation Buttons
        Button(contentFrame, text="View Assets/Worksites", width=20, height=3, font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(ViewPage)).grid(row=1,column=5)
        Button(contentFrame, text="Add Asset", width=20, height=3,font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(AddAssetPage)).grid(row=3,column=2,sticky=E)
        Button(contentFrame, text="Add Worksite", width=20, height=3,font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(AddWorksitePage)).grid(row=3,column=8,sticky=W)
        Button(contentFrame, text="Update Asset/Worksite", width=20, height=3,font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(UpdatePage)).grid(row=5,column=2,sticky=E)
        Button(contentFrame, text="Delete Asset/Worksite", width=20, height=3,font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(DeletePage)).grid(row=5,column=8,sticky=W)
        
class AddAssetPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        ##
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#bcdfeb")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=100)
        contentFrame.config(width=1220,height=600)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        contentFrame.pack(side="bottom")
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6),weight=1)
        contentFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)


        ##
        ## WIDGET SETTINGS
        ##

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(headerFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        # banner label and return button
        Label(headerFrame, text="Add an Asset",font=('Arial',36,'bold'),bg="#9ed1e1",width=33).pack(side="left")
        Button(headerFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")

        # Create and Place Labels and User-Entry Widgets
        Label(contentFrame,text="Asset Name:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20).grid(row=1,column=0)
        userEntry1 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry1.insert(0,'(Enter Asset Name)')
        userEntry1.bind("<FocusIn>", lambda args: userEntry1.delete('0', 'end'))
        userEntry1.grid(row=1,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Asset Type:",font=('Arial',26),bg="#bcdfeb",justify="right").grid(row=2,column=0)
        userEntry2 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry2.insert(0,'(Enter Asset Type)')
        userEntry2.bind("<FocusIn>", lambda args: userEntry2.delete('0', 'end'))
        userEntry2.grid(row=2,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Asset Model Number:",font=('Arial',26),bg="#bcdfeb",justify="right").grid(row=3,column=0)
        userEntry3 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry3.insert(0,'(Enter Asset Model Number)')
        userEntry3.bind("<FocusIn>", lambda args: userEntry3.delete('0', 'end'))
        userEntry3.grid(row=3,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Purchase Date:",font=('Arial',26),bg="#bcdfeb",justify="right").grid(row=4,column=0)
        userEntry4 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry4.insert(0,'(Enter Asset Purchase Date)')
        userEntry4.bind("<FocusIn>", lambda args: userEntry4.delete('0', 'end'))
        userEntry4.grid(row=4,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Asset Cost:",font=('Arial',26),bg="#bcdfeb",justify="right").grid(row=5,column=0)
        userEntry5 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry5.insert(0,'(Enter Asset Cost)')
        userEntry5.bind("<FocusIn>", lambda args: userEntry5.delete('0', 'end'))
        userEntry5.grid(row=5,column=1,columnspan=3,sticky=W)
        
        # Button to submit Changes
        submitBtn = Button(contentFrame, text="Add Asset", font=('Arial',20))
        submitBtn.grid(row=7,column=0,columnspan=7)
        
class AddWorksitePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        ##
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#bcdfeb")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=100)
        contentFrame.config(width=1220,height=600)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        contentFrame.pack(side="bottom")
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6),weight=1)
        contentFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)


        ##
        ## WIDGET SETTINGS
        ##

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(headerFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        #banner label and return button
        Label(headerFrame, text="Add a Worksite",font=('Arial',36,'bold'),bg="#9ed1e1",width=33).pack(side="left")
        Button(headerFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
        # Create and Place Labels and User-Entry Widgets
        Label(contentFrame,text="Order ID:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20).grid(row=1,column=0)
        userEntry1 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry1.insert(0,'(Enter Worksite Name)')
        userEntry1.bind("<FocusIn>", lambda args: userEntry1.delete('0', 'end'))
        userEntry1.grid(row=1,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Worksite Type:",font=('Arial',26),bg="#bcdfeb",justify="right").grid(row=2,column=0)
        userEntry2 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry2.insert(0,'(Enter Worksite Type)')
        userEntry2.bind("<FocusIn>", lambda args: userEntry2.delete('0', 'end'))
        userEntry2.grid(row=2,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Worksite Address:",font=('Arial',26),bg="#bcdfeb",justify="right").grid(row=3,column=0)
        userEntry3 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry3.insert(0,'(Enter Worksite Address)')
        userEntry3.bind("<FocusIn>", lambda args: userEntry3.delete('0', 'end'))
        userEntry3.grid(row=3,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Worksite City:",font=('Arial',26),bg="#bcdfeb",justify="right").grid(row=4,column=0)
        userEntry4 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry4.insert(0,'(Enter Worksite City)')
        userEntry4.bind("<FocusIn>", lambda args: userEntry4.delete('0', 'end'))
        userEntry4.grid(row=4,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Worksite Zip:",font=('Arial',26),bg="#bcdfeb",justify="right").grid(row=5,column=0)
        userEntry5 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry5.insert(0,'(Enter Worksite Zip Code)')
        userEntry5.bind("<FocusIn>", lambda args: userEntry5.delete('0', 'end'))
        userEntry5.grid(row=5,column=1,columnspan=3,sticky=W)
        
        # Button to submit Changes
        submitBtn = Button(contentFrame, text="Add Worksite", font=('Arial',20))
        submitBtn.grid(row=7,column=0,columnspan=7)
        
class UpdatePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        ##
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#bcdfeb")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=100)
        contentFrame.config(width=1220,height=600)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        contentFrame.pack(side="bottom")
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6),weight=1)
        contentFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)


        ##
        ## WIDGET SETTINGS
        ##

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(headerFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        #banner label and return button
        Label(headerFrame, text="Update Entity",font=('Arial',36,'bold'),bg="#9ed1e1",width=33).pack(side="left")
        Button(headerFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
        # Search Bar and Button
        Label(contentFrame,text="Asset/Worksite ID:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20).grid(row=0,column=0)
        searchEntry1 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=38)
        searchEntry1.grid(row=0,column=1,columnspan=3,sticky=W)
        searchBtn = Button(contentFrame, text="Search", font=('Arial',20))
        searchBtn.config(command=EntitySearchClick)
        searchBtn.grid(row=0,column=4, sticky=W)

class DeletePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        ##
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#bcdfeb")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=100)
        contentFrame.config(width=1220,height=600)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        contentFrame.pack(side="bottom")
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6),weight=1)
        contentFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)


        ##
        ## WIDGET SETTINGS
        ##

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(headerFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        #banner label and return button
        Label(headerFrame, text="Delete an Entity",font=('Arial',36,'bold'),bg="#9ed1e1",width=33).pack(side="left")
        Button(headerFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
        # Search Entry Bar and Button
        Label(contentFrame,text="Asset/Worksite ID:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20).grid(row=0,column=0)
        searchEntry1 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=38)
        searchEntry1.grid(row=0,column=1,columnspan=3,sticky=W)
        searchBtn = Button(contentFrame, text="Search", font=('Arial',20))
        searchBtn.grid(row=0,column=4, sticky=W)
        
class ViewPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        ##
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#9ed1e1")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=100)
        contentFrame.config(width=1220,height=600)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        contentFrame.pack(side="bottom")
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6),weight=1)
        contentFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)


        ##
        ## WIDGET SETTINGS
        ##

        # banner icon creation
        global tt_icon_tk
        tt_icon = Image.open('images\\techtrack_icon.png').resize((100,100))
        tt_icon_tk = ImageTk.PhotoImage(tt_icon)
        iconcanvas = Canvas(headerFrame, bg="#9ed1e1", bd=0, highlightthickness=0,height=100,width=100)
        iconcanvas.pack(side="left")
        iconcanvas.create_image(0, 0, image=tt_icon_tk, anchor=NW)

        #banner label and return button
        Label(headerFrame, text="Entity Viewer",font=('Arial',36,'bold'),bg="#9ed1e1",width=33).pack(side="left")
        Button(headerFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
        # Button to View DB info by Assets or Worksites
        viewAssetBtn = Button(contentFrame, text="View Assets", font=('Arial',20))
        viewAssetBtn.grid(row=0,column=0,columnspan=3)
        viewWorksiteBtn = Button(contentFrame, text="View Worksites", font=('Arial',20))
        viewWorksiteBtn.grid(row=0,column=4,columnspan=3)
        
if __name__ == "__main__":
    tt = TechTrack()
    tt = mainloop()