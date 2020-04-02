import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import fileManager
import delUserWindow
import keyboard
import numPad



class MainWindow(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("Main Window")
        self.master.geometry("800x600")
        self.newVal = None
        self.newUser = ""
        self.selectedUser=""
        self.memberDict={}
        self.milkDict={}

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

        animationFrames = [tk.PhotoImage(file='coffeeAnimation2.gif', format='gif -index %i' %(i)) for i in range(4)]
        animationLabel = tk.Label(root)
        animationLabel.place(height=2.5*stdWidth, width=2*stdWidth, anchor='ne', relx=1.0, rely=0)

        def addName():
            dialog = keyboard.KeyboardGUI(self, app)
            root.wait_window(dialog)
            if len(self.newUser) > 0:
                updateList(self, self.newUser)
            self.newUser = ""

        def addAmount():
            dialog = numPad.NumPad(self, app)
            root.wait_window(dialog)
            if self.newVal != None:
                updateLabel(self, self.newVal, self.selectedUser)
            self.newVal=None
            self.selectedUser=""

        def buyCoffee(name):
            balance = self.memberDict.get(name)
            milk = self.milkDict.get(name)
            if balance != None:
                balance=balance-20-5*milk
                self.memberDict[name]=balance
                getattr(self, 'balance_%s'%name).configure(text='{:.2f}'.format(balance/100))

        def updateMilk(name):
            milkVal = self.milkDict[name]
            newVal = (milkVal+1)%2
            self.milkDict[name]=newVal

        def updateList(self, newName):
            if newName != None:
                self.memberDict[str(newName)]=0
                self.milkDict[str(newName)] = 0
            orderedList=sorted(self.memberDict)
            yOffset=0
            button_x = 2*stdWidth
            canvas.delete("all")
            canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
            for name in orderedList:
                nameLabel=tk.Label(root, text="")
                nameLabel.configure(text="%s"%name)
                nameLabel_window = canvas.create_window((0, yOffset), anchor="nw", window=nameLabel)
                balanceLabel = tk.Label(root, text="")
                balanceLabel.configure(text='{:.2f}'.format(self.memberDict[name]/100))
                setattr(self, 'balance_%s'%name, balanceLabel)
                balance_window = canvas.create_window((stdWidth, yOffset), anchor="nw", window=balanceLabel)
                milkCheck = tk.Checkbutton(root, text="with milk", command=lambda milkName = name: updateMilk(milkName))
                if self.milkDict[name] == 1:
                    milkCheck.toggle()
                milkCheck_window = canvas.create_window((button_x, yOffset), anchor="nw", window=milkCheck)
                buy_btn = tk.Button(root, text="Buy a coffee", command = lambda nameVal = name: buyCoffee(nameVal))
                buy_btn_window = canvas.create_window((button_x, yOffset+stdHeight), anchor="nw", window=buy_btn)
                if yOffset !=0:
                    lineY = yOffset - 10
                    canvas.create_line(0, lineY, 3*stdWidth, lineY, fill="blue")
                yOffset+=2*stdHeight
            canvas.configure(yscrollcommand=scrollbar.set)

        def updateLabel(self, amount, name):
            balance = self.memberDict.get(name)
            if balance != None:
                balance += amount
                self.memberDict[name] = balance
                getattr(self, 'balance_%s'%name).configure(text='{:.2f}'.format(balance/100))

        def removeUser():
            if len(self.memberDict) == 0:
                msg = "No users to remove!"
                tk.messagebox.showinfo("Error!", msg)
            else:
                dialog = delUserWindow.DelUserWindow(self, app)
                root.wait_window(dialog)
                if len(self.selectedUser) != 0:
                    del self.memberDict[self.selectedUser]
                    updateList(self, None)
                    self.selectedUser=""

        def animate(index):
            index = index%4
            frame = animationFrames[index]
            animationLabel.configure(image=frame)
            root.after(200, animate, index+1)

        canvas.pack(side="left",fill="both", expand="True")
        scrollbar.pack(side="right", fill="y")
        container.pack()

        nameBtn = tk.Button(root, text="Add User", command=addName)
        nameBtn.place(height=stdHeight, width=stdWidth, anchor="sw", x=0, rely=1.0)

        removeBtn = tk.Button(root, text="Remove User", command=removeUser)
        removeBtn.place(height=stdHeight, width=stdWidth, anchor="sw", x=120, rely=1.0)

        paymentBtn = tk.Button(root, text="Make Payment", command=addAmount)
        paymentBtn.place(height=stdHeight, width=stdWidth, anchor = "se", relx=1.0, rely=1.0)

        try:
            self.memberDict, self.milkDict = fileManager.openList()
            updateList(self, None)
        except IOError as e:
            self.memberDict = {}
            self.milkDict= {}

        root.after(200, animate, 0)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(master=root)
    root.mainloop()
