from tkinter import *
from tkinter import filedialog, messagebox, ttk

from hasher import Hasher


class App:
    # GUI components
    root = None
    label = None
    frame = None
    create_hash_button = None
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

    hash_code = None
    hash_types = (
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
        "sha3_224",
        "sha3_256",
        "sha3_384",
        "sha3_512",
        "shake_128",
        "shake_256",
        "blake2b",
        "blake2s",
        "md5",
    )

    # populate window intentionally mangled to make it private and to discourage calls from outside of class.
    @staticmethod
    def __populate_window():
        App.label = Label(App.root, text="Hash Application v1")
        App.label.pack()

        App.button_frame = Frame(App.root)
        App.create_hash_button = Button(
            App.button_frame, text="Create Hash", width=25, command=App.__create_hash
        )
        App.save_hash_button = Button(
            App.button_frame, text="Save Hash", width=25, command=App.__save_hash
        )
        App.create_hash_button.pack(side=LEFT, padx=5)

        App.save_hash_button.pack(side=LEFT, padx=5)
        App.button_frame.pack(side=BOTTOM, pady=20)

        App.hash_frame = Frame(App.root)
        App.hash_frame.pack(anchor="w", pady=10, padx=10)

        App.hash_header = Label(App.hash_frame, text="Hash Algorithm -")
        App.hash_type = ttk.Combobox(App.hash_frame, values=App.hash_types)
        App.hash_type.current(2)
        App.hash_type.state(["readonly"])

        App.browse_frame = Frame(App.root)
        App.browse_textbox = Entry(App.browse_frame, width=60)
        App.browse_textbox.config(state="readonly")
        App.browse_textbox.pack(side=LEFT)
        App.browse_button = Button(
            App.browse_frame, text="Browse...", width=10, command=App.__browse
        )
        App.browse_button.pack(side=RIGHT)
        App.browse_frame.pack(anchor="w", pady=0, padx=10)

        App.result_frame = Frame(App.root)
        App.result_label = Label(App.result_frame, text="Hash Result -")
        App.result_textbox = Entry(App.result_frame, width=45)
        App.copy_button = Button(
            App.result_frame, text="Copy Hash", width=10, command=App.__copy_hash
        )
        App.copy_button.pack(side=RIGHT)
        App.result_textbox.config(state="readonly")
        App.result_label.pack(side=LEFT, pady=10, padx=10)
        App.result_textbox.pack(side=LEFT)
        App.result_frame.pack(anchor="w")

        App.hash_header.pack(side=LEFT)
        App.hash_type.pack(side=LEFT)

    @staticmethod
    def create_window(X, Y, TITLE):
        if App.root is None:
            App.root = Tk()
            App.root.title(TITLE)
            App.root.geometry(f"{X}x{Y}")
            App.root.minsize(X, Y)
            App.root.maxsize(X * 2, Y * 2)
            App.__populate_window()
        else:
            print("App Already Created!")

    @staticmethod
    def open_window():
        App.root.mainloop()

    @staticmethod
    def __create_hash():
        App.hash_code = Hasher.create_hash(
            App.hash_type.get(), App.browse_textbox.get()
        )
        App.result_textbox.config(state="normal")
        App.result_textbox.delete(0, END)
        App.result_textbox.insert(0, App.hash_code)
        App.result_textbox.config(state="readonly")

    @staticmethod
    def __save_hash():
        if App.hash_code is None:
            messagebox.showwarning("Warning", "No Hash Generated To Save")
            print("No Hash Generated To Save")
            return
        try:
            Hasher.save_file(
                App.hash_type.get(), App.browse_textbox.get(), App.hash_code
            )
            messagebox.showinfo("Success", "Hash saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save hash:\n{e}")

    @staticmethod
    def __copy_hash():
        App.root.clipboard_clear()
        App.root.clipboard_append(App.result_textbox.get())
        pass

    @staticmethod
    def __browse():
        file_selected = filedialog.askopenfilename()

        if file_selected:
            App.hash_code = None
            App.result_textbox.config(state="normal")
            App.result_textbox.delete(0, END)
            App.result_textbox.config(state="readonly")
            App.browse_textbox.config(state="normal")
            App.browse_textbox.delete(0, END)
            App.browse_textbox.insert(0, file_selected)
            App.browse_textbox.config(state="readonly")
