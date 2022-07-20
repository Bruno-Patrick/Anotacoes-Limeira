from conta import Conta

class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._extrato._transacoes.append(f"\n-- Atualização na Conta Corrente --")
        valor = self._saldo*(taxa/100)
        self.sacar(valor)

    def depositar(self, valor):
        super().depositar(valor)
        super().sacar(0.10)