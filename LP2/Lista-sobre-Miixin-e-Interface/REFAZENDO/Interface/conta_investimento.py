from conta import Conta


class ContaInvestimento(Conta):
    def valor_imposto(self):
        imposto = self.saldo * 0.03
        self._extrato._transacoes.append(f"\n#< Cálculo de Imposto na Conta de Investimentos #>")
        self.sacar(imposto)
        return imposto
    
    def atualiza(self, taxa):
        pass