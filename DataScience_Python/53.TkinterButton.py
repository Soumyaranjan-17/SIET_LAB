# WAP to create color buttons on tk

from tkinter import *

Home = Tk()
Home.title("Buttons")

b1 = Button(Home, text="RED", bg="RED", fg="WHITE").pack()
b2 = Button(Home, text="BLUE", bg="BLUE", fg="WHITE").pack()
b3 = Button(Home, text="YELLOW", bg="YELLOW", fg="#000").pack()
b4 = Button(Home, text="GREEN", bg="GREEN", fg="WHITE").pack()

Home.mainloop()