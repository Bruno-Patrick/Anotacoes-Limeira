from abstratas.conta import Conta


class Investimento(Conta):
    def __init__(self, n, cli, sal, lim):
        super().__init__(n, cli, sal, lim)
        self._comment = "Não aguento mais"

    def atualiza(self):
        self._saldo += self._saldo*0.10
        self._saldo -= 9.99