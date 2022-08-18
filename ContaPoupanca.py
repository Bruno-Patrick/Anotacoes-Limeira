from Conta import Conta

class ContaPoupaca(Conta):

    def add_mov(self, operacao, valor):
        self.extrato.append(
            f"|{operacao}| no valor de R${valor:.2f}|"
        )

    def sacar(self, value):
        if self.__active == True:
            if self.__saldo < value:
                return (print(f"Quantia inexistente"))
            else:
                self.__saldo =- value

                operacao = "Saque"
                valor = value
                self.add_mov(operacao, valor)
        else:
            return (print(f"Esta conta foi encerrada!"))

    def depositar(self, value):
        if self.__active == True:
            self.__saldo += value

            operacao = "Depósito"
            valor = value
            self.add_mov(operacao, valor)
        else:
            return(print(f"Esta conta foi encerrada!"))

    def atualiza(self):
        juros = self.saldo*(self.__juros/100)
        operacao = "Atualização"
        valor = juros
        self.add_mov(operacao, valor)
        depositar(juros)

        