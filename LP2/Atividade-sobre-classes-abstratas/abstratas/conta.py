import abc

class Conta(abc.ABC):
    def __init__(self, n, cli, sal, lim):
        self._numero = n
        self._titular = cli
        self._saldo = sal
        self._limite = lim

    @abc.abstractmethod
    def atualiza(self):
        pass