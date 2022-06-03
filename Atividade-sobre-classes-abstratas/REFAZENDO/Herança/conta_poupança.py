from conta import Conta

class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self._extrato._transacoes.append(f"\n-- Atualização na Conta Poupança --")
        return super().atualiza(taxa*3)