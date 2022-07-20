from conta import Conta

class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self._extrato._transacoes.append(f"\n-- Atualização na Conta Poupança --")
        valor = self._saldo*(taxa/100)
        self.sacar(valor)
