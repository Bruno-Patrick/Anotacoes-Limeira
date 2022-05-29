class Historico():
    def __init__(self):
        self._transacoes = []

    def imprime(self):
        for movimentacoes in self._transacoes:
            print(movimentacoes)
            print("-------------------")