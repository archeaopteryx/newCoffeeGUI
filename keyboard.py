import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


class KeyboardGUI(tk.Toplevel):

    def __init__(self,parent, app, type):
        tk.Toplevel.__init__(self, parent)
        self.app = app
        self.type = type
        self.init_window()

    def init_window(self):
        self.title("Name Entry")
        self.geometry("950x600")
        fontSize = 28
        fontName = 'TkDefaultFont'

        self.textStr=""
        self.starredStr=""
        self.showPassToogle = 0
        self.accent=""

        row1 = [('q','Q'),('w','W'),('e','E'),('r','R'),('t','T'),('y','Y'),('u','U'),('i','I'),('o','O'),('p','P')]
        row2 = [('a','A'),('s','S'),('d','D'),('f','F'),('g','G'),('h','H'),('j','J'),('k','K'),('l','L')]
        row3 = [('shift', 120, 0), ('z','Z'),('x','X'),('c','C'),('v','V'),('b','B'),('n','N'),('m','M'), ('del',120,0)]
        row4 = [('\N{LATIN SMALL LETTER O WITH STROKE}', '\N{LATIN CAPITAL LETTER O WITH STROKE}'), ('\N{LATIN SMALL LETTER A WITH RING ABOVE}', '\N{LATIN CAPITAL LETTER A WITH RING ABOVE}')]
        row5 = ["!", "@", "#", "$", "%", "^", "&","*", "(", ")"]

        accentRow1 =[('\N{DIAERESIS}', '\N{COMBINING DIAERESIS}'),
        ('\N{ACUTE ACCENT}', '\N{COMBINING ACUTE ACCENT}'),('\N{GRAVE ACCENT}', '\N{COMBINING GRAVE ACCENT}')]
        accentRow2=[('\N{CIRCUMFLEX ACCENT}', '\N{COMBINING CIRCUMFLEX ACCENT}'),
        ('\N{TILDE}', '\N{COMBINING TILDE}'), ('\N{CEDILLA}', '\N{COMBINING CEDILLA}')]
        accentRow3=[('\N{OGONEK}', '\N{COMBINING OGONEK}'), ('\N{CARON}', '\N{COMBINING CARON}')]

        keyboard = [row1, row2, row3, row4, row5]
        accentPad = [accentRow1, accentRow2, accentRow3]
        numPad = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0","-","_"]

        stdHeight = 60
        stdWidth = 60
        displayWidth= 700

        display = tk.Label(self, text="", font=(fontName,fontSize))
        display.place(height=stdHeight, width=displayWidth, x=0, y=0)

        def helpBox():
            helpMsg = "First click the button with the desired accent, then click the letter you want to add it to. For example, \N{DIAERESIS}a produces \N{LATIN SMALL LETTER A WITH DIAERESIS}"
            self.messageBox.configure(text=helpMsg, foreground="blue")

        def showPass():
            self.showPassToogle = (self.showPassToogle+1)%2
            updateDisplay()

        def updateDisplay():
            if self.type=="admin" and self.showPassToogle==0 :
                display.configure(text="{0}".format(self.starredStr))
            else:
                display.configure(text="{0}".format(self.textStr))

        def nextChar(character):
            toDisplay = str(character)+self.accent
            self.textStr += character
            self.starredStr+="*"
            updateDisplay()
            if len(self.textStr) == 1:
                makeKeyboard(keyboard, False)
            self.accent = ""

        def backspace():
            self.textStr = self.textStr[:-1]
            self.starredStr = self.starredStr[:-1]
            updateDisplay()

        def space():
            self.textStr += ' '
            updateDisplay

        def submit():
            if self.textStr == "None":
                errorMsg = "Very funny. Please use a name that isn't likely to break the program"
                self.messageBox.configure(text=errorMsg, foreground="red")
            else:
                if self.type == "user":
                    if self.app.memberDict.get(self.textStr) == None:
                        self.app.newUser = self.textStr
                        self.destroy()
                    else:
                        errorMsg = "Error! Name already exists! Please change the name and hit 'submit' again."
                        self.messageBox.configure(text=errorMsg, foreground="red")
                elif self.type == "admin":
                    self.app.newUser = self.textStr
                    self.destroy()

        def cancel():
            self.destroy()

        def makeLastRow(keyboard, case, yOffset):
            if self.type == "user":
                row = keyboard[3]
                xOffset=120
                periodBtn = tk.Button(self, text = ".", font=(fontName, fontSize))
                periodBtn.configure(command=lambda glyphVar = ".": nextChar(glyphVar))
                periodBtn.place(height=stdHeight, width=stdWidth, x=xOffset, y=yOffset)
                spaceBtn = tk.Button(self, text="space", font=(fontName, fontSize), command=space)
                xOffset+=stdWidth
                spaceBtn.pack()
                spaceBtn.place(height=stdHeight, width=300, x=xOffset, y=yOffset)
                xOffset+=330
                for c in range(len(row)): #special layout for last row
                    glyph = str(row[c][case])
                    button=tk.Button(self, text='{0}'.format(glyph), font=(fontName, fontSize))
                    button.configure(command=lambda glyphVar = glyph: nextChar(glyphVar))
                    button.place(height=stdHeight, width=stdWidth, x=xOffset, y=yOffset)
                    xOffset+=stdWidth
                xOffset=0
                yOffset+= 2*stdHeight
                submitBtn = tk.Button(self, text="SUMBIT", font=(fontName, fontSize), command=submit)
                submitBtn.place(height=stdHeight, width=240, x=0, y = yOffset)
                messageBoxHeight = 2*stdHeight
                messageBoxWidth = 600
                messageBoxAspect = int(messageBoxWidth/messageBoxHeight*100)
                msgBoxDefault = "Welcome to the coffee list!\nPlease enter the name of the new user and hit The 'submit' button."
                self.messageBox = tk.Message(self, text=msgBoxDefault, aspect=messageBoxAspect, font=(fontName, 20))
                self.messageBox.place(height=messageBoxHeight, width=messageBoxWidth, x=300, y=yOffset)
            elif self.type == "admin":
                row = keyboard[4]
                xOffset=0
                for c in range(len(row)):
                    glyph = str(row[c])
                    button = tk.Button(self, text="{0}".format(glyph), font=(fontName, fontSize))
                    button.configure(command=lambda glyphVar = glyph: nextChar(glyphVar))
                    button.place(height=stdHeight, width=stdWidth, x=xOffset, y=yOffset)
                    xOffset+=stdWidth
                xOffset=0
                yOffset+=2*stdHeight
                submitBtn=tk.Button(self, text="SUBMIT", command=submit)
                submitBtn.configure(font=(fontName, fontSize))
                submitBtn.place(height=stdHeight, width=240, x=0, y=yOffset)
                messageBoxHeight = 2*stdHeight
                messageBoxWidth = 600
                messageBoxAspect = int(messageBoxWidth/messageBoxHeight*100)
                msgBoxDefault = "Welcome, Admin! Please enter your password\nClick on the checkbox over the numpad if you want the display in plain text"
                self.messageBox = tk.Message(self, text=msgBoxDefault, aspect=messageBoxAspect, font=(fontName, 20))
                self.messageBox.place(height=messageBoxHeight, width=messageBoxWidth, x=300, y=yOffset)

        def addAccent(accentCode):
            self.accent += accentCode

        def shiftKey(shift):
            if shift==True:
                makeKeyboard(keyboard,False)
            else:
                makeKeyboard(keyboard,True)

        def makeKeyboard(keyboard, shift):
            if shift==True:
                case=1
            else:
                case=0
            xOffset=0
            yOffset=stdHeight
            nameIndex =0
            widthIndex = 1
            offsetIndex = 2
            for r in range(3):
                xOffset=(r%2)*stdWidth/2
                for c in range(len(keyboard[r])):
                    if len(keyboard[r][c])==2:
                        glyph = str(keyboard[r][c][case])
                        button = tk.Button(self, text="{0}".format(glyph), font=(fontName, fontSize))
                        button.configure(command=lambda glpyhVar = glyph: nextChar(glpyhVar))
                        button.place(height=stdHeight, width=stdWidth, x=xOffset,y=yOffset)
                        xOffset+=stdWidth
                    else:
                        glyph = str(keyboard[r][c][nameIndex])
                        button = tk.Button(self, text='{0}'.format(glyph), font=(fontName, fontSize))
                        if glyph =='shift':
                            button.configure(command= lambda shiftVar = shift: shiftKey(shiftVar))
                        elif glyph == 'del':
                            button.configure(command= backspace)
                        xOffset+=keyboard[r][c][offsetIndex]
                        button.place(height=stdHeight, width=keyboard[r][c][widthIndex], x=xOffset, y=yOffset)
                        xOffset+=keyboard[r][c][widthIndex]
                yOffset+=stdHeight
            makeLastRow(keyboard, case, yOffset)
            cancelBtn = tk.Button(self, text="Cancel", command=cancel)
            cancelBtn.configure(foreground="red", font=(fontName, fontSize))
            cancelBtn.place(height=stdHeight, width=200, anchor="se", relx=0.98, rely=0.98)

        def makeAccentPad(accentPad):
            yOffset = 0
            for row in accentPad:
                xOffset = 750
                yOffset += stdHeight
                for accent in row:
                    accentGlyph = str(accent[0])
                    accentAdd = accent[1]
                    button = tk.Button(self, text="{0}".format(accentGlyph),font=(fontName, fontSize))
                    button.configure(command=lambda accentVar = accentAdd: addAccent(accentVar))
                    button.place(height=stdHeight, width=stdWidth, x=xOffset, y=yOffset)
                    xOffset+= stdWidth
            helpIcon = ImageTk.PhotoImage(Image.open('helpIcon.png').resize(size=(stdWidth-6, stdHeight-6)))
            helpBtn = tk.Button(self, image=helpIcon, font=(fontName, 16))
            helpBtn.image=helpIcon
            helpBtn.configure(command=helpBox)
            helpBtn.place(height=stdHeight, width=stdWidth, x=xOffset, y=yOffset)

        def makeNumPad(numPad):
            xOffset_0 =750
            yOffset = 0
            checkboxShowPass = tk.Checkbutton(self, text="show password", command=showPass)
            checkboxShowPass.configure(font=(fontName, 14))
            checkboxShowPass.place(height=stdHeight, width=200, x=xOffset_0, y=yOffset)
            for val in range(len(numPad)):
                if val%3 == 0:
                    yOffset+= stdHeight
                glyph = str(numPad[val])
                button = tk.Button(self, text="{0}".format(glyph), font=(fontName, fontSize))
                button.configure(command=lambda glyphVar = glyph: nextChar(glyphVar))
                xOffset = xOffset_0 + stdWidth*(val%3)
                button.place(height=stdHeight, width=stdWidth, x=xOffset, y=yOffset)


        makeKeyboard(keyboard, True)
        if self.type =="user":
            makeAccentPad(accentPad)
        elif self.type == "admin":
            makeNumPad(numPad)
