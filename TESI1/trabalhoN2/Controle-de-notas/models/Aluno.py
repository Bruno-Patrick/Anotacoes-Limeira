class Aluno:
     
    __slots__ = ['_id','_nome','_matricula','_telefone','_email','_responsavel']
    def __init__(self, nome, matricula, telefone = None, email = None, responsavel = None):
        self._id = None
        self._nome = nome
        self._matricula = matricula
        self._telefone = telefone
        self._email = email
        self._responsavel = responsavel

    @property
    def id(self):
        return self._id
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

    @id.setter
    def id(self, value):
        if not value:
            raise Exception("field nome cannot be empty!")
        self._id = value
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
        self._responsavel = value