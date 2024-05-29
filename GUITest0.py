import tkinter as tk 

class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__() # to call the method __init__ of Tk
        self.minsize(300,500)
        self.title("An example")
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        bt1=tk.Button(self, text="Start", command=self.start)
        bt1.grid(row=0, column=1, sticky=tk.E+tk.W)
        bt2=tk.Button(self, text="Stop")
        bt2.grid(row=0, column=2, sticky=tk.E+tk.W)
        bt2=tk.Button(self, text="Clear")
        bt2.grid(row=3, column=2, sticky=tk.E+tk.W)
        sc=tk.Scrollbar()
        sc.grid(row=0, column=0, sticky=tk.S+tk.N, rowspan=4)
        
    def start(self):
        print("Click on start")
        
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()
