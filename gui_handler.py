from tkinter import *
from tkinter import ttk


class App:
    
    root,label,frame,hash_button,hash_type = None,None,None,None,None
    
    hash_types = ('sha1','sha224','sha256','sha384','sha512'
                 ,'sha_224','sha_256','sha3_384','sha3_512',
                 'shake_128','shake_256','blake2b','blake2s','md5')
    
    # populate window intentionally mangled to make it private and to discourage calls from outside of class.
    @staticmethod
    def __populate_window():
        App.label = Label(App.root, text="Hello World")
        App.label.pack()
        App.hash_button = Button(App.root,text="HASH",width=50)
        App.hash_button.pack()
        App.hash_type = ttk.Combobox(App.root, values= App.hash_types)
        App.hash_type.state(["readonly"])
        App.hash_type.pack()       
        
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