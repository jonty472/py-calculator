"""
plan -
    get button press 
    evaluate button press by print
    store button value(s)
    check button values by using the self.entry.get() function with add_char

todo -
    how to take different number of args (dynamic)
    
"""
from tkinter import *
from tkinter import ttk

class Calculator:

    def __init__(self, root):
        
        # window title
        root.title("Calculator")

        # Calc Frame
        mainframe = ttk.Frame(root, relief="ridge", width=200, height=100)
        mainframe.grid(column=0, row=0)
        
        # Declare input 
            #Entry
        self.entryCalc = Entry(mainframe, width=10)
        self.entryCalc.pack()
            #Buttons
        self.calcBtn = Button(mainframe, text="calc", command=lambda:self.evaluate())
        self.calcBtn.pack()

        self.oneBtn = Button(mainframe, text="1", command=lambda:self.set_text("1"))
        self.oneBtn.pack()

        self.twoBtn = Button(mainframe, text="2", command=lambda:self.set_text("2"))
        self.twoBtn.pack()

        self.addBtn = Button(mainframe, text="+", command=lambda:self.set_text("+"))
        self.addBtn.pack()
    
    def set_text(self, text):
        """
        entry from button press
        """
        self.entryCalc.insert(END, text)
        return
        
    
    def evaluate(self):
        """
        uses the eval() function from python to calculate the answer
        """
        self.eval = self.entryCalc.get()
        self.answer = eval(self.eval)
        self.entryCalc.delete(0, END)
        self.entryCalc.insert(END, self.answer)
        


root = Tk()
Calculator(root)
root.mainloop()