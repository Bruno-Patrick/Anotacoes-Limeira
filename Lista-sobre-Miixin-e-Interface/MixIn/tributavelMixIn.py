class TributavelMixIn():

    def valor_imposto(self, taxa):
        taxa = taxa/100
        valor = self._saldo*taxa
        return valor