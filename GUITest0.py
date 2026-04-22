"""
Examples of GUI modules:
    
    tkinter (tk -> tcl)

    PyQT (QT -> C++)

    PyGTK (GTK -> C++)

    WXPython

Some common concepts:

    Container : Window (tk frame)

    Final component: Button, Entry, Scrollbars

    Layout Managers (Geometry Managers): placer, gridder, packer

    Event: event source + event listener

    GUI Builder

"""

import tkinter as tk 

class MyWindow(tk.Tk):
    
    def __init__(self):
        
        super().__init__() # to call the method __init__ of Tk
        self.minsize(500,200)
        self.title("An example")
        
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=2)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        
        bt1=tk.Button(self, text="Start", command=self.start)
        bt1.grid(row=0, column=1)
        
        bt2=tk.Button(self, text="Stop")
        bt2.grid(row=0, column=2, sticky=tk.E+tk.W+tk.N+tk.S, columnspan=2)
        
        bt2=tk.Button(self, text="Clear")
        bt2.grid(row=0, column=4, sticky=tk.E+tk.W)
        
        txt=tk.Text(self)
        txt.grid(row=1, column=1, columnspan=5)
        
        sc=tk.Scrollbar()
        sc.grid(row=0, column=0, sticky=tk.S+tk.N, rowspan=2)
        
    def start(self):
        print("Click on start")
        
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()
