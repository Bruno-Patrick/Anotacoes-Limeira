from historico import Historico
class Emprestimo():
    
    __total_emprestimo = 0

    @classmethod
    def get__total_emprestimo(cls):
        return cls.__total_emprestimo

    @classmethod
    def total_emprestimos(cls):
        if cls.__total_emprestimo != 0:
            print("Total de emprestimos feitos pela conta: ",cls.__total_emprestimo)
        else:
            print("Não há empréstimos ativos para essa conta!")

    __slots__ = ['__juros', '__valor', '__periodo','__extrato','__conta', '__total', '__periodo','__parcela']
    def __init__(self, conta,valor, juros, periodo):
        self.__juros = juros/100
        self.__valor = valor
        self.__periodo = periodo
        self.__extrato = Historico()
        self.__conta = conta
        self.__total = self.__valor*self.__juros*self.__periodo
        self.__periodo = periodo
        self.__parcela = self.__total/self.__periodo
        return self.emprestimo()
   
    @property
    def get_emprestimo(self):
        return print(self.__valor)

    def get_total(self):
        print(f"O Montante é: {self.__total}")
        print(f"O juros é {self.__juros}")
        print(f"A parcela ficou {self.__parcela}")

    def emprestimo(self):
        self.__conta.depositar(self.__valor)
        print(f"Emprestimo realizado para a conta {self.__conta.get_numero()}")
        Emprestimo.__total_emprestimo += 1
        self.__extrato.transacoes.append(f'Emprestimo de {self.__valor}')

    def paga_emprestimo_avista(self):
        valor = self.__total
        if self.__conta.get_saldo() < valor:
            print("\nNão é possivel pagar o emprestimo a vista\n")
        else:
            self.__conta.sacar(valor)
            print("Emprestimo quitado!!\n")
            self.__extrato.transacoes.append(f'Quitado empréstimo no valor remanescente de {valor}')
            self.__periodo = 0
            self.__total = 0

        
    def pagar_emprestimo_parcela(self):
        self.__parcela
        if self.__conta.get_saldo() < self.__parcela or self.__total == 0:
            print("\nNão é possivel pagar a parcela!\n")
        else:
            self.__conta.sacar(self.__parcela)
            self.__total -= self.__parcela
            self.__periodo -= 1
            print("\nParcela paga com sucesso!\n")
            self.__extrato.transacoes.append(f'Parcela do empréstimo no valor de {self.__parcela}')
        if self.__parcela < self.__total:
            print("Você ainda possui parcelas a pagar: ",self.__periodo,"\n") 
        else:
            print("Emprestimo quitado\n")
            self.__total = 0
            Emprestimo.__total_emprestimo -= 1