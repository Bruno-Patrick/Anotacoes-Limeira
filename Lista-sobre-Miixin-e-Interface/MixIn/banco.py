class Banco:
    def __init__(self, numero, nome):
        self._num = numero
        self._nome = nome
        self._contas = []
        self._caixa_geral = 0

    @property
    def caixa_geral(self):
        self._caixa_geral = 0
        for tr in self._contas:
            self._caixa_geral += tr._saldo
        return print(f"Caixa geral do {self._nome} R${self._caixa_geral}")

    def vincular_conta(self, conta):
        self._contas.append(conta)

    @property
    def contas(self):
        return self._contas