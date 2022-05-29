from banco import Banco
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca
from segurodevida import SegurodeVida
from manipulador import ManipuladorDeTributaveis
from tributavelInterface import TributavelInterface
from ContaInvestimento import Investimento
""" Criação dos Objetos """
B1 = Banco(1, "Banco do Brasil")
CC = ContaCorrente(2, "Bruno", 120)
CP = ContaPoupanca(3, "Patrick", 140)
investir = Investimento(5,"Mariano", 1009)
Seguro = SegurodeVida("Bruno Patrick", 300, 4)
Manipulador = ManipuladorDeTributaveis()
""" Fim da Criação dos Objetos """

""" Main(){ """
print(dir(B1),'\n')
print(dir(CC),'\n')
print(dir(CP),'\n')

TributavelInterface.register(ContaCorrente)
TributavelInterface.register(SegurodeVida)
TributavelInterface.register(Investimento)

B1.vincular_conta(CC)
B1.vincular_conta(CP)
B1.vincular_conta(Seguro)
B1.vincular_conta(investir)

CC.atualiza(2)
CP.atualiza(1)

CC.depositar(3003)
CP.depositar(300)

CC.sacar(600)
CP.sacar(245)

CC.extrato.imprime()
CP.extrato.imprime()
B1.tributos()

B1.caixa_geral