import csv
import pandas as pd

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk

from visualize import tracker

data_path = ""
axisOptions = ["None"]
x = ""
y = ""
z = ""
c = ""

def setX(selection):
    global x
    x = selection

def setY(selection):
    global y
    y = selection

def setZ(selection):
    global z
    z = selection

def setC(selection):
    global c
    c = selection

def UploadAction(event=None):
    global data_path, axisOptions
    data_path = tk.filedialog.askopenfilename()
    
    # clear axisOptions
    axisOptions = ["None"]

    # parse columns from csv
    with open(data_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ',')
        for row in csv_reader:
            for i in row:
                axisOptions.append(i)
            break

    # update dropdowns
    xAxis = StringVar()
    ttk.Label(config, text="X-Axis", anchor="c").grid(column=0, row=1, columnspan=1, padx=0, pady=5, sticky = tk.W+tk.E)
    ttk.OptionMenu(config, xAxis, *axisOptions, command=setX).grid(column=1, row=1, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)

    yAxis = StringVar()
    ttk.Label(config, text="Y-Axis", anchor="c").grid(column=0, row=2, columnspan=1, padx=0, pady=5, sticky = tk.W+tk.E)
    ttk.OptionMenu(config, yAxis, *axisOptions, command=setY).grid(column=1, row=2, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)

    zAxis = StringVar()
    ttk.Label(config, text="Z-Axis", anchor="c").grid(column=0, row=3, columnspan=1, padx=0, pady=5, sticky = tk.W+tk.E)
    ttk.OptionMenu(config, zAxis, *axisOptions, command=setZ).grid(column=1, row=3, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)

    cAxis = StringVar()
    ttk.Label(config, text="Color-Axis", anchor="c").grid(column=0, row=4, columnspan=1, padx=0, pady=5, sticky = tk.W+tk.E)
    ttk.OptionMenu(config, cAxis, *axisOptions, command=setC).grid(column=1, row=4, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)

    ttk.Button(config, text="Visualize", command=visualize).grid(column=0, row=5, columnspan=2, padx=15, pady=5, sticky = tk.W+tk.E)

def visualize(event=None):
    tracker(data_path, [x, y, z, c])
    

root = Tk()
root.title("HABViz by Penn HAB")
# root.geometry("200x350")
config = ttk.Frame(root, padding=10)
config.grid()

# ttk.Label(config, text="HABViz").grid(column=0, row=0, columnspan=2, padx=15, pady=5, sticky = tk.W+tk.E)
ttk.Button(config, text="Upload", command=lambda: UploadAction()).grid(column=0, row=0, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)
ttk.Button(config, text="Demo", command=root.destroy).grid(column=1, row=0, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)



root.mainloop()