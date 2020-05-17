import tkinter as tk
from platform import mac_ver
import sys
from src.mainWindow import MainWindow

if __name__ == '__main__':
    if len(mac_ver()[0]) != 0:
        #mac_ver returns a tuple, first entry is version number
        print("MacOS not supported. Aborted run.")
        sys.exit(0)
    root = tk.Tk()
    app = MainWindow(master=root)
    root.mainloop()
