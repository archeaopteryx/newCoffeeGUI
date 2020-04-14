import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


class KeyboardGUI(tk.Toplevel):

    def __init__(self,parent, app):
        tk.Toplevel.__init__(self, parent)
        self.app = app
        self.init_window()

    def init_window(self):
        self.title("Name Entry")
        self.geometry("950x560")
        fontSize = 28
        fontName = 'TkDefaultFont'

        self.textStr=""
        self.accent=""

        row1 = [('q','Q'),('w','W'),('e','E'),('r','R'),('t','T'),('y','Y'),('u','U'),('i','I'),('o','O'),('p','P')]
        row2 = [('a','A'),('s','S'),('d','D'),('f','F'),('g','G'),('h','H'),('j','J'),('k','K'),('l','L')]
        row3 = [('shift', 120, 0), ('z','Z'),('x','X'),('c','C'),('v','V'),('b','B'),('n','N'),('m','M'), ('del',120,0)]
        row4 = [('\N{LATIN SMALL LETTER O WITH STROKE}', '\N{LATIN CAPITAL LETTER O WITH STROKE}'), ('\N{LATIN SMALL LETTER A WITH RING ABOVE}', '\N{LATIN CAPITAL LETTER A WITH RING ABOVE}')]

        accentRow1 =[('\N{DIAERESIS}', '\N{COMBINING DIAERESIS}'),
        ('\N{ACUTE ACCENT}', '\N{COMBINING ACUTE ACCENT}'),('\N{GRAVE ACCENT}', '\N{COMBINING GRAVE ACCENT}')]
        accentRow2=[('\N{CIRCUMFLEX ACCENT}', '\N{COMBINING CIRCUMFLEX ACCENT}'),
        ('\N{TILDE}', '\N{COMBINING TILDE}'), ('\N{CEDILLA}', '\N{COMBINING CEDILLA}')]
        accentRow3=[('\N{OGONEK}', '\N{COMBINING OGONEK}'), ('\N{CARON}', '\N{COMBINING CARON}')]

        keyboard = [row1, row2, row3, row4]
        accentPad = [accentRow1, accentRow2, accentRow3]

        stdHeight = 60
        stdWidth = 60
        displayWidth= 700

        display = tk.Label(self, text="", font=(fontName,fontSize))
        display.place(height=stdHeight, width=displayWidth, x=0, y=0)

        def helpBox():
            helpMsg = "First click the button with the desired accent, then click the letter you want to add it to. For example, \N{DIAERESIS}a produces \N{LATIN SMALL LETTER A WITH DIAERESIS}"
            self.messageBox.configure(text=helpMsg, foreground="blue")

        def nextChar(character):
            toDisplay = str(character)+self.accent
            self.textStr += character
            display.configure(text="{0}".format(self.textStr))
            if len(self.textStr) == 1:
                makeKeyboard(keyboard, False)
            self.accent = ""

        def backspace():
            self.textStr = self.textStr[:-1]
            display.configure(text="{0}".format(self.textStr))

        def space():
            self.textStr += ' '
            display.configure(text="{0}".format(self.textStr))

        def submit():
            if self.textStr == "None":
                errorMsg = "Very funny. Please use a name that isn't likely to break the program"
                self.messageBox.configure(text=errorMsg, foreground="red")
            elif self.app.memberDict.get(self.textStr) == None:
                self.app.newUser = self.textStr
                self.destroy()
            else:
                errorMsg = "Error! Name already exists! Please change the name and hit 'submit' again."
                self.messageBox.configure(text=errorMsg, foreground="red")

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
            for r in range(len(keyboard)-1):
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
            xOffset=120
            periodBtn = tk.Button(self, text = ".", font=(fontName, fontSize))
            periodBtn.configure(command=lambda glyphVar = ".": nextChar(glyphVar))
            periodBtn.place(height=stdHeight, width=stdWidth, x=xOffset, y=yOffset)
            spaceBtn = tk.Button(self, text="space", font=(fontName, fontSize), command=space)
            xOffset+=stdWidth
            spaceBtn.pack()
            spaceBtn.place(height=stdHeight, width=300, x=xOffset, y=yOffset)
            xOffset+=330
            for c in range(len(keyboard[-1])): #special layout for last row
                glyph = str(keyboard[-1][c][case])
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


        makeKeyboard(keyboard, True)
        makeAccentPad(accentPad)
