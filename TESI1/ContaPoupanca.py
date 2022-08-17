from Conta import Conta

class ContaPoupaca(Conta):

    def sacar(self, value):
        if self.__active == True:
            if self.__saldo < value:
                return (print(f"Quantia inexistente"))
            else:
                self.__saldo =- value
                self.__extrato.append(f"Saque de {value}!")
        else:
            return (print(f"Esta conta foi encerrada!"))

    def depositar(self, value):
        if self.__active == True:
            self.__saldo += value
            self.__extrato.append(f"Depósito de {value}!")
        else:
            return(print(f"Esta conta foi encerrada!"))

    def atualiza(self):
        juros = self.__juros/100
        depositar(juros)
        