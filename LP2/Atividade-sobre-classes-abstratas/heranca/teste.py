from banco import Banco
from conta import Conta
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

# -----------------------------------------------------------------#

BB = Banco(1, "Banco do Brasil")
conta1 = Conta(1, "Bruno Patrick", 70, 1200)
contaCC = ContaCorrente(2, "Bruno Patrick", 70, 1200)
contaP = ContaPoupanca(2, "Bruno Patrick", 70, 1200)

#--------------------------#
BB.vincular_conta(conta1)
conta1.deposita(220)
conta1.saldo
conta1.atualiza(2)
conta1.saldo
#--------------------------#
BB.vincular_conta(contaCC)
contaCC.deposita(200)
contaCC.saldo
contaCC.atualiza(2)
contaCC.saldo
#--------------------------#
BB.vincular_conta(contaP)
contaP.deposita(230)
contaP.saldo
contaP.atualiza(2)
contaP.saldo

BB.relatorio()
print(conta1)

BB.total_atualizacoes()