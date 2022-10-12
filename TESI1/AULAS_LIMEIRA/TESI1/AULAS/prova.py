from cgitb import text
from textwrap import fill
import tkinter as tk

class Display:
    def __init__(self, master):
        self.display = master
        self.display.geometry("300x180")
        self.display.title("Teste")

        entry = tk.Entry(width=5).grid(row=1,column=1)

        col = 0
        for i in range(7,10):
            col += 1
            button = tk.Button(self.display, text=i, width=1, height=1).grid(
                row=2,column=col
            )

        button = tk.Button(self.display, text="/", width=1, height=1).grid(
                row=2,column=4
            )

        col = 0
        for i in range(4,7):
            col += 1
            button = tk.Button(self.display, text=i, width=1, height=1).grid(
                row=3,column=col
            )

        col = 0
        for i in range(1,4):
            col += 1
            button = tk.Button(self.display, text=i, width=1, height=1).grid(
                row=4 ,column=col
            )


app = tk.Tk()
Display(app)
app.mainloop()