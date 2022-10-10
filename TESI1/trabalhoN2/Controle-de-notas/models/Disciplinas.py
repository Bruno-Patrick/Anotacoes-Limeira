class Disciplinas:

    __slots__ = ["_id","_nome", "_ano","_semestre", "_professor","_codigo"]
    def __init__(self, nome, ano, semestre, professor, codigo):
        self._id = None
        self._nome = nome
        self._ano = ano
        self._semestre = semestre
        self._professor = professor
        self._codigo = codigo

    @property
    def id(self):
        return self._id
    @property
    def nome(self):
        return self._nome
    @property
    def ano(self):
        return self._ano
    @property
    def professor(self):
        return self._professor
    @property
    def codigo(self):
        return self._codigo


    @id.setter
    def id(self, value):
        if not value:
            raise Exception("field cannot be empty!")
        self._id = value
    @nome.setter
    def nome(self, value):
        if not value:
            raise Exception("field cannot be empty!")
        self._nome = value
    @ano.setter
    def ano(self, value):
        if not value:
            raise Exception("field cannot be empty!")
        self._ano = value
    @professor.setter
    def professor(self, value):
        if not value:
            raise Exception("field cannot be empty!")
        self._professor = value
    @codigo.setter
    def codigo(self, value):
        if not value:
            raise Exception("field cannot be empty!")
        self._codigo = value