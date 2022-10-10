class Notas:

    __slots__ = ['_id','_disciplina','_nota','_aluno']
    def __init__(self, disciplina, nota, aluno):
        self._id = None
        self._disciplina = disciplina
        self._nota = nota
        self._aluno = aluno

    @property
    def id(self):
        return self._id
    @property
    def disciplina(self):
        return self._disciplina
    @property
    def nota(self):
        return self._nota
    @property
    def aluno(self):
        return self._aluno

    @id.setter
    def id(self, value):
        self._id = value
    @disciplina.setter
    def disciplina(self, value):
        self._disciplina = value
    @nota.setter
    def nota(self, value):
        self._nota = value
    @aluno.setter
    def aluno(self, value):
        self._aluno = value