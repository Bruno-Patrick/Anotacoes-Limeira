class Historico:
    def __init__(self):
        self._transacoes = []

    def imprime(self):
        print("| =========== |")
        for mov in self._transacoes:
            print(mov)
