import tkinter as tk
from tkinter import ttk


class Display:
    def __init__(self, master):
        self.display = master
        # self.display.attributes("-fullscreen", True)
        self.display.title('Banco do Brasil')
        self.container = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.geometry("{0}x{1}+0+0".format(self.container, self.alturaTotal))

        self.logo = tk.Label(self.display, bg="yellow", text="Banco do Brasil",
            height=5)
        self.logo.pack(side=tk.TOP, fill=tk.X, expand=True)


app = tk.Tk()
Display(app)
app.mainloop()