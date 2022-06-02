from manipulador_de_tributaveis import ManipuladorDeTributaveis


class Banco:
    def __init__(self, numero, nome):
        self._num = numero
        self._nome = nome
        self._contas = []
        self._caixa_geral = 0
        self._impostos = ManipuladorDeTributaveis()

    def vincular_conta(self, conta):
        return self._contas.append(conta)

    @property
    def impostos(self):
        print(f"\n{self._nome}")
        return self._impostos.calcular_impostos(self._contas)

    @property
    def caixa_geral(self):
        self._caixa_geral = 0
        for contas in self._contas:
            self._caixa_geral += contas.saldo
        return print(f"Caixa geral do {self._nome}: R${self._caixa_geral:,.2f}")