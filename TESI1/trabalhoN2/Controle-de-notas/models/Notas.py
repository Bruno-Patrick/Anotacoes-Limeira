class Notas:

    __slots__ = ['_disciplina','_nota','_aluno']
    def __init__(self, disciplina, nota, aluno):
        self._disciplina = disciplina
        self._nota = nota
        self._aluno = aluno

    @property
    def disciplina(self):
        return self._disciplina
    @property
    def nota(self):
        return self._nota
    @property
    def aluno(self):
        return self._aluno

    @disciplina.setter
    def disciplina(self, value):
        self._disciplina = value
    @nota.setter
    def nota(self, value):
        self._nota = value
    @aluno.setter
    def aluno(self, value):
        self._aluno = value