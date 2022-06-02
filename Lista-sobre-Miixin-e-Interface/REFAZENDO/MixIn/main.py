# Imports
from banco import Banco
from conta import Conta
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from SeguroDeVida import SeguroDeVida
# Fim dos imports

# Declaração dos objetos de classe
bank = Banco(1, "Nubank")
corrente = ContaCorrente(1, "Bruno", 100)
corrente2 = ContaCorrente(4, "Nascimento", 11250)
poupanca = ContaPoupanca(2, "Patrick", 200)
seguro = SeguroDeVida(3, 500, corrente)
# Fim da declaração dos objetos de classe

# Main(){

bank.vincular_conta(corrente)
bank.vincular_conta(corrente2)
bank.vincular_conta(poupanca)

corrente.atualiza(5)
corrente.valor_imposto()
corrente.extrato

poupanca.atualiza(7)
poupanca.extrato

seguro.valor_imposto()
corrente.extrato

bank.impostos
# }