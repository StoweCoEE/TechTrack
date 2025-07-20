from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
import database

conn = database.connect()
database.initialize(conn)

##============================================================
## TKNINTER WINDOW CLASS
##

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

##============================================================
## TKINTER FRAME CLASSES
##

class HomePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ##============================================================
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


        ##============================================================
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
               command=lambda: parent.switch_frame(ViewPage)).grid(row=5,column=7)
        Button(contentFrame, text="Add Asset", width=20, height=3,font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(AddAssetPage)).grid(row=1,column=3)
        Button(contentFrame, text="Add Worksite", width=20, height=3,font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(AddWorksitePage)).grid(row=1,column=7)
        Button(contentFrame, text="Update Asset/Worksite", width=20, height=3,font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(UpdatePage)).grid(row=3,column=3)
        Button(contentFrame, text="Delete Asset/Worksite", width=20, height=3,font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(DeletePage)).grid(row=3,column=7)
        Button(contentFrame, text="Add Assignment", width=20, height=3,font=('Arial',16,'bold'),
               command=lambda: parent.switch_frame(AssignmentPage)).grid(row=5,column=3)
        
class AddAssetPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        placeholder1 = "(Enter Asset Name)"
        placeholder2 = "(Enter Asset Type)"
        placeholder3 = "(Enter Asset Model Number)"
        placeholder4 = "(Enter Asset Purchase Date)"
        placeholder5 = "(Enter Asset Cost)"

        ##============================================================
        ## WIDGET FUNCTION SETTINGS
        ##

        def addAssetClick(entry1, entry2, entry3, entry4, entry5):
            assetName = entry1.get()
            assetType = entry2.get()
            assetModelNo = entry3.get()
            assetPurchaseDate = entry4.get()
            assetCost = entry5.get()

            if (len(assetName) == 0 or len(assetType) == 0 or len(assetModelNo) == 0 or len(assetPurchaseDate) == 0 or len(assetCost) == 0):
                messagebox.showerror("Error","Entry Data Was Missing")
                userEntry1.delete(0,END)
                userEntry2.delete(0,END)
                userEntry3.delete(0,END)
                userEntry4.delete(0,END)
                userEntry5.delete(0,END)
            elif (assetName == placeholder1 or assetType == placeholder2 or assetModelNo == placeholder3 or assetPurchaseDate == placeholder4 or assetCost == placeholder5):
                messagebox.showerror("Error","Placeholder Text Entered")
                userEntry1.delete(0,END)
                userEntry2.delete(0,END)
                userEntry3.delete(0,END)
                userEntry4.delete(0,END)
                userEntry5.delete(0,END)
            else:
                database.addAsset(conn, assetType, assetName, assetCost, assetPurchaseDate, assetModelNo)
                messagebox.showinfo("Success","Asset Added Successfully")
                userEntry1.delete(0,END)
                userEntry2.delete(0,END)
                userEntry3.delete(0,END)
                userEntry4.delete(0,END)
                userEntry5.delete(0,END)
        
        ##============================================================
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

        ##============================================================
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
        Label(contentFrame,text="Asset Name:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20
              ).grid(row=1,column=0)
        userEntry1 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry1.insert(0,placeholder1)
        userEntry1.bind("<FocusIn>", lambda args: userEntry1.delete('0', 'end'))
        userEntry1.grid(row=1,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Asset Type:",font=('Arial',26),bg="#bcdfeb",justify="right"
              ).grid(row=2,column=0)
        userEntry2 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry2.insert(0,placeholder2)
        userEntry2.bind("<FocusIn>", lambda args: userEntry2.delete('0', 'end'))
        userEntry2.grid(row=2,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Asset Model Number:",font=('Arial',26),bg="#bcdfeb",justify="right"
              ).grid(row=3,column=0)
        userEntry3 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry3.insert(0,placeholder3)
        userEntry3.bind("<FocusIn>", lambda args: userEntry3.delete('0', 'end'))
        userEntry3.grid(row=3,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Purchase Date (YYYYMMDD):",font=('Arial',26),bg="#bcdfeb",justify="right"
              ).grid(row=4,column=0)
        userEntry4 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry4.insert(0,placeholder4)
        userEntry4.bind("<FocusIn>", lambda args: userEntry4.delete('0', 'end'))
        userEntry4.grid(row=4,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Asset Cost:",font=('Arial',26),bg="#bcdfeb",justify="right"
              ).grid(row=5,column=0)
        userEntry5 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry5.insert(0,placeholder5)
        userEntry5.bind("<FocusIn>", lambda args: userEntry5.delete('0', 'end'))
        userEntry5.grid(row=5,column=1,columnspan=3,sticky=W)
        
        # Button to submit Changes
        submitBtn = Button(contentFrame, text="Add Asset", font=('Arial',20),command=lambda: addAssetClick(userEntry1, userEntry2, userEntry3, userEntry4, userEntry5))
        submitBtn.grid(row=7,column=0,columnspan=7)
        
class AddWorksitePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        placeholder1 = "(Enter Order ID)"
        placeholder2 = "(Enter Worksite Type)"
        placeholder3 = "(Enter Worksite Address)"
        placeholder4 = "(Enter Worksite City)"
        placeholder5 = "(Enter Worksite Zip Code)"

        ##============================================================
        ## WIDGET FUNCTION SETTINGS
        ##

        def addWorksiteClick(entry1, entry2, entry3, entry4, entry5):
            orderID = entry1.get()
            worksiteType = entry2.get()
            worksiteAddress = entry3.get()
            worksiteCity = entry4.get()
            worksiteZip = entry5.get()

            if (len(orderID) == 0 or len(worksiteType) == 0 or len(worksiteAddress) == 0 or len(worksiteCity) == 0 or len(worksiteZip) == 0):
                messagebox.showerror("Error","Entry Data Was Missing")
                userEntry1.delete(0,END)
                userEntry2.delete(0,END)
                userEntry3.delete(0,END)
                userEntry4.delete(0,END)
                userEntry5.delete(0,END)
            elif (orderID == placeholder1 or worksiteType == placeholder2 or worksiteAddress == placeholder3 or worksiteCity == placeholder4 or worksiteZip == placeholder5):
                messagebox.showerror("Error","Placeholder Text Entered")
                userEntry1.delete(0,END)
                userEntry2.delete(0,END)
                userEntry3.delete(0,END)
                userEntry4.delete(0,END)
                userEntry5.delete(0,END)
            else:
                database.addWorksite(conn, orderID, worksiteType, worksiteAddress, worksiteCity, worksiteZip)
                messagebox.showinfo("Success","Worksite Added Successfully")
                userEntry1.delete(0,END)
                userEntry2.delete(0,END)
                userEntry3.delete(0,END)
                userEntry4.delete(0,END)
                userEntry5.delete(0,END)
        
        ##============================================================
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

        ##============================================================
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
        Label(headerFrame, text="Add a Worksite",font=('Arial',36,'bold'),bg="#9ed1e1",width=33
              ).pack(side="left")
        Button(headerFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
        # Create and Place Labels and User-Entry Widgets
        Label(contentFrame,text="Order ID:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20
              ).grid(row=1,column=0)
        userEntry1 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry1.insert(0,placeholder1)
        userEntry1.bind("<FocusIn>", lambda args: userEntry1.delete('0', 'end'))
        userEntry1.grid(row=1,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Worksite Type:",font=('Arial',26),bg="#bcdfeb",justify="right"
              ).grid(row=2,column=0)
        userEntry2 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry2.insert(0,placeholder2)
        userEntry2.bind("<FocusIn>", lambda args: userEntry2.delete('0', 'end'))
        userEntry2.grid(row=2,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Worksite Address:",font=('Arial',26),bg="#bcdfeb",justify="right"
              ).grid(row=3,column=0)
        userEntry3 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry3.insert(0,placeholder3)
        userEntry3.bind("<FocusIn>", lambda args: userEntry3.delete('0', 'end'))
        userEntry3.grid(row=3,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Worksite City:",font=('Arial',26),bg="#bcdfeb",justify="right"
              ).grid(row=4,column=0)
        userEntry4 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry4.insert(0,placeholder4)
        userEntry4.bind("<FocusIn>", lambda args: userEntry4.delete('0', 'end'))
        userEntry4.grid(row=4,column=1,columnspan=3,sticky=W)
        Label(contentFrame,text="Worksite Zip:",font=('Arial',26),bg="#bcdfeb",justify="right"
              ).grid(row=5,column=0)
        userEntry5 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=50)
        userEntry5.insert(0,placeholder5)
        userEntry5.bind("<FocusIn>", lambda args: userEntry5.delete('0', 'end'))
        userEntry5.grid(row=5,column=1,columnspan=3,sticky=W)
        
        # Button to submit Changes
        submitBtn = Button(contentFrame, text="Add Worksite", font=('Arial',20),command=lambda: addWorksiteClick(userEntry1, userEntry2, userEntry3, userEntry4, userEntry5))
        submitBtn.grid(row=7,column=0,columnspan=7)
        
class UpdatePage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        def searchOneAsset():
            assetID = searchEntry1.get()

            if assetID == "":
                messagebox.showerror("Missing Entry","Please Enter an Entity ID")
                searchEntry1.delete(0,END)
            else:
                foundLabel = Label(resultFrame,text="Asset Found:",font=('Arial',20),bg="#bcdfeb")
                foundLabel.grid(row=0,column=0,columnspan=7)
                searchResult=database.viewOneAsset(conn, assetID)

                label0 = Label(resultFrame,text="Asset ID:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20)
                label0.grid(row=1,column=0,columnspan=3)
                userEntry0 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry0.insert(0,searchResult[0])
                userEntry0.config(state="readonly")
                userEntry0.grid(row=1,column=3,columnspan=3,sticky=W)

                label1 = Label(resultFrame,text="Asset Name:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20)
                label1.grid(row=2,column=0,columnspan=3)
                userEntry1 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry1.insert(0,searchResult[2])
                userEntry1.grid(row=2,column=3,columnspan=3,sticky=W)

                label2 = Label(resultFrame,text="Asset Type:",font=('Arial',26),bg="#bcdfeb",justify="right")
                label2.grid(row=3,column=0,columnspan=3)
                userEntry2 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry2.insert(0,searchResult[1])
                userEntry2.grid(row=3,column=3,columnspan=3,sticky=W)

                label3 = Label(resultFrame,text="Asset Model Number:",font=('Arial',26),bg="#bcdfeb",justify="right")
                label3.grid(row=4,column=0,columnspan=3)
                userEntry3 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry3.insert(0,searchResult[5])
                userEntry3.grid(row=4,column=3,columnspan=3,sticky=W)

                label4 = Label(resultFrame,text="Purchase Date (YYYYMMDD):",font=('Arial',26),bg="#bcdfeb",justify="right")
                label4.grid(row=5,column=0,columnspan=3)
                userEntry4 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry4.insert(0,searchResult[4])
                userEntry4.grid(row=5,column=3,columnspan=3,sticky=W)

                label5 = Label(resultFrame,text="Asset Cost:",font=('Arial',26),bg="#bcdfeb",justify="right")
                label5.grid(row=6,column=0,columnspan=3)
                userEntry5 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry5.insert(0,searchResult[3])
                userEntry5.grid(row=6,column=3,columnspan=3,sticky=W)
                
                searchOneAssetBtn.config(state=DISABLED)
                searchOneWorksiteBtn.config(state=DISABLED)

                confirmAssetBtn = Button(resultFrame, text="Confirm Update", font=('Arial',20),
                                         command=lambda: UpdateAsset())
                confirmAssetBtn.grid(row=7,column=0,columnspan=4)

                resetAssetBtn = Button(resultFrame, text="Reset", font=('Arial',20),command=lambda: resetAsset())
                resetAssetBtn.grid(row=7,column=4,columnspan=4)

            def UpdateAsset():
                assetID=userEntry0.get()
                assetType=userEntry2.get()
                assetName=userEntry1.get()
                assetCost=userEntry5.get()
                assetPurchase=userEntry4.get()
                assetModel=userEntry3.get()
                database.deleteAsset(conn, assetID)
                database.updateAsset(conn, assetID,assetType,assetName,assetCost,assetPurchase,assetModel)
                messagebox.showinfo("Update Success","Asset Updated Successfully")
                foundLabel.destroy()
                label0.destroy()
                label1.destroy()
                label2.destroy()
                label3.destroy()
                label4.destroy()
                label5.destroy()
                userEntry0.destroy()
                userEntry1.destroy()
                userEntry2.destroy()
                userEntry3.destroy()
                userEntry4.destroy()
                userEntry5.destroy()
                resetAssetBtn.destroy()
                confirmAssetBtn.destroy()
                searchOneAssetBtn.config(state=ACTIVE)
                searchOneWorksiteBtn.config(state=ACTIVE)
                searchEntry1.delete(0,END)

            def resetAsset():
                foundLabel.destroy()
                label0.destroy()
                label1.destroy()
                label2.destroy()
                label3.destroy()
                label4.destroy()
                label5.destroy()
                userEntry0.destroy()
                userEntry1.destroy()
                userEntry2.destroy()
                userEntry3.destroy()
                userEntry4.destroy()
                userEntry5.destroy()
                resetAssetBtn.destroy()
                confirmAssetBtn.destroy()
                searchOneAssetBtn.config(state=ACTIVE)
                searchOneWorksiteBtn.config(state=ACTIVE)
                searchEntry1.delete(0,END)

        def searchOneWorksite():
            worksiteID = searchEntry1.get()

            if worksiteID == "":
                messagebox.showerror("Missing Entry","Please Enter an Entity ID")
                searchEntry1.delete(0,END)
            else:
                foundLabel = Label(resultFrame,text="Worksite Found:",font=('Arial',20),bg="#bcdfeb")
                foundLabel.grid(row=0,column=0,columnspan=7)
                searchResult=database.viewOneWorksite(conn, worksiteID)

                label0 = Label(resultFrame,text="Worksite ID:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20)
                label0.grid(row=1,column=0,columnspan=3)
                userEntry0 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry0.insert(0,searchResult[0])
                userEntry0.config(state="readonly")
                userEntry0.grid(row=1,column=3,columnspan=3,sticky=W)

                label1 = Label(resultFrame,text="Order ID:",font=('Arial',26),bg="#bcdfeb",justify="right",width=20)
                label1.grid(row=2,column=0,columnspan=3)
                userEntry1 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry1.insert(0,searchResult[1])
                userEntry1.grid(row=2,column=3,columnspan=3,sticky=W)

                label2 = Label(resultFrame,text="Worksite Type:",font=('Arial',26),bg="#bcdfeb",justify="right")
                label2.grid(row=3,column=0,columnspan=3)
                userEntry2 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry2.insert(0,searchResult[2])
                userEntry2.grid(row=3,column=3,columnspan=3,sticky=W)

                label3 = Label(resultFrame,text="Worksite Address:",font=('Arial',26),bg="#bcdfeb",justify="right")
                label3.grid(row=4,column=0,columnspan=3)
                userEntry3 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry3.insert(0,searchResult[3])
                userEntry3.grid(row=4,column=3,columnspan=3,sticky=W)

                label4 = Label(resultFrame,text="Worksite City:",font=('Arial',26),bg="#bcdfeb",justify="right")
                label4.grid(row=5,column=0,columnspan=3)
                userEntry4 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry4.insert(0,searchResult[4])
                userEntry4.grid(row=5,column=3,columnspan=3,sticky=W)

                label5 = Label(resultFrame,text="Worksite Zip:",font=('Arial',26),bg="#bcdfeb",justify="right")
                label5.grid(row=6,column=0,columnspan=3)
                userEntry5 = Entry(resultFrame,font=('Arial',20),relief=RIDGE,width=50)
                userEntry5.insert(0,searchResult[5])
                userEntry5.grid(row=6,column=3,columnspan=3,sticky=W)
                
                searchOneAssetBtn.config(state=DISABLED)
                searchOneWorksiteBtn.config(state=DISABLED)

                confirmAssetBtn = Button(resultFrame, text="Confirm Update", font=('Arial',20),
                                         command=lambda: UpdateWorksite())
                confirmAssetBtn.grid(row=7,column=0,columnspan=4)

                resetAssetBtn = Button(resultFrame, text="Reset", font=('Arial',20),command=lambda: resetAsset())
                resetAssetBtn.grid(row=7,column=4,columnspan=4)

            def UpdateWorksite():
                worksiteID=userEntry0.get()
                orderID=userEntry1.get()
                workType=userEntry2.get()
                address=userEntry3.get()
                city=userEntry4.get()
                zip=userEntry5.get()
                database.deleteWorksite(conn, worksiteID)
                database.updateWorksite(conn, worksiteID,orderID,workType,address,city,zip)
                messagebox.showinfo("Update Success","Worksite Updated Successfully")
                foundLabel.destroy()
                label0.destroy()
                label1.destroy()
                label2.destroy()
                label3.destroy()
                label4.destroy()
                label5.destroy()
                userEntry0.destroy()
                userEntry1.destroy()
                userEntry2.destroy()
                userEntry3.destroy()
                userEntry4.destroy()
                userEntry5.destroy()
                resetAssetBtn.destroy()
                confirmAssetBtn.destroy()
                searchOneAssetBtn.config(state=ACTIVE)
                searchOneWorksiteBtn.config(state=ACTIVE)
                searchEntry1.delete(0,END)

            def resetAsset():
                foundLabel.destroy()
                label0.destroy()
                label1.destroy()
                label2.destroy()
                label3.destroy()
                label4.destroy()
                label5.destroy()
                userEntry0.destroy()
                userEntry1.destroy()
                userEntry2.destroy()
                userEntry3.destroy()
                userEntry4.destroy()
                userEntry5.destroy()
                resetAssetBtn.destroy()
                confirmAssetBtn.destroy()
                searchOneAssetBtn.config(state=ACTIVE)
                searchOneWorksiteBtn.config(state=ACTIVE)
                searchEntry1.delete(0,END)
        
        ##============================================================
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#bcdfeb")
        resultFrame = Frame(self, bg="#bcdfeb")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        resultFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=100)
        contentFrame.config(width=1220,height=150)
        resultFrame.config(width=1220,height=400)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        resultFrame.pack(side="bottom")
        contentFrame.pack(side="bottom")
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6),weight=1,minsize=182)
        contentFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
        resultFrame.columnconfigure((0,1,2,3,4,5,6),weight=1,minsize=182)
        resultFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)

        ##============================================================
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
        Label(contentFrame,text="Asset/Worksite ID:",font=('Arial',20),bg="#bcdfeb",justify="right",width=20,anchor=E
              ).grid(row=0,column=0, columnspan=3)
        searchEntry1 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=34)
        searchEntry1.grid(row=0,column=3,columnspan=4,sticky=W)
        searchOneAssetBtn = Button(contentFrame, text="Search Asset", font=('Arial',20),command=lambda: searchOneAsset())
        searchOneAssetBtn.grid(row=1,column=1, columnspan=3)
        searchOneWorksiteBtn = Button(contentFrame, text="Search Worksite", font=('Arial',20),command=lambda: searchOneWorksite())
        searchOneWorksiteBtn.grid(row=1,column=3, columnspan=3)

class DeletePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ##============================================================
        ## WIDGET FUNCTION SETTINGS
        ##

        def searchOneAsset(userEntry):
            assetID = userEntry.get()

            if assetID == "":
                messagebox.showerror("Missing Entry","Please Enter an Entity ID")
                searchEntry1.delete(0,END)
            else:
                foundLabel = Label(resultFrame,text="Asset Found:",font=('Arial',20),bg="#bcdfeb")
                foundLabel.pack(pady=10)
                searchResult=database.viewOneAsset(conn, assetID)
                print(searchResult)
                assetTree = ttk.Treeview(resultFrame,height=1)
                assetTree['columns']=("ID","Name","Type","Model No.","Purchase Date","Cost")
                assetTree.column("#0",width=1)
                assetTree.column("ID",width=10)
                assetTree.column("Name",width=150,anchor="center")
                assetTree.column("Type",width=150,anchor="center")
                assetTree.column("Model No.",width=120,anchor="center")
                assetTree.column("Purchase Date",width=120,anchor="center")
                assetTree.column("Cost",width=120,anchor="center")
                assetTree.heading("#0", text="")
                assetTree.heading("ID", text="ID")
                assetTree.heading("Name", text="Name")
                assetTree.heading("Type", text="Type")
                assetTree.heading("Model No.", text="Model No.")
                assetTree.heading("Purchase Date", text="Purchase Date")
                assetTree.heading("Cost", text="Cost")
                assetTree.insert(parent="",index='end',iid=1,text="val",values=(
                                 searchResult[0],searchResult[2],searchResult[1],
                                 searchResult[3],searchResult[4],searchResult[5]))
                assetTree.pack()
                searchOneAssetBtn.config(state=DISABLED)
                searchOneWorksiteBtn.config(state=DISABLED)
                confirmAssetBtn = Button(resultFrame, text="Confirm Delete", font=('Arial',20),
                                         command=lambda: deleteAsset(assetID,assetTree,confirmAssetBtn,resetAssetBtn,foundLabel))
                confirmAssetBtn.pack(pady=10)
                resetAssetBtn = Button(resultFrame, text="Reset", font=('Arial',20),
                                       command=lambda: resetAsset(assetTree,confirmAssetBtn,resetAssetBtn,foundLabel))
                resetAssetBtn.pack(pady=10)

            def deleteAsset(userEntry, tree, confrmButton,resetButton,label):
                    database.deleteAsset(conn, userEntry)
                    messagebox.showinfo("Delete Success","Asset Deleted Successfully")
                    tree.destroy()
                    confrmButton.destroy()
                    resetButton.destroy()
                    label.destroy()
                    searchOneAssetBtn.config(state=ACTIVE)
                    searchOneWorksiteBtn.config(state=ACTIVE)
                    searchEntry1.delete(0,END)

            def resetAsset(tree, confrmButton,resetButton,label):
                    tree.destroy()
                    confrmButton.destroy()
                    resetButton.destroy()
                    label.destroy()
                    searchOneAssetBtn.config(state=ACTIVE)
                    searchOneWorksiteBtn.config(state=ACTIVE)
                    searchEntry1.delete(0,END)

        def searchOneWorksite(userEntry):
            worksiteID = userEntry.get()
            
            if worksiteID == "":
                messagebox.showerror("Missing Entry","Please Enter an Entity ID")
                searchEntry1.delete(0,END)
            else:
                foundLabel = Label(resultFrame,text="Worksite Found:",font=('Arial',20),bg="#bcdfeb")
                foundLabel.pack(pady=10)
                searchResult=database.viewOneWorksite(conn, worksiteID)
                worksiteTree = ttk.Treeview(resultFrame,height=1)
                worksiteTree['columns']=("ID","Order ID","Type","Address","City","Zip Code")
                worksiteTree.column("#0",width=1)
                worksiteTree.column("ID",width=10)
                worksiteTree.column("Order ID",width=150,anchor="center")
                worksiteTree.column("Type",width=150,anchor="center")
                worksiteTree.column("Address",width=120,anchor="center")
                worksiteTree.column("City",width=120,anchor="center")
                worksiteTree.column("Zip Code",width=120,anchor="center")
                worksiteTree.heading("#0", text="")
                worksiteTree.heading("ID", text="ID")
                worksiteTree.heading("Order ID", text="Order ID")
                worksiteTree.heading("Type", text="Type")
                worksiteTree.heading("Address", text="Address")
                worksiteTree.heading("City", text="City")
                worksiteTree.heading("Zip Code", text="Zip Code")
                worksiteTree.insert(parent="",index='end',iid=1,text="val",values=(
                                 searchResult[0],searchResult[1],searchResult[2],
                                 searchResult[3],searchResult[4],searchResult[5]))
                worksiteTree.pack()
                searchOneAssetBtn.config(state=DISABLED)
                searchOneWorksiteBtn.config(state=DISABLED)
                confirmWorksiteBtn = Button(resultFrame,text="Confirm Delete", font=('Arial',20),
                                         command=lambda: deleteWorksite(worksiteID,worksiteTree,confirmWorksiteBtn,resetWorksiteBtn,foundLabel))
                confirmWorksiteBtn.pack(pady=10)
                resetWorksiteBtn = Button(resultFrame,text="Reset", font=('Arial',20),
                                       command=lambda: resetWorksite(worksiteTree,confirmWorksiteBtn,resetWorksiteBtn,foundLabel))
                resetWorksiteBtn.pack(pady=10)

                def deleteWorksite(userEntry, tree, confrmButton,resetButton,label):
                    database.deleteWorksite(conn, userEntry)
                    messagebox.showinfo("Delete Success","Worksite Deleted Successfully")
                    tree.destroy()
                    confrmButton.destroy()
                    resetButton.destroy()
                    label.destroy()
                    searchOneAssetBtn.config(state=ACTIVE)
                    searchOneWorksiteBtn.config(state=ACTIVE)
                    searchEntry1.delete(0,END)

                def resetWorksite(tree, confrmButton,resetButton,label):
                    tree.destroy()
                    confrmButton.destroy()
                    resetButton.destroy()
                    label.destroy()
                    searchOneAssetBtn.config(state=ACTIVE)
                    searchOneWorksiteBtn.config(state=ACTIVE)
                    searchEntry1.delete(0,END)

        ##============================================================
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#bcdfeb")
        resultFrame = Frame(self, bg="#bcdfeb")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        resultFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=100)
        contentFrame.config(width=1220,height=200)
        resultFrame.config(width=1220,height=400)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        resultFrame.pack(side="bottom")
        contentFrame.pack(side="bottom")
        
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6),weight=1,minsize=182)
        contentFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)

        ##============================================================
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
        Label(headerFrame, text="Delete an Entity",font=('Arial',36,'bold'),bg="#9ed1e1",width=33
              ).pack(side="left")
        Button(headerFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
        # Search Entry Bar and Buttons
        Label(contentFrame,text="Asset/Worksite ID:",font=('Arial',20),bg="#bcdfeb",justify="right",width=20,anchor=E
              ).grid(row=0,column=0, columnspan=3)
        searchEntry1 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=34)
        searchEntry1.grid(row=0,column=3,columnspan=4,sticky=W)
        searchOneAssetBtn = Button(contentFrame, text="Search Asset", font=('Arial',20),command=lambda: searchOneAsset(searchEntry1))
        searchOneAssetBtn.grid(row=1,column=1, columnspan=3)
        searchOneWorksiteBtn = Button(contentFrame, text="Search Worksite", font=('Arial',20),command=lambda: searchOneWorksite(searchEntry1))
        searchOneWorksiteBtn.grid(row=1,column=3, columnspan=3)
        
class ViewPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ##============================================================
        ## WIDGET FUNCTION SETTINGS
        ##

        def DisplayAssets():

            def resetView():
                viewAssetBtn.config(state=ACTIVE)
                viewWorksiteBtn.config(state=ACTIVE)
                viewAssignmentsBtn.config(state=ACTIVE)
                assetTree.destroy()
                resetBtn.destroy()
                viewScroll.destroy()

            def softResetView():
                viewAssetBtn.config(state=ACTIVE)
                viewWorksiteBtn.config(state=ACTIVE)
                viewAssignmentsBtn.config(state=ACTIVE)

            viewAssetBtn.config(state=DISABLED)
            viewWorksiteBtn.config(state=DISABLED)
            viewAssignmentsBtn.config(state=DISABLED)
            assetList = database.viewAllAssets(conn)
            
            if not len(assetList) == 0:
                viewScroll = Scrollbar(resultFrame)
                assetTree = ttk.Treeview(resultFrame,height=20,yscrollcommand=viewScroll.set)
                assetTree['columns']=("ID","Name","Type","Model No.","Purchase Date","Cost")
                assetTree.column("#0",width=1)
                assetTree.column("ID",width=10)
                assetTree.column("Name",width=150,anchor="center")
                assetTree.column("Type",width=150,anchor="center")
                assetTree.column("Model No.",width=120,anchor="center")
                assetTree.column("Purchase Date",width=120,anchor="center")
                assetTree.column("Cost",width=120,anchor="center")
                assetTree.heading("#0", text="")
                assetTree.heading("ID", text="ID")
                assetTree.heading("Name", text="Name")
                assetTree.heading("Type", text="Type")
                assetTree.heading("Model No.", text="Model No.")
                assetTree.heading("Purchase Date", text="Purchase Date")
                assetTree.heading("Cost", text="Cost")
                assetTree.tag_configure('even', background="gainsboro")
                assetTree.tag_configure('odd', background="white")
                i=0
                for asset in range(0,len(assetList)):
                    resultTup = assetList[asset]
                    if i % 2 == 0:
                        assetTree.insert(parent="",index='end',iid=i,text="val",values=(
                                            resultTup[0],resultTup[2],resultTup[1],
                                            resultTup[5],resultTup[4],resultTup[3]),tags=('even',))
                    else:
                        assetTree.insert(parent="",index='end',iid=i,text="val",values=(
                                            resultTup[0],resultTup[2],resultTup[1],
                                            resultTup[5],resultTup[4],resultTup[3]),tags=('odd',))
                    i+=1
                assetTree.pack(side="left")
                viewScroll.pack(side="left",fill="y")
                viewScroll.config(command=assetTree.yview)
                resetBtn = Button(resultFrame,text="Reset", font=('Arial',20),
                                       command=lambda: resetView())
                resetBtn.pack(side="right",padx=50)
            else:
                messagebox.showerror("Missing Data","No Assets Found")
                softResetView()

        def DisplayWorksites():

            def resetView():
                viewAssetBtn.config(state=ACTIVE)
                viewWorksiteBtn.config(state=ACTIVE)
                viewAssignmentsBtn.config(state=ACTIVE)
                worksiteTree.destroy()
                resetBtn.destroy()
                viewScroll.destroy()

            def softResetView():
                viewAssetBtn.config(state=ACTIVE)
                viewWorksiteBtn.config(state=ACTIVE)
                viewAssignmentsBtn.config(state=ACTIVE)

            viewAssetBtn.config(state=DISABLED)
            viewWorksiteBtn.config(state=DISABLED)
            viewAssignmentsBtn.config(state=DISABLED)

            worksiteList = database.viewAllWorksites(conn)

            if not len(worksiteList) == 0:
                viewScroll = Scrollbar(resultFrame)
                worksiteTree = ttk.Treeview(resultFrame,height=20,yscrollcommand=viewScroll.set)
                worksiteTree['columns']=("ID","Order ID","Type","Address","City","Zip Code")
                worksiteTree.column("#0",width=1)
                worksiteTree.column("ID",width=10)
                worksiteTree.column("Order ID",width=150,anchor="center")
                worksiteTree.column("Type",width=150,anchor="center")
                worksiteTree.column("Address",width=120,anchor="center")
                worksiteTree.column("City",width=120,anchor="center")
                worksiteTree.column("Zip Code",width=120,anchor="center")
                worksiteTree.heading("#0", text="")
                worksiteTree.heading("ID", text="ID")
                worksiteTree.heading("Order ID", text="Order ID")
                worksiteTree.heading("Type", text="Type")
                worksiteTree.heading("Address", text="Address")
                worksiteTree.heading("City", text="City")
                worksiteTree.heading("Zip Code", text="Zip Code")
                worksiteTree.tag_configure('even', background="gainsboro")
                worksiteTree.tag_configure('odd', background="white")
                i=0
                for worksite in range(0,len(worksiteList)):
                    resultTup = worksiteList[worksite]
                    if i % 2 == 0:
                        worksiteTree.insert(parent="",index='end',iid=i,text="val",values=(
                                            resultTup[0],resultTup[1],resultTup[2],
                                            resultTup[3],resultTup[4],resultTup[5]),tags=('even',))
                    else:
                        worksiteTree.insert(parent="",index='end',iid=i,text="val",values=(
                                            resultTup[0],resultTup[1],resultTup[2],
                                            resultTup[3],resultTup[4],resultTup[5]),tags=('odd',))
                    i+=1
                worksiteTree.pack(side="left")
                viewScroll.pack(side="left",fill="y")
                viewScroll.config(command=worksiteTree.yview)
                resetBtn = Button(resultFrame,text="Reset", font=('Arial',20),
                                       command=lambda: resetView())
                resetBtn.pack(side="right",padx=50)
            else:
                messagebox.showerror("Missing Data","No Worksites Found")
                softResetView()
            
        def DisplayAssignments():
            def resetView():
                viewAssetBtn.config(state=ACTIVE)
                viewWorksiteBtn.config(state=ACTIVE)
                viewAssignmentsBtn.config(state=ACTIVE)
                assignmentTree.destroy()
                resetBtn.destroy()
                viewScroll.destroy()

            def softResetView():
                viewAssetBtn.config(state=ACTIVE)
                viewWorksiteBtn.config(state=ACTIVE)
                viewAssignmentsBtn.config(state=ACTIVE)

            viewAssetBtn.config(state=DISABLED)
            viewWorksiteBtn.config(state=DISABLED)
            viewAssignmentsBtn.config(state=DISABLED)

            assignmentList = database.viewAllAssignments(conn)

            if not len(assignmentList) == 0:
                viewScroll = Scrollbar(resultFrame)
                assignmentTree = ttk.Treeview(resultFrame,height=20,yscrollcommand=viewScroll.set)
                assignmentTree['columns']=("Assignment ID","Asset ID","Asset Type","Asset Name","Asset Model No",
                                           "Worksite ID", "Order ID", "Worksite Type")
                assignmentTree.column("#0",width=1)
                assignmentTree.column("Assignment ID",width=120)
                assignmentTree.column("Asset ID",width=100,anchor="center")
                assignmentTree.column("Asset Type",width=120,anchor="center")
                assignmentTree.column("Asset Name",width=120,anchor="center")
                assignmentTree.column("Asset Model No",width=150,anchor="center")
                assignmentTree.column("Worksite ID",width=100,anchor="center")
                assignmentTree.column("Order ID",width=120,anchor="center")
                assignmentTree.column("Worksite Type",width=150,anchor="center")
                assignmentTree.heading("#0", text="")
                assignmentTree.heading("Assignment ID", text="Assignment ID")
                assignmentTree.heading("Asset ID", text="Asset ID")
                assignmentTree.heading("Asset Type", text="Asset Type")
                assignmentTree.heading("Asset Name", text="Asset Name")
                assignmentTree.heading("Asset Model No", text="Asset Model No")
                assignmentTree.heading("Worksite ID", text="Worksite ID")
                assignmentTree.heading("Order ID", text="Order ID")
                assignmentTree.heading("Worksite Type", text="Worksite Type")
                assignmentTree.tag_configure('even', background="gainsboro")
                assignmentTree.tag_configure('odd', background="white")
                i=0
                for assignment in range(0,len(assignmentList)):
                    resultTup = assignmentList[assignment]
                    resultAssetID = resultTup[1]
                    resultWorksiteID = resultTup[2]
                    foundAsset = database.viewOneAsset(conn, resultAssetID)
                    foundWorksite = database.viewOneWorksite(conn, resultWorksiteID)
                    if i % 2 == 0:
                        assignmentTree.insert(parent="",index='end',iid=i,text="val",values=(
                                            resultTup[0],resultTup[1],foundAsset[1],
                                            foundAsset[2],foundAsset[5],resultTup[2],
                                            foundWorksite[1],foundWorksite[2]),tags=('even',))
                    else:
                        assignmentTree.insert(parent="",index='end',iid=i,text="val",values=(
                                            resultTup[0],resultTup[1],foundAsset[1],
                                            foundAsset[2],foundAsset[5],resultTup[2],
                                            foundWorksite[1],foundWorksite[2]),tags=('odd',))
                    i+=1
                assignmentTree.pack(side="left")
                viewScroll.pack(side="left",fill="y")
                viewScroll.config(command=assignmentTree.yview)
                resetBtn = Button(resultFrame,text="Reset", font=('Arial',20),
                                       command=lambda: resetView())
                resetBtn.pack(side="right",padx=50)
            else:
                messagebox.showerror("Missing Data","No Assignments Found")
                softResetView()
        
        ##============================================================
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#bcdfeb")
        resultFrame = Frame(self, bg="#bcdfeb")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        resultFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=100)
        contentFrame.config(width=1220,height=100)
        resultFrame.config(width=1220,height=500)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        resultFrame.pack(side="bottom")
        contentFrame.pack(side="bottom")
        
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6,7),weight=1)
        contentFrame.rowconfigure((0,1,2),weight=1)
        resultFrame.columnconfigure((0,1,2,3,4,5,6,7),weight=1)
        resultFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)

        ##============================================================
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
        viewAssetBtn = Button(contentFrame, text="View Assets", font=('Arial',20),command=lambda: DisplayAssets())
        viewAssetBtn.grid(row=1,column=0,columnspan=2)
        viewWorksiteBtn = Button(contentFrame, text="View Worksites", font=('Arial',20),command=lambda: DisplayWorksites())
        viewWorksiteBtn.grid(row=1,column=3,columnspan=2)
        viewAssignmentsBtn = Button(contentFrame, text="View Assignments", font=('Arial',20),command=lambda: DisplayAssignments())
        viewAssignmentsBtn.grid(row=1,column=6,columnspan=2)

class AssignmentPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        def comboSearch():

            def confirmAssign():
                database.addAssignment(conn, entry1, entry2)
                messagebox.showinfo("Assignment Success","Entity Assignment Successful")
                searchComboBtn.config(state=ACTIVE)
                worksiteTree.destroy()
                assetTree.destroy()
                confirmBtn.destroy()
                resetBtn.destroy()
                assetLabel.destroy()
                worksiteLabel.destroy()
                searchEntry1.delete(0,END)
                searchEntry2.delete(0,END)


            def resetView():
                searchComboBtn.config(state=ACTIVE)
                worksiteTree.destroy()
                assetTree.destroy()
                confirmBtn.destroy()
                resetBtn.destroy()
                assetLabel.destroy()
                worksiteLabel.destroy()
                searchEntry1.delete(0,END)
                searchEntry2.delete(0,END)

            entry1 = searchEntry1.get()
            entry2 = searchEntry2.get()
            assetID = database.viewOneAsset(conn, entry1)
            worksiteID = database.viewOneWorksite(conn, entry2)

            if (entry1 == "") or (entry2 == ""):
                messagebox.showerror("Missing Entry","Please Enter an Asset ID and Worksite ID")
                searchEntry1.delete(0,END)
                searchEntry2.delete(0,END)
                searchComboBtn.config(state=ACTIVE)
            elif assetID == None:
                messagebox.showerror("Asset Not Found","No asset exists with that Asset ID")
                searchEntry1.delete(0,END)
                searchEntry2.delete(0,END)
                searchComboBtn.config(state=ACTIVE)
            elif worksiteID == None:
                messagebox.showerror("Worksite Not Found","No worksite exists with that Worksite ID")
                searchEntry1.delete(0,END)
                searchEntry2.delete(0,END)
                searchComboBtn.config(state=ACTIVE)
            else:
                searchComboBtn.config(state=DISABLED)
                
                assetLabel = Label(resultFrame,text="Asset:",font=('Arial',20),bg="#bcdfeb")
                assetLabel.pack(pady=10)
                assetTree = ttk.Treeview(resultFrame,height=1)
                assetTree['columns']=("ID","Name","Type","Model No.","Purchase Date","Cost")
                assetTree.column("#0",width=1)
                assetTree.column("ID",width=10)
                assetTree.column("Name",width=150,anchor="center")
                assetTree.column("Type",width=150,anchor="center")
                assetTree.column("Model No.",width=120,anchor="center")
                assetTree.column("Purchase Date",width=120,anchor="center")
                assetTree.column("Cost",width=120,anchor="center")
                assetTree.heading("#0", text="")
                assetTree.heading("ID", text="ID")
                assetTree.heading("Name", text="Name")
                assetTree.heading("Type", text="Type")
                assetTree.heading("Model No.", text="Model No.")
                assetTree.heading("Purchase Date", text="Purchase Date")
                assetTree.heading("Cost", text="Cost")
                assetTree.insert(parent="",index='end',iid=1,text="val",values=(
                                 assetID[0],assetID[2],assetID[1],
                                 assetID[3],assetID[4],assetID[5]))
                assetTree.pack()
                worksiteLabel = Label(resultFrame,text="Worksite:",font=('Arial',20),bg="#bcdfeb")
                worksiteLabel.pack(pady=10)
                worksiteTree = ttk.Treeview(resultFrame,height=1)
                worksiteTree['columns']=("ID","Order ID","Type","Address","City","Zip Code")
                worksiteTree.column("#0",width=1)
                worksiteTree.column("ID",width=10)
                worksiteTree.column("Order ID",width=150,anchor="center")
                worksiteTree.column("Type",width=150,anchor="center")
                worksiteTree.column("Address",width=120,anchor="center")
                worksiteTree.column("City",width=120,anchor="center")
                worksiteTree.column("Zip Code",width=120,anchor="center")
                worksiteTree.heading("#0", text="")
                worksiteTree.heading("ID", text="ID")
                worksiteTree.heading("Order ID", text="Order ID")
                worksiteTree.heading("Type", text="Type")
                worksiteTree.heading("Address", text="Address")
                worksiteTree.heading("City", text="City")
                worksiteTree.heading("Zip Code", text="Zip Code")
                worksiteTree.insert(parent="",index='end',iid=1,text="val",values=(
                                 worksiteID[0],worksiteID[1],worksiteID[2],
                                 worksiteID[3],worksiteID[4],worksiteID[5]))
                worksiteTree.pack()
                confirmBtn = Button(resultFrame,text="Confirm Assignment", font=('Arial',20),command=lambda: confirmAssign())
                confirmBtn.pack(pady=20)
                resetBtn = Button(resultFrame,text="Reset", font=('Arial',20),
                                       command=lambda: resetView())
                resetBtn.pack()
        
        ##============================================================
        ## LAYOUT SETTINGS
        ##

        # Set background color for main frame
        self.config(background="#bcdfeb")
        # Create frames for header and content
        headerFrame = Frame(self, bg="#9ed1e1")
        contentFrame = Frame(self, bg="#bcdfeb")
        resultFrame = Frame(self, bg="#bcdfeb")
        # grid propagate so we can force frame sizes
        headerFrame.grid_propagate(0)
        contentFrame.grid_propagate(0)
        resultFrame.grid_propagate(0)
        # configure frame sizes
        headerFrame.config(width=1220,height=100)
        contentFrame.config(width=1220,height=150)
        resultFrame.config(width=1220,height=450)
        # pack frames onto main frame
        headerFrame.pack(side="top")
        resultFrame.pack(side="bottom")
        contentFrame.pack(side="bottom")
        # Establish grid for content frame
        contentFrame.columnconfigure((0,1,2,3,4,5,6),weight=1)
        contentFrame.rowconfigure((0,1,2,3),weight=1)
        resultFrame.columnconfigure((0,1,2,3,4,5,6,7),weight=1)
        resultFrame.rowconfigure((0,1,2,3,4,5,6,7),weight=1)

        ##============================================================
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
        Label(headerFrame, text="Entity Assignments",font=('Arial',36,'bold'),bg="#9ed1e1",width=33).pack(side="left")
        Button(headerFrame, text="Return to Home Page",
               command=lambda: parent.switch_frame(HomePage)).pack(side="left",fill="y")
        
        # Search Bar and Button
        Label(contentFrame,text="Asset ID:",font=('Arial',20),bg="#bcdfeb",justify="right",width=20,anchor=E
              ).grid(row=0,column=0, columnspan=3)
        searchEntry1 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=34)
        searchEntry1.grid(row=0,column=3,columnspan=4,sticky=W)
        Label(contentFrame,text="Worksite ID:",font=('Arial',20),bg="#bcdfeb",justify="right",width=20,anchor=E
              ).grid(row=1,column=0, columnspan=3)
        searchEntry2 = Entry(contentFrame,font=('Arial',20),relief=RIDGE,width=34)
        searchEntry2.grid(row=1,column=3,columnspan=4,sticky=W)
        searchComboBtn = Button(contentFrame, text="Search", font=('Arial',20),command=lambda: comboSearch())
        searchComboBtn.grid(row=2,column=0,columnspan=7)

##============================================================
## TKINTER WINDOW MAINLOOP
##

if __name__ == "__main__":
    tt = TechTrack()
    tt = mainloop()