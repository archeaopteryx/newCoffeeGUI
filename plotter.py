from time import strftime, localtime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import MaxNLocator
#import tkinter as tk
#import sys

########################################################
# Initalizes the coffees plot and updates its values
#
# If the day has changed, then the Plotter re-initializes itself with None values.
# The hours displayed on the x axis are determined by the time when the first
# coffee of the day is purchased
#
# If the day has not changed, then the hour is checked and the number of coffees
# for that hour is incremented
########################################################

class Plotter():

    def __init__(self):

        self.day = None
        self.firstHour = None

        self.coffees =  None
        self.hours = None
        self.init_values()

    def init_values(self):
        self.day = int(strftime('%j', localtime()))
        self.firstHour = int(strftime('%H', localtime()))
        numHours = 24-self.firstHour
        self.coffees = np.zeros((numHours), dtype = int)
        self.hours=np.array(np.arange(self.firstHour, 24), dtype=int)

    def update_values(self):
        today = int(strftime('%j', localtime()))
        if today == self.day:
            hour = int(strftime('%H', localtime()))
            hourIndex = hour-self.firstHour
            self.coffees[hourIndex]+=1
            return(self.coffees, self.hours)
        else:
            self.init_values()
            self.update_values()


    #def close():
    #    sys.exit(0)

def makePlot(coffees, hours):

    figure = plt.Figure(figsize=(5,5))
    ax = figure.add_subplot(111)
    ax.bar(x=hours, height=coffees, width=1.0, edgecolor='lightsteelblue',linewidth=1)
    tickpoints = hours[::2]
    ax.set_xticks(tickpoints)
    ax.set_xticklabels(tickpoints)
    ax.set_xlabel("Hour", fontsize=12)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylabel("Cups of Coffee", fontsize=12)
    return figure


#############################################
#For testing:
'''
root = tk.Tk()
testday =98
testhour = 9
testhours = np.array(np.arange(testhour,24), dtype=int)
testcoffee=np.array([2,0,4,1,2,5,2,3,1,1,0,0,0,0,0])

day = testday
firstHour = testhour
hours = testhours
coffees = testcoffee
update_values()
##############################################
figure = plt.Figure(figsize=(5,5))
ax = figure.add_subplot(111)
ax.bar(x=hours, height=coffees, width=1.0, edgecolor='lightsteelblue',linewidth=1)
tickpoints = hours[::2]
ax.set_xticks(tickpoints)
ax.set_xticklabels(tickpoints)
ax.set_xlabel("Hour", fontsize=12)
ax.set_ylabel("Cups of Coffee", fontsize=12)
bars = FigureCanvasTkAgg(figure, root)
bars.get_tk_widget().pack()


root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
'''
##############################################
