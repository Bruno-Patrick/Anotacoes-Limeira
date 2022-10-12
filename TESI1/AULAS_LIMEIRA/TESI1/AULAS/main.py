from struct import pack
import tkinter as tk

class Tela:

    def __init__(self, master):
        self.display = master
        self.display.title('Lula')
        self.display.minsize(400,200)
        self.lbl_name = tk.Label(self.display
        ,text='User name:'

        ,font=('abel',10,'bold')
        ).pack()

        self.ent_name = tk.Entry(
            self.display ,width=15
        ).pack()

        self.lbl_password = tk.Label(self.display
            ,text='Password'
            ,font=('abel',10,'bold')

        ).pack()
        self.ent_senha = tk.Entry(self.display
            ,show='*'
        ).pack()

        self.btn_login = tk.Button(self.display
        ,text='(m)amar'
        ,command=self.display.destroy
        ).pack()


app = tk.Tk()
Tela(app)
app.mainloop()