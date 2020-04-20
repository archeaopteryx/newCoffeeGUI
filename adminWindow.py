import tkinter as tk
from numPad import NumPad
from keyboard import KeyboardGUI

class AdminWindow(tk.Toplevel):

    def __init__(self, parent, app, coffee, milk):
        tk.Toplevel.__init__(self, parent)
        self.app = app
        self.coffee = coffee
        self.milk = milk
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
            elif self.newVal != None and var == "milk":
                self.milk = self.newVal
            self.newVal = None
            print(str(self.coffee)+" "+str(self.milk))

        def enterPass():
            dialog = KeyboardGUI(self, self.app, "admin")
            self.wait_window(dialog)
            print("done")

        def cancel():
            self.destroy()


        msgAspect = int(frameWidth/2*stdHeight*100) #width/height*100
        msg = "Welcome, Admin! \nNew values will be accepted upon clicking 'submit'.\nThe 'milk' cost is added to the base cost of 'coffee' \n to give the 'milk with coffee' cost. "
        info = tk.Message(upperFrame, text=msg, aspect=msgAspect)
        info.configure(font=(fontName, msgFontSize))
        info.place(height=2*stdHeight, width=frameWidth, anchor='nw',relx=0, rely=0)

        tk.Label(upperFrame, text="Coffee Price:", font=(fontName, btnFontSize),anchor='w').place(height=stdHeight, width=labelWidth, anchor="nw", relx=0, rely=0.4)
        tk.Label(upperFrame, text="{:.2f}".format(self.coffee/100), font=(fontName, btnFontSize)).place(height=stdHeight, width=labelWidth, anchor="nw", relx=0.45, rely=0.4)
        coffeeBtn = tk.Button(upperFrame, text="Update", command=lambda var = "coffee":enterValue(var))
        coffeeBtn.configure(font=(fontName, btnFontSize))
        coffeeBtn.place(height=stdHeight, width=btnWidth, anchor='ne', relx=1.0, rely=0.4)

        tk.Label(upperFrame, text="Milk Price:", font=(fontName, btnFontSize),anchor='w').place(height=stdHeight, width=labelWidth, anchor="nw", relx=0, rely=0.6)
        tk.Label(upperFrame, text="{:.2f}".format(self.milk/100), font=(fontName, btnFontSize)).place(height=stdHeight, width=labelWidth, anchor="nw", relx=0.45, rely=0.6)
        milkBtn = tk.Button(upperFrame, text="Update", command=lambda var = "milk":enterValue(var))
        milkBtn.configure(font=(fontName, btnFontSize))
        milkBtn.place(height=stdHeight, width=btnWidth, anchor='ne', relx=1.0, rely=0.6)

        tk.Label(upperFrame, text="Admin Password:", font=(fontName, btnFontSize),anchor='w').place(height=stdHeight, width=labelWidth, anchor="nw", relx=0, rely=0.8)
        tk.Label(upperFrame, text="****", font=(fontName, btnFontSize)).place(height=stdHeight, width=labelWidth, anchor="nw", relx=0.45, rely=0.8)
        passBtn = tk.Button(upperFrame, text="Update",command=enterPass)
        passBtn.configure(font=(fontName, btnFontSize))
        passBtn.place(height=stdHeight, width=btnWidth, anchor='ne', relx=1.0, rely=0.8)

        submitBtn = tk.Button(lowerFrame, text="Submit")
        submitBtn.configure(font=(fontName, btnFontSize))
        submitBtn.place(height=stdHeight, width=btnWidth, anchor='nw', relx=0, rely=0)

        cancelBtn = tk.Button(lowerFrame, text="Cancel", command=cancel)
        cancelBtn.configure(font=(fontName, btnFontSize), foreground="red")
        cancelBtn.place(height=stdHeight, width=btnWidth, anchor='ne', relx=1.0, rely=0)

        upperFrame.place(height=325, width=frameWidth, x=10,y=10)
        lowerFrame.place(height=60, width=frameWidth, x=10, y=350)
