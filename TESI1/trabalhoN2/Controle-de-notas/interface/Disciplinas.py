class Disciplinas:

    __slots__ = ["_nome", "_ano", "_professor"]
    def __init__(self, nome, ano, professor):
        self._nome = nome
        self._ano = ano
        self._professor = professor

    @property
    def nome(self):
        return self._nome
    @property
    def ano(self):
        return self._ano
    @property
    def professor(self):
        return self._professor

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