class Professor:

    __slots__ = ['_id','_nome']
    def __init__(self, nome):
        self._id = None
        self._nome = nome

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        if not value:
            raise Exception("Field name cannot be empty!")
        self._id = value

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        if not value:
            raise Exception("Field name cannot be empty!")
        self._nome = value