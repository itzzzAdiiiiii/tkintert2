from tkinter import *
from time import strftime
from tkinter.ttk import *
screen = Tk()
screen.title("menu")
menubar = Menu(screen)
#adding file menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label="new file", command = None)
file.add_command(label="new folder", command = None)
file.add_command(label="open file", command = None)
file.add_separator()
screen.config(menu=menubar)
mainloop()