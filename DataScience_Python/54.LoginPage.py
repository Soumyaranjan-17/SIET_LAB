# WAP to develop login page 

from tkinter import *

Home = Tk()
Home.title("___LOGIN___")

l1= Label(Home, text="Username: ").grid(row=0, column=0)
e1= Entry(Home).grid(row=0, column=1)
l2= Label(Home, text="Password: ").grid(row=1, column=0)
e2= Entry(Home).grid(row=1, column=1)

b1 = Button(Home, text="LOGIN", bg="GREEN", fg="WHITE").grid(row=2, column=0)
b2 = Button(Home, text="Forgot", bg="RED", fg="WHITE").grid(row=2, column=1)
b3 = Button(Home, text="CANCEL", bg="#EE0000", fg="WHITE").grid(row=2, column=2)



Home.mainloop()