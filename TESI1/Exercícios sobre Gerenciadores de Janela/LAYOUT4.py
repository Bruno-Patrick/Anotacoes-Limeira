from cmath import exp
from ctypes import sizeof
from email.utils import collapse_rfc2231_value
import tkinter as tk

class Display:
    def __init__(self, master):
        self.display = master
        self.display.geometry("300x300")
        self.display.title("Layout 01")

        l1 = tk.Label(
            text="Numero 1:"
        )
        l1.grid(column=0, row=0)

        entry1 = tk.Entry(
            width=20
        )
        entry1.grid(row=0, column=1)

        l1 = tk.Label(
            text="Numero 2:"
        )
        l1.grid(column=0, row=1)

        entry1 = tk.Entry(
            width=20
        )
        entry1.grid(row=1, column=1)

        button = tk.Button(
            text="somar>>", width=12
        )
        button.grid(row=2, column=0, columnspan=2, sticky=tk.W)

        l1 = tk.Label(
            bg="white", text="0.3", width=7
        )
        l1.grid(column=1, row=2, columnspan=2)



app = tk.Tk()
Display(app)
app.mainloop()