import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as mb


class MyWindow(tk.Tk):
    
    def __init__(self):
        super().__init__() # To call the method __init__() of the "super" class (here Tk)
        
        self.minsize(900,300)
        self.maxsize(1200,600)
        self.title("Tkinter Exercise")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
       
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        
        # Binding variables:
        self.nameStr=tk.StringVar()
        self.priceFloat=tk.DoubleVar()
        self.qtyInt=tk.IntVar()
      
        sb = tk.Scrollbar()
        
        customFont = tkFont.Font(family="Courier", size=16)
        
        self.listB = tk.Listbox(font=customFont)
        self.listB.grid(row=0, column=0, columnspan=3, padx=0, pady=10, sticky=tk.E+tk.W+tk.N+tk.S)
        sb.grid(row=0, column=3, padx=0, pady=10, sticky=tk.N+tk.S)
        
        sb.config(command=self.listB.yview)
        self.listB.config(yscrollcommand=sb.set)
        
        nameL=tk.Label(self, text="Name")
        nameL.grid(row=1, column=0, padx=10, pady=10)
        
        nameE=tk.Entry(self, textvariable=self.nameStr)
        nameE.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E+tk.W)
        
        priceL=tk.Label(self, text="Price")
        priceL.grid(row=1, column=1, padx=10, pady=10)
        
        priceE=tk.Entry(self, textvariable=self.priceFloat)
        priceE.grid(row=2, column=1, padx=10, pady=10,sticky=tk.E+tk.W)
        
        qtyL=tk.Label(self, text="Qty")
        qtyL.grid(row=1, column=2, padx=10, pady=10)
        
        qtyE=tk.Entry(self, textvariable=self.qtyInt)
        qtyE.grid(row=2, column=2, padx=10, pady=10, sticky=tk.E+tk.W)
        
        # TODO: Add the 3 buttons: insert, update and delete
        
        # the bind() method is used to register an event listener with
        # the event "ListBoxSelect" of the ListBox listB:
            
        self.listB.bind('<<ListboxSelect>>', self.onSelect)    
        
        self.setMenu()
        self.onLoad()
      
    def insert(self):
        # TO DO: insert a new product in the table
        pass
        
    def update(self):
        # TO DO: update the selected product
        pass
        
    def delete(self):
        # TO DO: delete the selected product
        pass
        pass
          
        
    def onSelect(self, evt):
        
        # TODO: retrive the selected product and populate, with the help of it
        # the differents entries
        pass
    
    def setMenu(self):
        import sys
        mainmenu = tk.Menu(self)  # MenuBar 
        menuFile = tk.Menu(mainmenu)  # Menu 
        menuFile.add_command(label="Quit", command=sys.exit) 
  
        menuHelp = tk.Menu(mainmenu) # Menu
        menuHelp.add_command(label="About", command=self.about) 
        
        mainmenu.add_cascade(label = "File", menu=menuFile) 
        mainmenu.add_cascade(label = "Help", menu=menuHelp) 
        
        # display the menu
        self.config(menu = mainmenu) 
        
    def onLoad(self):
        #TODO: construct the listbox with the help of the table product
        # "select * from product"
        pass
    def about(self): 
        mb.showinfo("A tkinter example", "Version 1.0")       
               
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()