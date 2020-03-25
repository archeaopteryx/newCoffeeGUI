import tkinter as tk
import tkinter.font as tkFont

class NumPad(tk.Toplevel):

    def __init__(self, parent, app):
        tk.Toplevel.__init__(self, parent)
        self.app= app
        self.init_window()

    def init_window(self):
        self.title("NumPad")
        self.geometry("470x600")
        fontSize = 30
        self.textStr = ""

        stdKeyWidth = 3

        row1 = ['7','8','9']
        row2 = ['4','5','6']
        row3 = ['1','2','3']
        row4 = ['-','0','.']
        row5= ['del','C', 'SUBMIT']

        numPad = [row1, row2, row3, row4, row5]
        display = tk.Label(self, text="", font=("TkDefaultFont", fontSize))
        rowHeight=0.16
        colWidth= 0.33
        display.pack()
        display.place(relheight=rowHeight, relwidth=1, x=0, y=0)
        #display.grid(row=0, column=0, columnspan=3)

        def nextGlyph(glyph):
            self.textStr += glyph
            display.configure(text="%s" %self.textStr)

        def clear():
            self.textStr = ""
            display.configure(text="%s" %self.textStr)

        def delete():
            self.textStr = self.textStr[:-1]
            display.configure(text="%s" %self.textStr)

        def submit():
            self.app.newVal=self.textStr
            self.destroy()

        def makeNumPad(numPad):
            xOffset=12
            yOffset=12+rowHeight*600
            for r in range(len(numPad)):
                for c in range(len(numPad[r])):
                    glyph = numPad[r][c]
                    button = tk.Button(self, text="%s"%glyph, font=("TkDefaultFont", fontSize))
                    if glyph=='del':
                        button.configure(command=delete)
                    elif glyph=='C':
                        button.configure(command=clear)
                    elif glyph == 'SUBMIT':
                        button.configure(command=submit)
                    else:
                        button.configure(command = lambda glyph=glyph: nextGlyph(glyph))
                    button.pack()
                    button.place(relheight=rowHeight, relwidth=colWidth, x=xOffset, y=yOffset)
                    xOffset+=colWidth*450
                xOffset=12
                yOffset+=rowHeight*600

        '''def makeNumPad(numPad):
            keyRow = 1
            for r in range(len(numPad)):
                for c in range(len(numPad[r])):
                    glyph = numPad[r][c]
                    button = tk.Button(self, text="%s"%glyph, width=stdKeyWidth)
                    if glyph=='del':
                        button.configure(command=delete)
                    elif glyph=='C':
                        button.configure(command=clear)
                    elif glyph == 'submit':
                        button.configure(command=submit)
                    else:
                        button.configure(command = lambda glyph=glyph: nextGlyph(glyph))
                    button.grid(row=keyRow, column=c)
                keyRow+=1;'''

        makeNumPad(numPad)
