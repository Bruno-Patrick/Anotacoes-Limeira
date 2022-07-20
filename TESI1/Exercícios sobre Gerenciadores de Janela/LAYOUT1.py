from cmath import exp
import tkinter as tk

class Display:
    def __init__(self, master):
        self.display = master
        self.display.geometry("300x180")
        self.display.title("Layout 01")

        top = tk.Label(
            self.display, text="TOPO", bg="yellow", height=5, width=42
        )
        top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        footer = tk.Label(
            self.display, text="RODAPÉ", bg="#00ffff", height=5, width=42
        )
        footer.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        midLeft = tk.Label(
            self.display, bg="red", text="ESQUERDA", height=1, width=22
        )
        midLeft.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        midRight = tk.Label(
            self.display, bg="green", text="DIREITA", height=1, width=22
        )
        midRight.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)



app = tk.Tk()
Display(app)
app.mainloop()