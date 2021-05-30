from tkinter import *
from tkinter import ttk

"""
TODO label above nums that shows result. add division. hook buttons up to calc class.

"""
root = Tk()

content = ttk.Frame(root, padding=(6,12))
frame = ttk.Frame(content, relief="ridge", width=200, height=100)
title = root.title("Jonty's Calculator")


#calc buttons

#row 4
empty = ttk.Button(frame, text="empty")
zero = ttk.Button(frame, text="0")
decimal = ttk.Button(frame, text=".")
equal = ttk.Button(frame, text="=")
#row 3
one = ttk.Button(frame, text="1")
two = ttk.Button(frame, text="2")
three = ttk.Button(frame, text="3")
four = ttk.Button(frame, text="4")
#row 
five = ttk.Button(frame, text="5")
six = ttk.Button(frame, text="6")
seven = ttk.Button(frame, text="7")
eight = ttk.Button(frame, text="8")
nine = ttk.Button(frame, text="9")

multiply = ttk.Button(frame, text="x")
subtract = ttk.Button(frame, text="-")
add = ttk.Button(frame, text="+")
#calc grid layout

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)

#row 4
empty.grid(column=0, row=4)
zero.grid(column=1, row=4)
decimal.grid(column=2, row=4)
equal.grid(column=3, row=4)
#row 3
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
add.grid(column=3, row=3)
#row 2
four.grid(column=0, row=2)
five.grid(column=1, row=2)
six.grid(column=2, row=2)
subtract.grid(column=3, row=2)
#row 1
seven.grid(column=0, row=0)
eight.grid(column=1, row=0)
nine.grid(column=2, row=0)
multiply.grid(column=3, row=0)


root.mainloop()