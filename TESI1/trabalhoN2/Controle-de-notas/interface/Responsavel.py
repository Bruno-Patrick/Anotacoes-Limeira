class Responsavel:
    
    __slots__ = ['_nome','_telefone','_email']
    def __init__(self, nome, telefone = None, email = None):
        self._nome = nome
        self._telefone = telefone
        self._email = email

    @property
    def nome(self):
        return self._nome
    @property
    def telefone(self):
        return self._telefone
    @property
    def email(self):
        return self._email

    @nome.setter
    def nome(self, value):
        if not value:
            raise Exception("field cannot be empty!")
        self._nome = value
    @telefone.setter
    def telefone(self, value):
        self._telefone = value
    @email.setter
    def email(self, value):
        self._email = value