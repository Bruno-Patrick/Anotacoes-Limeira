import tkinter as tk

class Display:
    def __init__(self, master):
        self.display = master
        self.container = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.geometry(
            f"{self.container}x{self.alturaTotal}"
        )

        def left(event):
            self.btb['fg'] = 'pink'
        def right(event):
            self.btb['bg'] = "black"
            self.btb['fg'] = '#FCFCFC'

        self.btb = tk.Button(self.display, text="Clique aqui!")
        self.btb.bind('<Enter>', left)
        self.btb.bind('<Leave>', right)
        self.btb.focus()
        self.btb.pack(fill=tk.BOTH)

app = tk.Tk()
Display(app)
app.mainloop()