import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as ms
from tkinter.scrolledtext import ScrolledText

class Display:
    def __init__(self, master):
        self.display = master
        self.container = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.geometry(
            f"{self.container}x{self.alturaTotal}"
        )


        def mostrar_arquivo():
            nome = fd.askopenfilename()()
            ms.showinfo('Aviso',f'{nome}')


        def carregar_arquivo():
            filetypes = (('Texto', '*.txt'),('Python','*.py'))     
            arquivo = fd.askopenfile(initialdir='/home/bruno.patrick/Área de Trabalho/AULAS_LIMEIRA', filetypes=filetypes)
            with open(arquivo.name, 'r') as archive:
                leitura = archive.readlines()
                for i in leitura:
                    self.sct.insert(tk.END, i)

        def salvar_arquivo():
            arquivo = fd.asksaveasfile()
            with open(arquivo.name, 'w') as arq:
                arq.write(sct.get('1.0',tk.END))
            

        self.btn = tk.Button(self.display, text="Mostrar Arquivo", command=mostrar_arquivo)
        self.btn.pack()
        self.btn1 = tk.Button(self.display, text="Carregar Arquivo", command=carregar_arquivo)
        self.btn1.pack()
        self.btn1 = tk.Button(self.display, text="Salvar Arquivo", command=salvar_arquivo)
        self.btn1.pack()
        self.sct = ScrolledText(self.display, height=10)
        self.sct.pack()


app = tk.Tk()
Display(app)
app.mainloop()        