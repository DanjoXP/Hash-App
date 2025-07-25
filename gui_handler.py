from tkinter import *
from tkinter import ttk


class App:
    
    root,label,frame,hash_button = None,None,None,None
    
    def __populate_window():
        App.label = Label(App.root, text="Hello World")
        App.label.pack()
        App.hash_button = Button(App.root,text="HASH",width=50)
        App.hash_button.pack()
                
        
        
    @staticmethod
    def create_window(X,Y,TITLE):
       if App.root is None:
           App.root = Tk()
           App.root.title(TITLE)
           App.root.geometry(f"{X}x{Y}")
           App.__populate_window()
       else:
           print("App Already Created!")
    
    @staticmethod 
    def open_window():
        App.root.mainloop()