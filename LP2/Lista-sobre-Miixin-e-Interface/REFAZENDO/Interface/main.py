# Imports
from banco import Banco
from tributavel_interface import TributavelInterface
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from SeguroDeVida import SeguroDeVida
from conta_investimento import ContaInvestimento
# Fim dos imports

# Declaração dos objetos de classe
bank = Banco(1, "Nubank")
investimentos = ContaInvestimento(5, "Márcio", 750)
corrente = ContaCorrente(1, "Bruno", 100)
corrente2 = ContaCorrente(4, "Nascimento", 11250)
poupanca = ContaPoupanca(2, "Patrick", 200)
seguro = SeguroDeVida(3, 500, corrente)
# Fim da declaração dos objetos de classe

# Main(){
help(TributavelInterface)

TributavelInterface.register(ContaCorrente)
TributavelInterface.register(SeguroDeVida)
TributavelInterface.register(ContaInvestimento)

bank.vincular_conta(corrente)
bank.vincular_conta(corrente2)
bank.vincular_conta(poupanca)
bank.vincular_conta(investimentos)

corrente.atualiza(5)
corrente.valor_imposto()
corrente.extrato

poupanca.atualiza(7)
poupanca.extrato

seguro.valor_imposto()
corrente.extrato

investimentos.atualiza(4)
investimentos.valor_imposto()
investimentos.extrato

bank.impostos
bank.caixa_geral

# }