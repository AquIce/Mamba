import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os

username = os.environ.get('USERNAME')
filename = ''

root = tk.Tk()
root.title('Mamba Interpreter')
root.resizable(False, False)
root.geometry('300x150')
root.iconphoto(False, tk.PhotoImage(file='mamba.png'))

root.bg, root.fg, root.ac1, root.ac2 = ('#282828', 'white', '#404040y', '#B3B3B3')

def select_file():
    filetypes = (
        ('Python files', '*.py'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Choose file to compile',
        initialdir='C:/Users/'+username+'/Desktop',
        filetypes=filetypes
    )

    showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = ttk.Button(
    root,
    text='Choose File',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()