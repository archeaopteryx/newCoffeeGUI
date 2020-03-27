import tkinter as tk
from tkinter import ttk
import keyboard
import numPad



class MainWindow(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("Main Window")
        self.master.geometry("600x600")
        self.newVal = ""
        self.memberDict={} #dictionaries can be sorted

        stdHeight = 40
        stdWidth = 100

        container = ttk.Frame(root)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command = canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
        "<Configure>",
         lambda e: canvas.configure(
         scrollregion=canvas.bbox("all")))

        canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        def addName():
            dialog = keyboard.KeyboardGUI(self, app)
            root.wait_window(dialog)
            updateList(self, self.newVal)
            self.newVal = ""

        def addAmount():
            dialog = numPad.NumPad(self, app)
            root.wait_window(dialog)
            field='amount'
            updateLabel(self, self.newVal,field)
            self.newVal=""

        '''def updateLabel(self, value, field):
            if field == 'name':
                name.configure(text=value)
                self.memberDict = sorted(self.memberDict)
                print(self.memberDict)
            elif field == 'amount':
                balance.configure(text=value)'''


        def updateList(self, newName):
            self.memberDict[str(newName)]=0
            orderedList=sorted(self.memberDict)
            yOffset=0
            canvas.delete("all")
            canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
            for name in orderedList:
                nameLabel=tk.Label(root, text="")
                nameLabel.configure(text="%s"%name)
                #nameLabel.place(height=stdHeight, width=stdWidth, x=0, y=yOffset)
                nameLabel_window = canvas.create_window((0, yOffset), anchor="nw", window=nameLabel)
                balanceLabel = tk.Label(root, text="")
                balanceLabel.configure(text="%s"%str(self.memberDict[name]))
                #balanceLabel.place(height=stdHeight, width=stdWidth, x=stdWidth, y=yOffset)
                balance_window = canvas.create_window((stdWidth, yOffset), anchor="nw", window=balanceLabel)
                if yOffset !=0:
                    lineY = yOffset - 10
                    canvas.create_line(0, lineY, 3*stdWidth, lineY, fill="blue")
                yOffset+=stdHeight
            canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left",fill="both", expand="True")
        scrollbar.pack(side="right", fill="y")
        container.pack()

        nameBtn = tk.Button(root, text="Add Name", command=addName)
        nameBtn.place(height=stdHeight, width=stdWidth, anchor="sw", x=200, rely=1.0)

        paymentBtn = tk.Button(root, text="Make Payment", command=addAmount)
        paymentBtn.place(height=stdHeight, width=stdWidth, anchor = "sw", x=320, rely=1.0)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(master=root)
    root.mainloop()
