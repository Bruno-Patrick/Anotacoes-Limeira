from conta import Conta

class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._extrato._transacoes.append(f"\n-- Atualização na Conta Corrente --")
        return super().atualiza(taxa*2)

    def depositar(self, valor):
        super().depositar(valor)
        super().sacar(0.10)