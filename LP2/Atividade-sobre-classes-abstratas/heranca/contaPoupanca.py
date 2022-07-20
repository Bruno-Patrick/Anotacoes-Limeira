from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, n, cli, sal, lim):
        super().__init__(n, cli, sal, lim)
        self._transacoes = []
        self._saldo_total = 0

    def atualiza(self, taxa):
        super().atualiza(taxa*3)
        self._saldo_total += self._saldo


    def imprimir_transacoes(self):
        print("#-----------------------------------#")
        print(f"CONTA POUPANÇA")
        return super().imprimir_transacoes()