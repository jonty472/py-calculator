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
        
        root.title("Calculator")

        # Calc Frame
        mainframe = ttk.Frame(root, relief="ridge", width=200, height=100)
        mainframe.grid(column=0, row=0)
        # Declare input 
        self.entry = Entry(root).grid(row=0, column=0, columnspan=6, sticky="w")
        
        self.createWidgets()
        self.grid()

    
    def add_chr(self, char, btn=None):
        pass
    
    def evaluate(self):
        """
        use the eval() function from python. 
        """
        pass

    def createWidgets(self):
        """
        Widgets used in calcualtor
        """
        
        self.division = ttk.Button(mainframe, text="/").grid(column=0, row=4, command=lambda: self.add_chr('/')
        #self.multiply = ttk.Button(mainframe, text="*").grid(column=0, row=4, command=lambda: self.add_chr('*')
        self.decimal = ttk.Button(mainframe, text=".").grid(column=2, row=4, command=lambda: self.add_chr('.')
        self.equal = ttk.Button(mainframe, text="=").grid(column=3, row=4, command=lambda: self.evaluate()
        self.add = ttk.Button(mainframe, text="+").grid(column=3, row=3, command=lambda: self.add_chr('+')
        self.subtract = ttk.Button(mainframe, text="-").grid(column=3, row=2, command=lambda: self.add_chr('-')
    
        self.zero = ttk.Button(mainframe, text="0").grid(column=1, row=4, command=lambda: self.add_chr(0)
        self.one = ttk.Button(mainframe, text="1").grid(column=0, row=3, command=lambda: self.add_chr(1)
        self.two = ttk.Button(mainframe, text="2").grid(column=1, row=3, command=lambda: self.add_chr(2)
        self.three = ttk.Button(mainframe, text="3").grid(column=2, row=3, command=lambda: self.add_chr(3)
        self.four = ttk.Button(mainframe, text="4").grid(column=0, row=2, command=lambda: self.add_chr(4)
        
        self.five = ttk.Button(mainframe, text="5").grid(column=1, row=2, command=lambda: self.add_chr(5)
        self.six = ttk.Button(mainframe, text="6").grid(column=2, row=2, command=lambda: self.add_chr(6)
        self.seven = ttk.Button(mainframe, text="7").grid(column=0, row=1, command=lambda: self.add_chr(7)
        self.eight = ttk.Button(mainframe, text="8").grid(column=1, row=1, command=lambda: self.add_chr(8)
        self.nine = ttk.Button(mainframe, text="9").grid(column=2, row=1, command=lambda: self.add_chr(9)




root = Tk()
Calculator(root)
root.mainloop()