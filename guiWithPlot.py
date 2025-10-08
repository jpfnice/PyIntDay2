import numpy as np
import tkinter as tk
import sys

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class MyWin(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self) # super().__init__()
        
        self.minsize(300,100)
        self.title("Demo: Tk + Matplotlib")
        
        # This portion of the code plot data (a curve here) with the help of the matplotlib module:
            
        fig = plt.figure()
        self.ax = fig.add_subplot(111)
        self.t = np.arange(0.0,3.0,0.01)
        self.s = np.sin(np.pi*self.t)
        self.ax.plot(self.t, self.s)
        
        # A special tkinter widget (a canvas) is placed in the main window to hold the plot
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        plot_widget = self.canvas.get_tk_widget()
        plot_widget.grid(row=0, column=0, columnspan=2)
        
        # The button update provide a way to update the plot (it draws a new 
        # curve each time it is pressed)
        self.bt1=tk.Button(self,text="Update", command=self.update)
        self.bt1.grid(row=1, column=0, sticky=tk.E, padx=20)
        
        self.bt2=tk.Button(self,text="Exit",command=sys.exit)
        self.bt2.grid(row=1, column=1, sticky=tk.W)
        
    def update(self):
        import random
        # This portion of the code plot a new curve with the help of the matplotlib module:
        self.s = np.cos(np.pi*self.t+random.randint(1,100))
        self.ax.plot(self.t, self.s)
        self.canvas.draw()
        
if __name__== "__main__":
    matplotlib.use('TkAgg')
    r=MyWin()
    tk.mainloop()