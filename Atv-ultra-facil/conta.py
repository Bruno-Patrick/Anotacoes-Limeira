from historico import Historico

class Conta:
    #Numero da conta:
    _num_conta = 1
    total_dinheiro = 0
    __slots__ = ['__numero', '__titular', '__saldo', '__limite','__extrato']
    def __init__(self,cli,sal,lim):
        self.__numero = Conta._num_conta
        self.__titular = cli
        self.__saldo = sal
        self.__limite = lim
        self.__extrato = Historico()
        Conta.total_dinheiro += self.__saldo
        Conta._num_conta += 1

    
    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def get_extrato(self):
        return self.__extrato

    def encerrar_conta(self):
        try:
            if self.__saldo == 0:
                for i in range(0,len(self.__extrato.transacoes)-2):
                    self.__extrato.transacoes.remove(self.__extrato.transacoes[i])
                del self.__numero
                del self.__titular
                del self.__saldo
                del self.__limite
                Conta._num_conta -= 1

                print("A conta foi encerrada com sucesso!")
            else:
                print("O SALDO DA CONTA DEVERÁ ESTAR ZERADO!!")
        except AttributeError:
            print("A CONTA FOI ENCERRADA!!")
    
    def depositar(self, valor):
        self.__saldo += valor
        Conta.total_dinheiro += valor
        self.__extrato.transacoes.append('Depósito de {}'.format(valor))
        return print(f"Depósito de {valor} efetuado!")

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            Conta.total_dinheiro -= valor
            self.__extrato.transacoes.append('Saque de {}'.format(valor))
            print(f"Saque de {valor} efetuado!")
        else:
            print("Saldo insuficiente!!!")