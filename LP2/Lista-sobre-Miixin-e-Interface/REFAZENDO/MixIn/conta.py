import abc
from historico import Historico


class Conta(abc.ABC):
    def __init__(self, n, cli, sal):
        self._numero = n
        self._titular = cli
        self._saldo = sal
        self._extrato = Historico()

    def __str__(self):
        return f"Conta Nº {self._numero} | TITULAR: {self._titular}"
    
    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

    def depositar(self, valor):
        self._saldo += valor
        self._extrato._transacoes.append(f"\nConta Nº {self._numero} | TITULAR: {self._titular}")
        self._extrato._transacoes.append(f"\nDepósito de {valor:,.2f}")

    def sacar(self, valor):
        self._saldo -= valor
        self._extrato._transacoes.append(f"\nConta Nº {self._numero} | TITULAR: {self._titular}")
        self._extrato._transacoes.append(f"\nSaque de {valor:,.2f}")        

    @property
    def saldo(self):
        return self._saldo

    @property
    def extrato(self):
        return self._extrato.imprime()