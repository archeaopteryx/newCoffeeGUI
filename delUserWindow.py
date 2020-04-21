import tkinter as tk
import tkinter.font as tkFont

########################################################
#
# The window for selecting a user for deletion
# User is selected from a drop-down menu
#
# deletion is actually done in mainWindow
########################################################

class DelUserWindow(tk.Toplevel):

    def __init__(self, parent, app):
        tk.Toplevel.__init__(self, parent)
        self.app = app
        self.init_window()

    def init_window(self):
        self.title("Remove User")
        self.geometry("500x300")

        self.user="None"

        stdHeight = 60
        infoHeight=100
        dropHeight = infoHeight+20
        stdWidth = 400
        xCoord =(500-stdWidth)/2
        fontName = "TkDefaultFont"
        fontSize = 20

        def changeDropdown(*args):
            self.user = dropDownVar.get()

        def submit():
            if self.user != "None":
                self.app.selectedUser += self.user
            self.destroy()

        def cancel():
            self.destroy()

        infoTxt = "Select a user to remove using the dropdown menu:"
        infoBox = tk.Message(self, text=infoTxt, width = stdWidth, font=(fontName, fontSize))
        infoBox.place(height=infoHeight, width=stdWidth, anchor="nw", x=xCoord, y=0)

        dropDownVar = tk.StringVar(self)
        memberList = sorted(self.app.memberDict)
        memberList.append("None")
        dropDownVar.set("None")

        dropdownList = tk.OptionMenu(self, dropDownVar,*memberList)
        dropdownList.config(font=(fontName, fontSize))
        options = self.nametowidget(dropdownList.menuname)
        options.config(font=(fontName, fontSize))
        dropDownVar.trace('w', changeDropdown)
        dropdownList.place(height=stdHeight, width=stdWidth, anchor="nw", x=xCoord, y=dropHeight)

        submitBtn = tk.Button(self, text="Submit", command=submit)
        submitBtn.configure(font=(fontName, fontSize))
        submitBtn.place(height=stdHeight, width=150, anchor="sw", x=xCoord, rely=0.95)

        cancelBtn = tk.Button(self, text="Cancel", command=cancel)
        cancelBtn.configure(foreground = "red", font=(fontName, fontSize))
        cancelBtn.place(height=stdHeight, width=150, anchor="se", x=500-xCoord, rely=0.95)
