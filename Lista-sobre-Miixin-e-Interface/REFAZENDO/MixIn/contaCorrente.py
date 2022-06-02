from conta import Conta
from tributavelMixIn import TributavelMixin


class ContaCorrente(Conta, TributavelMixin):
    def atualiza(self, taxa):
        self._extrato._transacoes.append(f"\n#< Atualização na Conta há {taxa}% #>")
        taxa = taxa/100
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor

    def valor_imposto(self):
        imposto = self.saldo * 0.02
        self._extrato._transacoes.append(f"\n#< Cálculo de Imposto #>")
        self.sacar(imposto)
        return imposto