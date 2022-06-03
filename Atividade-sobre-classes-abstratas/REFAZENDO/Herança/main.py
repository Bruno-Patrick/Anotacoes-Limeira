# Importações
from distutils import core
from banco import Banco
from conta_corrente import ContaCorrente
from conta_poupança import ContaPoupanca

# Criando objetos das classes
bank = Banco(1, "Nubank")
corrente = ContaCorrente(1, "Bruno", 150, 200)
poupanca = ContaPoupanca(2, "Patrick", 600, 8000)

#Main(){

bank.vincular_conta(corrente)
bank.vincular_conta(poupanca)

corrente.atualiza(3)
corrente.sacar(10)
corrente.depositar(132)

poupanca.atualiza(2)
poupanca.sacar(20)
poupanca.depositar(114)
poupanca.sacar(114)

bank.extrato_geral()