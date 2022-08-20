from Banco import Banco
from Cliente import Cliente
from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupaca
# ------------ || ------------ #
b1 = Banco(1, "Banco do Brasil")
cliente = Cliente('Bruno Patriques', 'Sex GPS', '036319')
cliente2 = Cliente('Bruno Patriques', 'Sex GPS', '03631932')
c1 = ContaCorrente(1, cliente, 300)
c2 = ContaPoupaca(2,cliente,300)
c3 = ContaPoupaca(3, cliente, 12)

c1.change_active()
print(c1.active)

b1.add_conta(c1)
c1.sacar(100)
c1.sacar(100)
c1.depositar(100)
c1.depositar(100)
c1.depositar(100)
c1.depositar(100)
c1.sacar(100)
c1.sacar(396)
print(c1.saldo)
c1.change_active()
print(c1.active)
c1.sacar(100)
c1.depositar(100)
c1.change_active()
c1.imprimir_extrato()

b1.add_conta(c2)
print(c2.saldo)
c2.sacar(200)
c2.depositar(100)
c2.atualiza()
c2.sacar(203)
c2.change_active()
c2.sacar(200)
c2.depositar(100)
print(c2.saldo)
c2.change_active()
c2.imprimir_extrato()

print(b1.contas)
b1.remover(cliente2)
print(cliente2)