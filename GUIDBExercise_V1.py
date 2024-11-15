"""
The purpose of this code is to offer a GUI that could help to visualize and modify the SQLLite table product (this table is composed of the columns name, price and qty).

This GUI, with the help of a ListBox, will make the rows of the table product appear one below the other.

After having clicked on one ListBox element you gonna be able to:
    update it
    delete it
    insert an updated version of it

The update/delete/insert will concern both the table product and the ListBox widget.

"""
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
        self.columnconfigure(3, weight=0)
       
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        
        # Binding variables:
        self.nameStr=tk.StringVar()
        self.priceFloat=tk.DoubleVar()
        self.qtyInt=tk.IntVar()
        self.counterInt=tk.IntVar()
        self.activeBool=tk.BooleanVar()
        self.activeBool.set(True)
        
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
        
        countL=tk.Label(self, text="Number of rows")
        countL.grid(row=3, column=1, padx=10, pady=10, sticky=tk.E+tk.W)
        
        countE=tk.Entry(self, textvariable=self.counterInt, justify=tk.CENTER, width=6)
        countE.grid(row=4, column=1, padx=10, pady=10)
        
        # TODO: Add the 3 buttons: insert, update and delete
        
        loadB=tk.Button(self, text="update", command=self.update)
        loadB.grid(row=2, column=3, padx=10, pady=10)
        
        loadB=tk.Button(self, text="insert", command=self.insert)
        loadB.grid(row=3, column=3, padx=10, pady=10)
        
        loadB=tk.Button(self, text="delete", command=self.delete)
        loadB.grid(row=4, column=3, padx=10, pady=10)
        
        # DONE
         
        checkB=tk.Checkbutton(self, text="active", variable=self.activeBool, command=self.activate)
        checkB.grid(row=5, column=3, padx=10, pady=10)
        # the bind() method is used to register an event listener with
        # the event "ListBoxSelect" of the ListBox listB:
            
        self.listB.bind('<<ListboxSelect>>', self.onSelect)    
        
        self.setMenu()
        self.onLoad()
        
    def clear(self):
        self.nameStr.set("")
        self.priceFloat.set(0.0)
        self.qtyInt.set(0)
        
    def activate(self):
        if self.activeBool.get():
            self.listB.bind('<<ListboxSelect>>', self.onSelect)
        else:
            self.listB.unbind('<<ListboxSelect>>')
            self.clear()
            
    def insert(self):
        # TODO: 
        import sqlite3
        with sqlite3.connect(r"epfl.db") as conn:
            try:
                cursor=conn.cursor()
                cursor.execute (f"insert into product values ('{self.nameStr.get()}', {self.priceFloat.get()}, {self.qtyInt.get()})")
                cursor.execute("commit")
                cursor.close()
                self.onLoad() 
            except Exception as ex:
                print(ex)
           
    def countRows(self):
        import sqlite3
        with sqlite3.connect(r"epfl.db") as conn:
            try:
                cursor=conn.cursor()
                cursor.execute ("select count(*) from product")
                while True:
                    row = cursor.fetchone()
                    if row == None: break
                    cursor.close()
                    return (int(row[0]))
                cursor.close()
                self.onLoad()
            except Exception as ex:
                print(ex)    
            
    def update(self):
        # TODO: 
        import sqlite3
        with sqlite3.connect(r"epfl.db") as conn:
            try:
                
                cursor=conn.cursor()
                cursor.execute (f"update product set price={self.priceFloat.get()}, qty={self.qtyInt.get()} where name='{self.nameStr.get()}'")
                cursor.execute("commit")
                cursor.close()
                self.onLoad()                
            except Exception as ex:
                print(ex)
         
    def delete(self):
        # TODO: 
        import sqlite3
        with sqlite3.connect(r"epfl.db") as conn:
            try:
                conn=sqlite3.connect(r"epfl.db")
                cursor=conn.cursor()
                cursor.execute (f"delete from product where name='{self.nameStr.get()}'")
                cursor.execute("commit")
                cursor.close()
                self.onLoad() 
            except Exception as ex:
                print(ex)
          
    def onSelect(self, evt):
        # TODO: 
        theListBox = evt.widget # not needed if you have a reference to the listB object
        try:
            index = int(theListBox.curselection()[0])
            # or index = int(self.listB.curselection()[0])
        except:
            return
        
        val = theListBox.get(index)
        import re
        n,p,q=re.split(r"\s*\*\s*", val)
       
        self.priceFloat.set(float(p))
        self.qtyInt.set(int(q))
        self.nameStr.set(n)
        
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
        self.listB.delete(0,tk.END)
        self.counterInt.set(self.countRows())
        import sqlite3
        with sqlite3.connect(r"epfl.db") as conn:
            try:
                cursor=conn.cursor()
                cursor.execute ("SELECT * FROM product")
                while True:
                    row = cursor.fetchone()
                    if row == None: break
                    self.listB.insert(tk.END, f"{row[0]:20s} * {row[1]:10.2f} * {row[2]:5}")
                cursor.close()
            except Exception as ex:
                print(ex)
      
    def about(self): 
        mb.showinfo("A tkinter example", "Version 1.0")       
               
if __name__== "__main__":
    win=MyWindow()
    tk.mainloop()