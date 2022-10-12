import tkinter as tk

class Frame:
    def __init__(self, master):
        self.display = master
        self.display.title("Exemplo com frames")
        self.display.geometry("300x300")

        frm1 = tk.Frame(self.display)
        frm1.pack()
        frm2 = tk.Frame(self.display)
        frm2.pack()

        btn1 = tk.Button(frm1, text='Adicionar')
        btn1.pack(side=tk.LEFT)

        btn2 = tk.Button(frm1, text='Editar')
        btn2.pack(side=tk.LEFT)

        btn3 = tk.Button(frm1, text='Remover')
        btn3.pack(side=tk.LEFT)

        btn4 = tk.Button(frm2, text='Salvar')
        btn4.pack(side=tk.BOTTOM)

        btn5 = tk.Button(frm2, text='Fechar')
        btn5.pack(side=tk.BOTTOM)

        btn6 = tk.Button(frm2, text='Listar')
        btn6.pack(side=tk.BOTTOM)

class LabelFrame:
    def __init__(self, master):
        self.display = master
        self.display.title("Exemplo com LabelFrame")
        self.display.geometry("300x300")

        lfr = tk.LabelFrame(self.display,text='Alinhamento')
        lfr.pack()

        rbt1 = tk.Radiobutton(lfr, text='LEFT')
        rbt1.pack(side=tk.LEFT)

        rbt2 = tk.Radiobutton(lfr, text='CENTER')
        rbt2.pack(side=tk.LEFT)

        rbt3 = tk.Radiobutton(lfr, text='RIGHT')
        rbt3.pack(side=tk.LEFT)

class TopLevel:
    def toplevel(self):
        self.secundaryDisplay = tk.Toplevel()
        self.secundaryDisplay.title("Janela Secundária - Toplevel")
        self.secundaryDisplay.geometry('400x400')
        self.btn2 = tk.Button(
            self.secundaryDisplay,text='Voltar', command=self.fechar_toplevel)
        self.btn2.pack()
        self.principal_display.iconify()

    def fechar_toplevel(self):
        self.principal_display.grab_set()
        self.secundaryDisplay.destroy()
        self.principal_display.deiconify()

    def __init__(self, master):
        self.principal_display = master
        self.principal_display.title("Janela Toplevel")
        self.principal_display.geometry("300x300")

        btn = tk.Button(self.principal_display, text='toplevel', command=self.toplevel)
        btn.pack()

        


app = tk.Tk()
TopLevel(app)
app.mainloop()
