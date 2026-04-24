"""
Note: the goal is to display a counter incremented every 0.5 seconds
This version those not work:
    the event listener is doing a loop, the tkinter "engine" is locked in this
    loop and is not able to treat any other event or display any widget
    
"""

import tkinter as tk
import time


class MyWindow(tk.Tk):
    
    def __init__(self):
        super().__init__() # To call the method __init__() of the "super" class (here Tk)
        
        self.minsize(300,100)
        self.maxsize(300,100)
        self.title("Tkinter Example")

        self.qtyInt=tk.IntVar()
        
        qtyE=tk.Entry(self, textvariable=self.qtyInt)
        qtyE.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E+tk.W)
        
        loadB=tk.Button(self, text="start", command=self.start)
        loadB.grid(row=0, column=1, padx=10, pady=10)
        
        loadB=tk.Button(self, text="stop", command=self.stop)
        loadB.grid(row=0, column=2, padx=10, pady=10)
        
       
    def start(self):
        self.OkToRun=True
        self.qtyInt.set("0")
        while self.OkToRun:
            value=int(self.qtyInt.get())
            value+=1
            time.sleep(0.5)
            self.qtyInt.set(str(value))
   
    def stop(self):
        self.OkToRun=False
          
         
               
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()