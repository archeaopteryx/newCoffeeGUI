import tkinter as tk
import tkinter.font as tkFont

class DelUserWindow(tk.Toplevel):

    def __init__(self, parent, app):
        tk.Toplevel.__init__(self, parent)
        self.app = app
        self.init_window()

    def init_window(self):
        self.title("Remove User")
        self.geometry("400x400")

        self.user="None"

        stdHeight = 60
        stdWidth = 300
        xCoord =(400-stdWidth)/2

        def changeDropdown(*args):
            self.user = dropDownVar.get()

        def submit():
            if self.user != "None":
                self.app.selectedUser += self.user
            self.destroy()

        infoLabelTxt = "Select a user to remove using the dropdown menu:"
        infoLabel = tk.Label(self, text=infoLabelTxt)
        infoLabel.place(height =stdHeight, width=stdWidth, anchor="nw", x=xCoord, y=0)

        dropDownVar = tk.StringVar(self)
        memberList = sorted(self.app.memberDict)
        memberList.append("None")
        dropDownVar.set("None")

        dropdownList = tk.OptionMenu(self, dropDownVar,*memberList)
        dropDownVar.trace('w', changeDropdown)
        dropdownList.place(height=stdHeight, width=stdWidth, anchor="nw", x=xCoord, y=stdHeight)

        submitBtn = tk.Button(self, text="Submit", command=submit)
        submitBtn.place(height=stdHeight, width=stdWidth, anchor="nw", x=xCoord, y=2*stdHeight)
