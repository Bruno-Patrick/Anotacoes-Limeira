import tkinter as tk
from tkinter import ttk
import functions

class Display:
    def __init__(self, master):
        self.display = master
        self.display.minsize(500,500)

        def generate_columns(*args):
            columns = [x for x in args]
            return columns

        self.colunas_aluno = generate_columns('nome','turmas','atv1')
        self.tvw = ttk.Treeview(self.display, columns=self.colunas_aluno, show='headings')
        self.tvw.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for column in self.colunas_aluno:
            self.tvw.heading(column, text=f"{column}")
            del(self.tvw.heading(column, text=f"{column}"))

        for column in range(0, len(self.colunas_aluno)):
            self.tvw.column(column=[column], minwidth=40)
            del(self.tvw.column(column=[column], minwidth=40))

        

app = tk.Tk()
Display(app)
app.mainloop()