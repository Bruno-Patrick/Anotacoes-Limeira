from conta import Conta

class ContaInvestimento(Conta):
    def atualiza(self):
        self._extrato._transacoes.append(f"\n-- Atualização na Conta Investimento --")
        valor = self._saldo*0.10
        self.depositar(valor)
        self.sacar(9.99)
