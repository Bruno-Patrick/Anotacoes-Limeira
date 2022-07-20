from conta import Conta
from taxaMixIn import taxaMixIn
from historico import Historico


class ContaCorrente(Conta, taxaMixIn):

    def __init__(self, n, cli, sal):
        super().__init__(n, cli, sal)
        self._extrato = Historico()
        self._taxa = 2

    def __str__(self):
        super().__str__

    @property
    def taxa(self):
        return self._taxa
    @taxa.setter
    def taxa(self, valor):
        self._taxa = valor

    def valor_imposto(self, taxa):
        taxa = taxa/100
        valor = self._saldo*taxa
        return valor

    def taxa_decimal(self, taxa):
        taxa = taxa/100
        return taxa

    def atualiza(self, taxa):
        valor = self.valor_imposto(self.taxa_decimal(taxa)*self.taxa_decimal(self.taxa))
        self._extrato._transacoes.append(f"\nAtualização_na_Conta() =>")
        self.depositar(valor)
        self.sacar(0.1)
        self._extrato._transacoes.append(f"\n<= Fim_da_Atualização")
        return valor