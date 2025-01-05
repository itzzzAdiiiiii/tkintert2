from tkinter import *
#creating window
screen = Tk()
#def function for conversion
def conversion():
    Gram = float(value.get())*1000
    gram.insert(END,Gram)
    Pound = float(value.get())*2.20462
    pound.insert(END,Pound)
    Ounce = float(value.get())*35.27
    ounce.insert(END,Ounce)

#creating label widgets 
kgs = Label(screen,text= "enter the weight in kgs")
value = StringVar()
Input = Entry(screen, textvariable= value)
grams = Label(screen,text= "grams")
pounds = Label(screen,text="pounds")
ounces = Label(screen,text="ounces")
gram = Text(screen, height = 1, width = 20)
ounce = Text(screen, height = 1, width = 20)
pound = Text(screen, height = 1, width = 20)
convert = Button(screen, text = "convert", command = conversion, width = 15)
kgs.grid(row = 0,column = 1)
grams.grid(row = 1, column = 0)
pounds.grid(row = 1, column = 1)
ounces.grid(row= 1, column= 2)
Input.grid(row = 0, column = 2)
gram.grid(row = 2, column = 0)
ounce.grid(row = 2, column = 2)
pound.grid(row = 2, column = 1)
convert.grid(row = 0, column = 0)
screen.mainloop()
