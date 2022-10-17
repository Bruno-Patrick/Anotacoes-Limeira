from operator import truediv
import tkinter as tk
from tkinter import ttk, messagebox as msg

"""
Classe destinada ao fornecimento de funções
que serão usadas muitas vezes na aplicação
"""
class Functions:
    """
    Verifica se algum Entry está vazio
    """
    def isFieldsEmpty(self, *args):
        for field in args:
            if not field.get():
                return True
        return False