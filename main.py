from Banco import Banco
from Cliente import Cliente
from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupaca

# ------------ || ------------ #
b1 = Banco(1, "Banco do Brasil")
cliente = Cliente('Bruno Patriques', 'Sex GPS', '036319')
c1 = ContaCorrente(1, cliente, 300)