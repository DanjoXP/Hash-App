from tkinter import *
from tkinter import ttk, filedialog, messagebox,simpledialog
from hasher import Hasher
import os

class App:
    # GUI components
    root = None
    label = None
    frame = None
    save_hash_button = None
    hash_type = None
    hash_header = None
    hash_frame = None
    button_frame = None
    browse_frame = None
    browse_button = None
    browse_textbox = None
    result_frame = None
    copy_button = None
    result_label = None
    result_textbox = None
    compare_hash_button = None
    file_name = None
    
    hash_code = None
    hash_types = (
        'sha1','sha224','sha256','sha384','sha512',
        'sha3_224','sha3_256','sha3_384','sha3_512',
        'shake_128','shake_256','blake2b','blake2s','md5'
    )
    
    # Populates window with UI elements
    @staticmethod
    def __populate_window():
        App.label = Label(App.root, text='Hash Application v1')
        App.label.pack() 
       
        App.button_frame = Frame(App.root)
        App.get_hash_button = Button(App.button_frame,text='Get Hash',width=15,command=App.__get_hash)
        App.save_hash_button = Button(App.button_frame,text='Save Hash',width=15,command=App.__save_hash)
        App.compare_hash_button = Button(App.button_frame,text='Compare Hash',width=15,command=App.__compare_hash)
        
        App.get_hash_button.pack(side=LEFT,padx=5)
        App.compare_hash_button.pack(side=LEFT, padx=5)
        App.save_hash_button.pack(side=LEFT,padx=5)
        App.button_frame.pack(side=BOTTOM,pady=20)
        
        App.hash_frame = Frame(App.root)
        App.hash_frame.pack(anchor='w',pady=10,padx=10)
        
        App.hash_header = Label(App.hash_frame,text='Hash Algorithm -')
        App.hash_type = ttk.Combobox(App.hash_frame, values= App.hash_types)
        App.hash_type.current(2)
        App.hash_type.state(['readonly'])
        
        App.browse_frame = Frame(App.root)
        App.browse_textbox = Entry(App.browse_frame,width=60)
        App.browse_textbox.config(state='readonly')
        App.browse_textbox.pack(side=LEFT)
        App.browse_button = Button(App.browse_frame, text='Browse...',width=10,command=App.__browse)
        App.browse_button.pack(side=RIGHT)
        App.browse_frame.pack(anchor='w',pady=0,padx=10)
        
        App.result_frame = Frame(App.root)
        App.result_label = Label(App.result_frame,text="Hash Result -")
        App.result_textbox = Entry(App.result_frame,width=45)
        App.copy_button = Button(App.result_frame, text="Copy Hash",width=10,command=App.__copy_hash)
        App.copy_button.pack(side=RIGHT)
        App.result_textbox.config(state="readonly")
        App.result_label.pack(side=LEFT,pady=10,padx=10)
        App.result_textbox.pack(side=LEFT)
        App.result_frame.pack(anchor='w')
        
        App.hash_header.pack(side=LEFT)
        App.hash_type.pack(side=LEFT)     
    
    # Creates Window with dimensions and title   
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
           messagebox.showerror("Error", "App Already Created")
    
    # Displays window / starts main loop   
    @staticmethod 
    def open_window():
        App.root.mainloop()
        
    @staticmethod
    def __get_hash():
        
        if App.browse_textbox.get() is None or App.browse_textbox.get().strip() == "":
            messagebox.showwarning("Warning", "Please Select A File To Hash")
            return
        
        App.hash_code = Hasher.get_hash(App.hash_type.get(), App.browse_textbox.get())
        App.result_textbox.config(state='normal')
        App.result_textbox.delete(0,END)
        App.result_textbox.insert(0,App.hash_code)
        App.result_textbox.config(state='readonly')
    
    # Opens save dialog, and displays outcome of save
    @staticmethod
    def __save_hash():
        if App.hash_code is None:
            messagebox.showwarning("Warning", "No Hash Generated To Save")
            return
        try:
            file_path = filedialog.asksaveasfilename(
                title="Save Hash Code",
                initialfile=f"{os.path.basename(App.browse_textbox.get())}.{App.hash_type.get()}",
                defaultextension= f".{App.hash_type.get()}",
                filetypes=[("All Files","*.*")]
                )
            
            if not file_path:
                return
            
            Hasher.save_file(App.hash_type.get(),file_path,App.hash_code)
            messagebox.showinfo("Success", "Hash saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save hash:\n{e}")
     
    # Copies hash to clipboard, warns if no hash generated.
    @staticmethod
    def __copy_hash():
        
        if App.result_textbox.get() is None or App.result_textbox.get().strip() == "":
            messagebox.showwarning("Warning","There Is Nothing To Copy To Clipboard!")
            return
        
        App.root.clipboard_clear()
        App.root.clipboard_append(App.result_textbox.get())
        messagebox.showinfo("Clipboard","Hash Copied To Clipboard!")
    
    # Opens file dialog, updates textbox to full path, resets related variables
    @staticmethod
    def __browse():
        file_selected = filedialog.askopenfilename()
        
        if file_selected:
            App.file_name = None
            App.hash_code = None
            App.result_textbox.config(state='normal')
            App.result_textbox.delete(0,END)
            App.result_textbox.config(state='readonly')
            App.browse_textbox.config(state='normal')
            App.browse_textbox.delete(0,END)
            App.browse_textbox.insert(0,file_selected)
            App.browse_textbox.config(state='readonly')
            App.file_name = os.path.basename(file_selected)
    
    # Compares user entered hash with generated hash, displays result.       
    @staticmethod
    def __compare_hash():
        if App.hash_code is None:
            messagebox.showwarning("Warning","No Hash Generated To Compare")
            return 
        
        code = simpledialog.askstring("Input","Enter Hash To Compare")
        
        if code is None or code.strip() == "":
            return
        
        if code.strip() == App.hash_code.strip():
            messagebox.showinfo("Result","The Hashes Match")
        else:
            messagebox.showinfo("Result","The Hashes Are Different")
        
