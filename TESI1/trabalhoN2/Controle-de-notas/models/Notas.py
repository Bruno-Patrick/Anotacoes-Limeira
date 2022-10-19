class Notas:

    """
        #Identificadores:
            #Observações: x é uma variável
            atvN1.x = atividade parcial da N1 Nº x,
            atvN2.x = atividade parcial da N2 Nº x,
            N1 = Nota da N1,
            N2 = Nota da N2,
            media final = Nota da media final,
            situacao = Situação final do aluno

    """
    __slots__ = ['_id','_disciplina','_aluno','_nota','_identificador']
    def __init__(self, disciplina, nota, aluno, identificador):
        self._id = None
        self._disciplina = disciplina
        self._aluno = aluno
        self._nota = nota
        self._identificador = identificador

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
    @property
    def identificador(self):
        return self._identificador

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
    @identificador.setter
    def identificador(self, value):
        self._identificador = value