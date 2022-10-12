import tkinter as tk

class Display:
    def __init__(self, master):
        self.display = master
        self.container = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.geometry(
            f"{self.container}x{self.alturaTotal}"
        )

        def clicou(event):
            print(event)
            if event.keysym == "space":
                self.lbl = tk.Label(self.display, text=f" ", font=("Arial","14","bold"))
                self.lbl.pack(side=tk.LEFT)
            else:
                self.lbl = tk.Label(self.display, text=f"{event.keysym}", font=("Arial","14","bold"))
                self.lbl.pack(side=tk.LEFT)

        self.btb = tk.Button(self.display, text="Clique aqui!", bg="gray")
        #Button-3 é o botão direito do mouse
        self.btb.bind('<Button-1>', clicou, add='+')
        #Button-2 é o botão esquerdo do mouse
        self.btb.bind('<Button-2>', clicou, add='+')
        #À partir do segundo evento, adiciona-se o parâmetro
        # |_ add='+'
        self.btb.bind('<Any-KeyPress>', clicou, add='+')
        #Button-3 é o botão do meio do mouse
        self.btb.bind('<Button-3>', clicou)
        #Scroll lock para cima
        self.btb.bind('<Button-4>', clicou, add='+')
        #Return é o enter
        self.display.bind('<Button-1>', clicou)
        self.display.focus()
        self.btb.focus()
        self.btb.pack(fill=tk.BOTH)

app = tk.Tk()
Display(app)
app.mainloop()