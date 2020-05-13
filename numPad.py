import tkinter as tk
import tkinter.font as tkFont

########################################################
# Creates a clickable numberpad.
#
# The 'user' numberpad is meant to allow users to record the payments they make. If the
# type is 'user', then a userPane with a drop down option menu listing the users is
# also created.
#
# The 'admin' keyboard is intended to be used to change the prices for coffee and milk.
# It does not include the userPane
#
# The numpad does not directly return a variable. Instead, it sets a property of the
# parent widget.
########################################################

class NumPad(tk.Toplevel):

    def __init__(self, parent, app, type):
        tk.Toplevel.__init__(self, parent)
        self.parent= parent
        self.app= app
        self.type = type
        self.init_window()

    def init_window(self):
        self.title("NumPad")
        winWidth=800
        if self.type == "admin":
            winWidth= 480
        self.geometry("{0}x600".format(winWidth))
        fontSize = 30
        self.textStr = ""
        self.user = ""

        numPadFrame = tk.Frame(self)
        userSelectFrame = tk.Frame(self)
        stdKeyWidth = 3

        numPad = [
            ['7','8','9'],
            ['4','5','6'],
            ['1','2','3'],
            ['-','0','.'],
            ['del','C', 'SUBMIT']
        ]
        
        display = tk.Label(numPadFrame, text="", font=("TkDefaultFont", fontSize))
        rowHeight=0.16
        colWidth= 0.33
        display.place(relheight=rowHeight, relwidth=1, x=0, y=0)

        def nextGlyph(glyph):
            self.textStr += glyph
            display.configure(text="{0}".format(self.textStr))

        def clear():
            self.textStr = ""
            display.configure(text="{0}".format(self.textStr))

        def delete():
            self.textStr = self.textStr[:-1]
            display.configure(text="{0}".format(self.textStr))

        def submit():
            if len(self.textStr)>0 and self.type=="user":
                value = float(self.textStr)
                value =int(value*100)
                self.app.newVal=value
                self.app.selectedUser=self.user
            elif len(self.textStr)>0 and self.type=="admin":
                value = float(self.textStr)
                value = int(value*100)
                self.parent.newVal = value
            self.destroy()

        def makeNumPad(numPad):
            xOffset=12
            yOffset=12+rowHeight*600
            for r in range(len(numPad)):
                for c in range(len(numPad[r])):
                    glyph = numPad[r][c]
                    button = tk.Button(numPadFrame, text="{0}".format(glyph), font=("TkDefaultFont", fontSize))
                    if glyph=='del':
                        button.configure(command=delete)
                    elif glyph=='C':
                        button.configure(command=clear)
                    elif glyph == 'SUBMIT':
                        button.configure(font=("TkDefaultFont", 25))
                        button.configure(command=submit)
                    else:
                        button.configure(command = lambda glyph=glyph: nextGlyph(glyph))
                    button.pack()
                    button.place(relheight=rowHeight, relwidth=colWidth, x=xOffset, y=yOffset)
                    xOffset+=colWidth*450
                xOffset=12
                yOffset+=rowHeight*600

        def changeDropdown(*args):
            self.user = self.dropDownVar.get()

        def makeUserPane():
            dropDownLabel = tk.Label(userSelectFrame, text="Select user:")
            dropDownLabel.configure(font=("TkDefaultFont", 20))
            dropDownLabel.place(height=40, relwidth=0.95, x=5, y=10)

            self.dropDownVar = tk.StringVar(self)
            memberList = sorted(self.app.memberDict)
            memberList.append('None')
            self.dropDownVar.set('None')

            dropDown = tk.OptionMenu(userSelectFrame, self.dropDownVar, *memberList)
            dropDown.config(font=("TkDefaultFont", 20))
            options = self.nametowidget(dropDown.menuname)
            options.config(font=("TkDefaultFont",20))
            self.dropDownVar.trace('w', changeDropdown)
            dropDown.place(height=80, relwidth=0.95, x=5, y=60)

        if self.type == "user":
            makeNumPad(numPad)
            makeUserPane()
            userSelectFrame.place(relheight=1.0, relwidth=0.4, anchor="nw", x=0, y=0)
            numPadFrame.place(relheight=1.0, relwidth=0.6, anchor="ne", x=800, y=0)
        elif self.type == "admin":
            makeNumPad(numPad)
            numPadFrame.place(relheight=1.0, relwidth=1.0, anchor='nw', x=0, y=0)
