class Banco:
    def __init__(self, numero, nome):
        self._num = numero
        self._nome = nome
        self._vetContas = []
        self._saldo_atualizacoes = 0

    def vincular_conta(self, conta):
        if len(self._vetContas) == 0:
            return self._vetContas.append(conta)
        else:
            for check in range(0,len(self._vetContas)):
                if conta == self._vetContas[check]:
                    return print(f"{conta} Já percente à esse banco!")
            return self._vetContas.append(conta)

    def total_atualizacoes(self):
        for conta in self._vetContas:
            self._saldo_atualizacoes += conta.saldo_total
        return print(f"Para {self._nome} o total provindo das atualizações é: {self._saldo_atualizacoes}")
            
    def relatorio(self):
        for dados in self._vetContas:
            dados.imprimir_transacoes()
