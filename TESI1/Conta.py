import abc
from Banco import Banco

class Conta(abc.ABC):
    __slots__ = ["__numero", "__cliente", "__saldo", "__active", "__extrato"]
    def __init__(self, n, cli, sal):
        self.__numero = n
        self.__cliente = cli
        self.__saldo = sal
        self.__active = True
        self.__extrato = []
        self.__juros = 1.5
        self.__desconto = 0.20

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    @property
    def active(self):
        return self.__active
    def change_active(self):
        if (self.__active):
            if self.__saldo == 0:
                self.__active = False
                self.__extrato.append(f"Conta {self.__numero} foi encerrada")
            else:
                return (print(f"A conta não pode ter saldo positivo para encerrá-la"))
        else:
            self.__extrato.append(f"Conta {self.__numero} foi reaberta")
            self.__active = True

    @abc.abstractmethod
    def sacar(self, value):
        pass

    @abc.abstractmethod
    def depositar(self, value):
        pass

    @abc.abstractmethod
    def atualiza(self):
        pass
