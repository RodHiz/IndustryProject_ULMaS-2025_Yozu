from tkinter import *

root = Tk()

click = 0

#Entry is used to make a text box
inputField = Entry(root, width=40, bg="lightgreen").grid(row=10, column=10)


def onClick():
    outputField = "loading" + inputField.get()
    field = Label(root, text=outputField).grid(row=6, column=6)
    click += 1

#creating label widget
title = Label(root, text="Predicting road damage").grid(row=0, column=0)

#puts it onto the screen                                    /\
#without this, it will not show up                          ||
#title.pack()                                               ||
#cant use both pack and grid                                ||
#or do title.grid(row=0, column=0)                          ||

subtitle  = Label(root, text="welcome to the road damage prediction app").grid(row=5, column=5)


#can add state=DISABLED/ACTIVE to make it un/clickable
#padx/y changes size of button
#command is what happens when button is clicked
#fg, foreground, changes color of text
#bg, background, changes color of button
#can also use hex codes for colors
if(click == 0):
    button = Button(root, text="what parameter",padx=50,pady=49, command=onClick, fg="red", bg="lightblue").grid(row=3, column=4)


#running the main loop
#this will keep the window open
#constantly updates where the cursor is
root.mainloop()