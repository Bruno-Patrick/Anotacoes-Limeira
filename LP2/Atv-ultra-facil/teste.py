from io import BufferedRandom
from banco import Banco
from cliente import Cliente
from conta import Conta
from emprestimo import Emprestimo
from historico import Historico

cliente1 = Cliente("Rua lala", "03631929219", "19")
cliente1.verifica_cpf()
cliente2 = Cliente("Rua lala", "03631929218", "19")
cliente2.verifica_cpf()

conta1 = Conta('Bruno Patrick', 200, 1200)
conta1.sacar(100)
conta1.depositar(100)
conta1.encerrar_conta()
conta1.depositar(359)

BRADESCO = Banco('BRADESCO', 237)
conta2 = Conta('Marcelo Bonitin', 200, 1200)
BRADESCO.vincular_conta(conta2)
BRADESCO.remover_contas(conta2)
BRADESCO.vincular_conta(conta2)
BRADESCO.vincular_conta(conta1)
BRADESCO.extrato()
conta1.sacar(559)
# conta1.encerrar_conta()

conta3 = Conta('Rodrigo Caranáuas', 0, 1200)
BRADESCO.vincular_conta(conta3)
emprestimo_conta3 = Emprestimo(conta3,200,12,10)
emprestimo_conta3.pagar_emprestimo_parcela()
emprestimo_conta3.paga_emprestimo_avista()
conta3.depositar(50000)
emprestimo_conta3.paga_emprestimo_avista()
