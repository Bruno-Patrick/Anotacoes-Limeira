from Disciplinas import Disciplinas

class Professor:

    __slots__ = ['_nome','_disciplina']
    def __init__(self, nome):
        self._nome = nome
        self._disciplina = []

    @property
    def nome(self):
        return self._nome
    @property
    def disciplina(self):
        return self._disciplina

    @nome.setter
    def nome(self, value):
        if not value:
            raise Exception("Field name cannot be empty!")
        self._nome = value
    

    def add_disciplina(self, *args):
        for disciplina in args:
            if isinstance(disciplina, Disciplinas):
                self._disciplina.append(disciplina)