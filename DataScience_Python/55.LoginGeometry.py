# WAP to develop a login page using geometry 

from tkinter import *

Home = Tk()
Home.geometry("400x400")
Home.title("___LOGIN___")

l1= Label(Home, text="Username: ")
l1.place(x= 50, y= 10)

e1= Entry(Home)
e1.place(x= 150, y= 10)

l2= Label(Home, text="Password: ")
l2.place(x= 50, y= 50)

e2= Entry(Home)
e2.place(x= 150, y= 50)

b1 = Button(Home, text="LOGIN", bg="GREEN", fg="WHITE")
b1.place(x= 50, y= 90)
b2 = Button(Home, text="Forgot", bg="RED", fg="WHITE")
b2.place(x= 150, y= 90)
b3 = Button(Home, text="CANCEL", bg="#EE0000", fg="WHITE")
b3.place(x= 250, y= 90)



Home.mainloop()