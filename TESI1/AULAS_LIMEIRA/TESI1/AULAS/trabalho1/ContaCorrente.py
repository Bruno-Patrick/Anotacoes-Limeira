from Conta import Conta
from datetime import datetime

class ContaCorrente(Conta):

    def add_mov(self, operacao, valor, desconto):
        today = datetime.now()
        day = today.strftime("%d/%m/%Y às %H:%M")
        self.extrato.append(
            f"|{operacao}| no valor de {valor:.2f}, com desconto de {desconto:.2f}| {day}|"
        )

    def sacar(self, value):
        if self.active == True:
            if self.saldo < value+self.desconto:
                return "Quantia insuficiente"
            else:
                self.saldo = (self.saldo-(value + self.desconto))
                operacao = "Saque"
                valor = value
                desconto = self.desconto
                self.add_mov(operacao, valor, desconto)
                return True
        else:
            return "Sua conta está encerrada"

    def depositar(self, value):
        if self.active == True:
            self.saldo = (self.saldo + (value - self.desconto))
            operacao = "Depósito"
            valor = value
            desconto = self.desconto
            self.add_mov(operacao, valor, desconto)
            return True
        else:
            return "Sua conta está encerrada"

    def atualiza(self):
        pass