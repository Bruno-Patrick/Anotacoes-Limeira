from banco import Banco
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca
from segurodevida import SegurodeVida
from manipulador import ManipuladorDeTributaveis
""" Criação dos Objetos """
B1 = Banco(1, "Banco do Brasil")
CC = ContaCorrente(2, "Bruno", 120)
CP = ContaPoupanca(3, "Patrick", 140)
Seguro = SegurodeVida("Bruno", 200, 2)
Manipulador = ManipuladorDeTributaveis()
""" Fim da Criação dos Objetos """

""" Main(){ """
print(dir(B1),'\n')
print(dir(CC),'\n')
print(dir(CP),'\n')

B1.vincular_conta(CC)
B1.vincular_conta(CP)
B1.vincular_conta(Seguro)

CC.atualiza(2)
CP.atualiza(5)

CC.depositar(3003)
CP.depositar(300)

CC.sacar(600)
CP.sacar(245)

CC.extrato.imprime()
CP.extrato.imprime()
Manipulador.calcular_impostos(B1.contas)

B1.caixa_geral