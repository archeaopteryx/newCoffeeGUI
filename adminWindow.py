import tkinter as tk
from numPad import NumPad
from keyboard import KeyboardGUI

########################################################
# Lays out the window for the administrative tasks and takes care of the associated
# adminstrative functions.
#
#The adminstrative functions are: changing the prices, and changing the admin password.
#
#When these values are changed, they are passed back to the mainWindow, which takes
# care of calling fileManager to update the config file so that the changes are
# persistent.
########################################################

class AdminWindow(tk.Toplevel):

    def __init__(self, parent, app):
        tk.Toplevel.__init__(self, parent)
        self.app = app
        self.parent=parent
        self.coffee = self.app.coffeePrice
        self.milk = self.app.milkPrice
        self.adminPass = ""
        self.newVal = None
        self.init_window()

    def init_window(self):
        self.title("Administration")
        windowWidth=620
        self.geometry("{0}x420".format(windowWidth))

        upperFrame = tk.Frame(self)
        lowerFrame = tk.Frame(self)
        frameWidth=windowWidth-20

        fontName ="TkDefaultFont"
        msgFontSize =16
        btnFontSize = 20
        stdHeight = 60
        btnWidth = 150
        labelWidth=270
        valueWidth = 180

        def enterValue(var):
            dialog = NumPad(self, self.app, "admin")
            self.wait_window(dialog)
            if self.newVal != None and var == "coffee":
                self.coffee = self.newVal
                coffeeLbl.configure(text="{:.2f}".format(self.coffee/100))
            elif self.newVal != None and var == "milk":
                self.milk = self.newVal
                milkLbl.configure(text="{:.2f}".format(self.milk/100))
            self.newVal = None

        def enterPass():
            dialog = KeyboardGUI(self, self.app, "admin")
            self.wait_window(dialog)

        def submit():
            self.parent.coffeePrice = self.coffee
            self.parent.milkPrice = self.milk
            if len(self.adminPass)>0:
                self.parent.adminPass = self.adminPass
            self.destroy()

        def cancel():
            self.destroy()


        msgAspect = int(frameWidth/2*stdHeight*100) #width/height*100
        msg = "Welcome, Admin! \nNew values will be accepted upon clicking 'submit'.\nThe 'milk' cost is added to the base cost of 'coffee' \n to give the 'milk with coffee' cost. "
        info = tk.Message(upperFrame, text=msg, aspect=msgAspect)
        info.configure(font=(fontName, msgFontSize))
        info.place(height=2*stdHeight, width=frameWidth, anchor='nw',relx=0, rely=0)

        tk.Label(upperFrame, text="Coffee Price:", font=(fontName, btnFontSize),anchor='w').place(height=stdHeight, width=labelWidth, anchor="nw", relx=0, rely=0.4)
        coffeeLbl = tk.Label(upperFrame, text="{:.2f}".format(self.coffee/100), font=(fontName, btnFontSize))
        coffeeLbl.place(height=stdHeight, width=labelWidth, anchor="nw", relx=0.45, rely=0.4)
        coffeeBtn = tk.Button(upperFrame, text="set...", command=lambda var = "coffee":enterValue(var))
        coffeeBtn.configure(font=(fontName, btnFontSize))
        coffeeBtn.place(height=stdHeight, width=btnWidth, anchor='ne', relx=1.0, rely=0.4)

        tk.Label(upperFrame, text="Milk Price:", font=(fontName, btnFontSize),anchor='w').place(height=stdHeight, width=labelWidth, anchor="nw", relx=0, rely=0.6)
        milkLbl = tk.Label(upperFrame, text="{:.2f}".format(self.milk/100), font=(fontName, btnFontSize))
        milkLbl.place(height=stdHeight, width=labelWidth, anchor="nw", relx=0.45, rely=0.6)
        milkBtn = tk.Button(upperFrame, text="set...", command=lambda var = "milk":enterValue(var))
        milkBtn.configure(font=(fontName, btnFontSize))
        milkBtn.place(height=stdHeight, width=btnWidth, anchor='ne', relx=1.0, rely=0.6)

        tk.Label(upperFrame, text="Admin Password:", font=(fontName, btnFontSize),anchor='w').place(height=stdHeight, width=labelWidth, anchor="nw", relx=0, rely=0.8)
        tk.Label(upperFrame, text="****", font=(fontName, btnFontSize)).place(height=stdHeight, width=labelWidth, anchor="nw", relx=0.45, rely=0.8)
        passBtn = tk.Button(upperFrame, text="set...",command=enterPass)
        passBtn.configure(font=(fontName, btnFontSize))
        passBtn.place(height=stdHeight, width=btnWidth, anchor='ne', relx=1.0, rely=0.8)

        submitBtn = tk.Button(lowerFrame, text="Submit", command=submit)
        submitBtn.configure(font=(fontName, btnFontSize))
        submitBtn.place(height=stdHeight, width=btnWidth, anchor='nw', relx=0, rely=0)

        cancelBtn = tk.Button(lowerFrame, text="Cancel", command=cancel)
        cancelBtn.configure(font=(fontName, btnFontSize), foreground="red")
        cancelBtn.place(height=stdHeight, width=btnWidth, anchor='ne', relx=1.0, rely=0)

        upperFrame.place(height=325, width=frameWidth, x=10,y=10)
        lowerFrame.place(height=60, width=frameWidth, x=10, y=350)
