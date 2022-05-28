import abc
from historico import Historico

class Conta(abc.ABC):
    def __init__(self, n, cli, sal):
        self._numero = n
        self._titular = cli
        self._saldo = sal
        self._extrato = Historico()

    def __str__(self):
        return f"Conta N°: {self._numero} | Titular: {self._titular}"

    @property
    def extrato(self):
        return self._extrato

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

    def depositar(self, valor):
        self._saldo += valor
        self._extrato._transacoes.append(f"\nDepósito de R${valor}")

    def sacar(self, valor):
        self._saldo -= valor
        self._extrato._transacoes.append(f"\nSaque de R${valor}")