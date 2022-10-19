class Configurations:

    __slots__ = ['_atvAmountPartialN1','_atvAmountPartialN2', "_disciplina"]
    def __init__(self, parcialN1, parcialN2, disciplinaID):
        self._atvAmountPartialN1 = parcialN1
        self._atvAmountPartialN2 = parcialN2
        self._disciplina = disciplinaID

    @property
    def usuario(self):
        return self._disciplina

    @property
    def atvAmountPartialN1(self):
        return self._atvAmountPartialN1

    @property
    def atvAmountPartialN2(self):
        return self._atvAmountPartialN2

    @atvAmountPartialN1.setter
    def atvAmountPartialN1(self, value):
        self._atvAmountPartialN1 = value

    @atvAmountPartialN2.setter
    def atvAmountPartialN2(self, value):
        self._atvAmountPartialN2 = value