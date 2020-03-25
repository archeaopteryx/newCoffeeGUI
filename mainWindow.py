import tkinter as tk
import keyboard
import numPad



class MainWindow(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("Main Window")
        self.newVal = ""

        def addName():
            dialog = keyboard.KeyboardGUI(self, app)
            root.wait_window(dialog)
            field='name'
            updateLabel(self, self.newVal, field)
            self.newVal = ""

        def addAmount():
            dialog = numPad.NumPad(self, app)
            root.wait_window(dialog)
            field='amount'
            updateLabel(self, self.newVal,field)
            self.newVal=""

        def updateLabel(self, value, field):
            if field == 'name':
                name.configure(text=value)
            elif field == 'amount':
                balance.configure(text=value)

        stdHeight = 40
        stdWidth = 100

        nameLabel = tk.Label(root, text="Name:")
        nameLabel.pack()
        nameLabel.place(height = stdHeight, width= stdWidth, x=0, y=0)
        name = tk.Label(root, text="")
        name.pack()
        name.place(height=stdHeight, width=stdWidth, x=100, y=0)
        nameBtn = tk.Button(root, text="Enter name", command=addName)
        nameBtn.pack()
        nameBtn.place(height=stdHeight, width=stdWidth, x=200, y=0)

        balanceLabel = tk.Label(root, text="Balance:")
        balanceLabel.pack()
        balanceLabel.place(height=stdHeight, width=stdWidth, x=0, y=40)
        balance = tk.Label(root, text="")
        balance.pack()
        balance.place(height=stdHeight, width=stdWidth, x=100, y=40)
        balanceBtn = tk.Button(root, text="Enter Balance", command=addAmount)
        balanceBtn.pack()
        balanceBtn.place(height=stdHeight, width=stdWidth, x=200, y=40)


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(master=root)
    root.mainloop()
