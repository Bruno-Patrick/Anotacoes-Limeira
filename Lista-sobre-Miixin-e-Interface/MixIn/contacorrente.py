from conta import Conta
from tributavelMixIn import TributavelMixIn


class ContaCorrente(Conta, TributavelMixIn):

    def __init__(self, n, cli, sal):
        super().__init__(n, cli, sal)
        self._taxa = 2

    def __str__(self):
        super().__str__

    @property
    def taxa(self):
        return self._taxa
    @taxa.setter
    def taxa(self, valor):
        self._taxa = valor

    def atualiza(self, taxa):
        valor = super().valor_imposto(taxa*self._taxa)
        self._extrato._transacoes.append(f"\nAtualização_na_Conta() =>")
        self.depositar(valor)
        self.sacar(0.1)
        self._extrato._transacoes.append(f"\n<= Fim_da_Atualização")
        return valor