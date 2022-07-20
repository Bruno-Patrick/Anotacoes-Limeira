# Importações
from banco import Banco
from conta_corrente import ContaCorrente
from conta_poupança import ContaPoupanca
from conta_investimento import ContaInvestimento

# Criando objetos das classes
bank = Banco(1, "Nubank")
corrente = ContaCorrente(1, "Bruno", 150, 200)
poupanca = ContaPoupanca(2, "Patrick", 600, 8000)
investir = ContaInvestimento(3, "Nascimento", 2500, 7000)

#Main(){

bank.vincular_conta(corrente)
bank.vincular_conta(poupanca)
bank.vincular_conta(investir)

corrente.atualiza(3)
corrente.sacar(10)

poupanca.atualiza(2)
poupanca.sacar(20)

investir.atualiza()

bank.extrato_geral()