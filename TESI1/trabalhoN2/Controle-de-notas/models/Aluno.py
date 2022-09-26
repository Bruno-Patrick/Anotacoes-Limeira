from Disciplinas import Disciplinas
from Responsavel import Responsavel
from Notas import Notas

class Aluno:
     
    __slots__= ['_nome','_matricula','_telefone','_email','_responsavel','_notas','_disciplinas']
    def __init__(self, nome, matricula, telefone = None, email = None, responsavel = None):
        self._nome = nome
        self._matricula = matricula
        self._telefone = telefone
        self._email = email
        self._responsavel = responsavel
        self._notas = []
        self._disciplinas = []

    @property
    def nome(self):
        return self._nome
    @property
    def matricula(self):
        return self._matricula
    @property
    def telefone(self):
        return self._telefone
    @property
    def email(self):
        return self._email
    @property
    def responsavel(self):
        return self._responsavel
    @property
    def notas(self):
        return self._notas
    @property
    def disciplinas(self):
        return self._disciplinas

    @nome.setter
    def nome(self, value):
        if not value:
            raise Exception("field nome cannot be empty!")
        self._nome = value
    @matricula.setter
    def matricula(self, value):
        if not value:
            raise Exception("field matricula cannot be empty!")
        self._matricula = value
    @telefone.setter
    def telefone(self, value):
        self._telefone = value
    @email.setter
    def email(self, value):
        self._email = value
    @responsavel.setter
    def responsavel(self, value):
        if isinstance(value, Responsavel):
            self._responsavel = value
            
    def add_notas(self, value, key = None):
        if isinstance(value, Notas):
            if key == 'del':
                for data in self.notas:
                    if (data.disciplina == value.disciplina) and (data.nota == value.nota) and (data.aluno == value.aluno):
                        self.notas.remove(data)
            else:
                self.notas.append(value)

    def add_disciplina(self, value, key = None):
        if isinstance(value, Disciplinas):
            if key == 'del':
                for data in self.disciplinas:
                    if (data.codigo == value.codigo):
                        self.disciplinas.remove(data)
            else:
                self.disciplinas.append(value)
