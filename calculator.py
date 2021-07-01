"""
todo - 
    fix frame 
    add the rest of the buttons
    
    
"""
from tkinter import *
from tkinter import ttk

class Calculator:

    def __init__(self, root):
        
        # window title
        root.title("Calculator")

        # frame
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
       # entry button
        self.calcEntry = ttk.Entry(mainframe, width=12)
        self.calcEntry.grid(column=0, row=0, sticky=(W, E), columnspan=3)

        # calc buttons
       
        ttk.Button(mainframe, text="x", command=lambda:self.set_text("*")).grid(column=3, row=2, sticky=W)
        ttk.Button(mainframe, text="-", command=lambda:self.set_text("-")).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text="+", command=lambda:self.set_text("+")).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text="=", command=lambda:self.evaluate()).grid(column=3, row=5, sticky=W)

        ttk.Button(mainframe, text="C", command=lambda:self.clear_text()).grid(column=2, row=1, sticky=W)

        ttk.Button(mainframe, text=")", command=lambda:self.set_text(")")).grid(column=1, row=1, sticky=E)
        ttk.Button(mainframe, text="8", command=lambda:self.set_text("8")).grid(column=1, row=2, sticky=E)
        ttk.Button(mainframe, text="5", command=lambda:self.set_text("5")).grid(column=1, row=3, sticky=E)
        ttk.Button(mainframe, text="2", command=lambda:self.set_text("2")).grid(column=1, row=4, sticky=E)
        ttk.Button(mainframe, text="0", command=lambda:self.set_text("0")).grid(column=1, row=5, sticky=E)
        
        ttk.Button(mainframe, text="(", command=lambda:self.set_text("(")).grid(column=0, row=1, sticky=E)
        ttk.Button(mainframe, text="7", command=lambda:self.set_text("7")).grid(column=0, row=2, sticky=E)
        ttk.Button(mainframe, text="4", command=lambda:self.set_text("4")).grid(column=0, row=3, sticky=E)
        ttk.Button(mainframe, text="1", command=lambda:self.set_text("1")).grid(column=0, row=4, sticky=E)
        ttk.Button(mainframe, text=".", command=lambda:self.set_text(".")).grid(column=0, row=5, sticky=E)

        ttk.Button(mainframe, text="9", command=lambda:self.set_text("9")).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="6", command=lambda:self.set_text("6")).grid(column=2, row=3, sticky=(W, E))
        ttk.Button(mainframe, text="3", command=lambda:self.set_text("3")).grid(column=2, row=4, sticky=(W, E))
        ttk.Button(mainframe, text="/", command=lambda:self.set_text("/")).grid(column=2, row=5, sticky=(W, E))
    
    def set_text(self, text):
        """
        entry from button
        """
        self.calcEntry.insert(END, text)
        return
        
    
    def evaluate(self):
        """
        uses the eval() function from python to calculate the answer
        """
        self.eval = self.calcEntry.get()
        self.answer = eval(self.eval)
        self.calcEntry.delete(0, END)
        self.calcEntry.insert(END, self.answer)
        
    def clear_text(self):
        """
        clears the entry widget
        """
        self.calcEntry.delete(0, END)


root = Tk()
Calculator(root)
root.mainloop()