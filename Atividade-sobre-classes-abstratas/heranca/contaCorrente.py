from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, n, cli, sal, lim):
        super().__init__(n, cli, sal, lim)
        self._transacoes = []
        self._saldo_total = 0


    def atualiza(self, taxa):
        super().atualiza(taxa*2)
        self._saldo_total += self._saldo

    def deposita(self, valor):
        super().deposita(valor)
        super().sacar(0.10)
        print("\n IMPORTANTE! A taxa de depósito é de 10 centavos.")

    def imprimir_transacoes(self):
        print("#-----------------------------------#")
        print(f"CONTA CORRENTE")
        return super().imprimir_transacoes()