from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("HABViz by Penn HAB")
# root.geometry("200x350")
config = ttk.Frame(root, padding=10)
config.grid()

axisOptions = ["None", "Altitude", "Longitude", "Latitude"]

# ttk.Label(config, text="HABViz").grid(column=0, row=0, columnspan=2, padx=15, pady=5, sticky = tk.W+tk.E)
ttk.Button(config, text="Upload", command=root.destroy).grid(column=0, row=0, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)
ttk.Button(config, text="Demo", command=root.destroy).grid(column=1, row=0, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)

xAxis = StringVar()
ttk.Label(config, text="X-Axis", anchor="c").grid(column=0, row=1, columnspan=1, padx=0, pady=5, sticky = tk.W+tk.E)
ttk.OptionMenu(config, xAxis, *axisOptions).grid(column=1, row=1, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)

yAxis = StringVar()
ttk.Label(config, text="Y-Axis", anchor="c").grid(column=0, row=2, columnspan=1, padx=0, pady=5, sticky = tk.W+tk.E)
ttk.OptionMenu(config, yAxis, *axisOptions).grid(column=1, row=2, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)

zAxis = StringVar()
ttk.Label(config, text="Z-Axis", anchor="c").grid(column=0, row=3, columnspan=1, padx=0, pady=5, sticky = tk.W+tk.E)
ttk.OptionMenu(config, zAxis, *axisOptions).grid(column=1, row=3, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)

cAxis = StringVar()
ttk.Label(config, text="Color-Axis", anchor="c").grid(column=0, row=4, columnspan=1, padx=0, pady=5, sticky = tk.W+tk.E)
ttk.OptionMenu(config, cAxis, *axisOptions).grid(column=1, row=4, columnspan=1, padx=15, pady=5, sticky = tk.W+tk.E)

ttk.Button(config, text="Visualize", command=root.destroy).grid(column=0, row=5, columnspan=2, padx=15, pady=5, sticky = tk.W+tk.E)

root.mainloop()