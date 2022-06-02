from conta import Conta


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._extrato._transacoes.append(f"\n#< Atualização na Conta há {taxa}% #>")
        taxa = taxa/100
        valor = self._saldo * taxa * 3
        self.depositar(valor)
        return valor