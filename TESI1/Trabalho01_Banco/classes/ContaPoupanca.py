from datetime import datetime
from Conta import Conta

class ContaPoupaca(Conta):

    def add_mov(self, operacao, valor):
        today = datetime.now()
        day = today.strftime("%d/%m/%Y às %H:%M")
        self.extrato.append(
            f"|{operacao}| no valor de R${valor:.2f}| {day}"
        )

    def sacar(self, value):
        if self.active == True:
            if self.saldo < value:
                return "Quantia insuficiente"
            else:
                self.saldo = (self.saldo-value)
                operacao = "Saque"
                valor = value
                self.add_mov(operacao, valor)
                return True
        else:
            return "Sua conta está encerrada"

    def depositar(self, value):
        if self.active == True:
            self.saldo = (self.saldo+value)
            operacao = "Depósito"
            valor = value
            self.add_mov(operacao, valor)
            return True
        else:
            return "Sua conta está encerrada"

    def atualiza(self):
        juros = self.saldo*(self.juros/100)
        operacao = "Atualização"
        valor = juros
        self.add_mov(operacao, valor)
        self.depositar(juros)

        