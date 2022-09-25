import tkinter as tk
from tkinter import ttk
from Login import Login

class Display:

    def __init__(self, master):
        self.display = master
        self.larguraTotal = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.geometry("{0}x{1}+0+0".format(self.larguraTotal, self.alturaTotal))
        self.display.title("Controle de Notas Acadêmico")
        self.userSession = Login()



app = tk.Tk()
Display(app)
app.mainloop()