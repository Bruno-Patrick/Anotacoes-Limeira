class Professor:

    __slots__ = ['_nome']
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        if not value:
            raise Exception("Field name cannot be empty!")
        self._nome = value