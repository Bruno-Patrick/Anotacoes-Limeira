from conta import Conta


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._extrato._transacoes.append(f"\nAtualização_na_Conta() =>")
        valor = self._saldo * taxa * 3
        self._extrato._transacoes.append(f"\n<= Fim_da_Atualização")
        self.depositar(valor)
        return valor

    def __str__(self):
        super().__str__