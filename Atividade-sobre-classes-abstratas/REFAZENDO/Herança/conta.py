from historico import Historico

class Conta:
    def __init__(self, n, cli, sal, lim):
        self._numero = n
        self._titular = cli
        self._saldo = sal
        self._limite = lim
        self._extrato = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def extrato(self):
        return self._extrato.imprime()

    def __str__(self):
        return f"Conta N° {self._numero} | TITULAR: {self._titular}"

    def atualiza(self, taxa):
        self._extrato._transacoes.append(f"\n-- Atualização no saldo --")
        valor = self._saldo*(taxa/100)
        self.sacar(valor)
        return valor

    def sacar(self, valor):
        self._extrato._transacoes.append(f"\n-- Saque de {valor} --")
        self._extrato._transacoes.append(f"\n   -->Saldo Anterior: {self.saldo:,.2f}")
        self._saldo -= valor
        self._extrato._transacoes.append(f"\n   -->Saldo Novo: {self.saldo:,.2f}")

    def depositar(self, valor):
        self._extrato._transacoes.append(f"\n-- Depósito de {valor} --")
        self._extrato._transacoes.append(f"\n   -->Saldo Anterior: {self.saldo:,.2f}")
        self._saldo += valor
        self._extrato._transacoes.append(f"\n   -->Saldo Novo: {self.saldo:,.2f}")