from tkinter import *
from time import strftime
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
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
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'edit', menu=edit)
edit.add_command(label="undo", command = None)
edit.add_command(label="redo", command = None)
edit.add_command(label="cut", command = None)
edit.add_separator()
edit.add_command(label="copy", command = None)
edit.add_command(label="paste", command = None)
edit.add_command(label="find", command = None)
edit.add_command(label="replace", command = None)
edit.add_separator()
view = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'view', menu=view)
view.add_command(label="appearance", command = None)
view.add_command(label="search", command = None)
view.add_separator()
view.add_command(label="run", command = None)
view.add_command(label="extensions", command = None)
view.add_separator()
view.add_command(label="testing", command = None)
view.add_command(label="problems", command = None)
view.add_command(label="output", command = None)
view.add_command(label="terminal", command = None)
view.add_separator()
screen.config(menu=menubar)
box = Spinbox(screen,from_=0,to=99)
box.pack()
progress = Progressbar(screen,orient=HORIZONTAL,length = 100,mode="determinate")
def loading():
    import time
    progress['value'] = 20
    screen.update_idletasks()
    time.sleep(1)
    progress['value'] = 40
    screen.update_idletasks()
    time.sleep(1)
    progress['value'] = 80
    screen.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    screen.update_idletasks()
    time.sleep(1)
progress.pack()
start = Button(screen,text = "start",command=loading)
start.pack()
#filedialog
def filed ():
    dbox = askopenfile
mainloop()
