import abc
from datetime import datetime
from Extrato import Extrato

class Conta(abc.ABC):

    numeroDaConta = 1

    __slots__ = ["__numero", "__cliente", "__saldo",
     "__active", "__extrato", "__juros","__desconto"]
    def __init__(self, cli, sal):
        self.__numero = Conta.numeroDaConta
        Conta.numeroDaConta += 1
        self.__cliente = cli
        self.__saldo = sal
        self.__active = True
        self.__extrato = Extrato()
        self.__juros = 1.5
        self.__desconto = 0.50

    def __str__(self):
        return (f"Conta {self.numero}, cliente {self.cliente.nome}")

    @abc.abstractmethod
    def sacar(self, value):
        pass

    @abc.abstractmethod
    def depositar(self, value):
        pass

    @abc.abstractmethod
    def atualiza(self):
        pass

    @abc.abstractmethod
    def add_mov(self):
        pass

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
    def extrato(self):
        return self.__extrato.extrato

    def imprimir_extrato(self):
        print("Extrato gerado!")
        return self.__extrato.imprimir(self.numero)
    
    @property
    def active(self):
        return self.__active
    def change_active(self):
        today = datetime.now()
        day = today.strftime("%d/%m/%Y às %H:%M")
        if (self.__active):
            if self.__saldo == 0:
                self.__active = False
                self.extrato.append(f"|Encerramento| Conta {self.__numero} foi encerrada| {day}")
            else:
                return (print(f"A conta não pode ter saldo positivo para encerrá-la"))
        else:
            self.extrato.append(f"|Encerramento| Conta {self.__numero} foi reaberta| {day}")
            self.__active = True

    @property
    def juros(self):
        return self.__juros

    @property
    def desconto(self):
        return self.__desconto