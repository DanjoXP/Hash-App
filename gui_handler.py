from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class App:
    
    root = None
    label = None
    frame = None
    create_hash_button = None
    view_hash_button = None
    hash_type = None
    hash_header = None
    hash_frame = None
    button_frame = None
    browse_frame = None
    browse_button = None
    browse_textbox = None
    
    hash_types = ('sha1','sha224','sha256','sha384','sha512'
                 ,'sha3_224','sha3_256','sha3_384','sha3_512',
                 'shake_128','shake_256','blake2b','blake2s','md5')
    
    # populate window intentionally mangled to make it private and to discourage calls from outside of class.
    @staticmethod
    def __populate_window():
        App.label = Label(App.root, text='Hash Application v1')
        App.label.pack() 
       
        App.button_frame = Frame(App.root)
        App.create_hash_button = Button(App.button_frame,text='Create Hash',width=25,command=App.__create_hash)
        App.view_hash_button = Button(App.button_frame,text='View Hash',width=25,command=App.__view_hash)
        App.create_hash_button.pack(side=LEFT,padx=5)
       
        App.view_hash_button.pack(side=LEFT,padx=5)
        App.button_frame.pack(side=BOTTOM,pady=20)
        
        App.hash_frame = Frame(App.root)
        App.hash_frame.pack(anchor='w',pady=10,padx=10)
        
        App.hash_header = Label(App.hash_frame,text='Hash Algorithm -')
        App.hash_type = ttk.Combobox(App.hash_frame, values= App.hash_types)
        App.hash_type.current(2)
        App.hash_type.state(['readonly'])
        
        App.browse_frame = Frame(App.root)
        App.browse_textbox = Entry(App.browse_frame,width=60,)
        App.browse_textbox.config(state='readonly')
        App.browse_textbox.pack(side=LEFT)
        App.browse_button = Button(App.browse_frame, text='Browse...',width=10,command=App.__browse)
        App.browse_button.pack(side=RIGHT)
        App.browse_frame.pack(side=LEFT,pady=20,padx=10)
        
        App.hash_header.pack(side=LEFT)
        App.hash_type.pack(side=LEFT)     
        
    @staticmethod
    def create_window(X,Y,TITLE):
       if App.root is None:
           App.root = Tk()
           App.root.title(TITLE)
           App.root.geometry(f'{X}x{Y}')
           App.root.minsize(X,Y)
           App.root.maxsize(X*2,Y*2)
           App.__populate_window()
       else:
           print('App Already Created!')
    
    @staticmethod 
    def open_window():
        App.root.mainloop()
        
    @staticmethod
    def __create_hash():
        pass
        
    @staticmethod
    def __view_hash():
        pass
    
    @staticmethod
    def __browse():
        file_selected = filedialog.askopenfilename()
        
        if file_selected:
            App.browse_textbox.config(state='normal')
            App.browse_textbox.delete(0,END)
            App.browse_textbox.insert(0,file_selected)
            App.browse_textbox.config(state='readonly')