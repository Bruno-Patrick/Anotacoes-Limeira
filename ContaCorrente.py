from Conta import Conta

class ContaCorrente(Conta):

    def add_mov(self, operacao, valor, desconto):
        self.extrato.append(
            f"|{operacao}| no valor de {valor:.2f}, com desconto de {desconto:.2f}|"
        )

    def sacar(self, value):
        if self.__active == True:
            if self.__saldo < value:
                return (print(f"Quantia para saque inexistente"))
            else:
                self.__saldo =- (value + self.__desconto)
                operacao = "Saque"
                valor = value
                desconto = self.desconto
                self.add_mov(operacao, valor, desconto)
        else:
            return (print(f"Esta conta foi encerrada!"))

    def depositar(self, value):
        if self.__active == True:
            self.__saldo += (value - self.__desconto)
            operacao = "Depósito"
            valor = value
            desconto = self.desconto
            self.add_mov(operacao, valor, desconto)
        else:
            return(print(f"Esta conta foi encerrada!"))