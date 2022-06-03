class Banco:
    def __init__(self, numero, nome):
        self._num = numero
        self._nome = nome
        self._vetContas = []
        self._saldo_total = 0

    def __str__ (self):
        return f"Banco {self._nome}"

    def vincular_conta(self, conta):
        self._vetContas.append(conta)

    def extrato_geral(self):
        self._saldo_total = 0
        for mov in self._vetContas:
            print(mov.extrato)
            self._saldo_total += mov.saldo
        print(f"Total de atualizações do banco {self._nome}: R${self._saldo_total:,.2f}")