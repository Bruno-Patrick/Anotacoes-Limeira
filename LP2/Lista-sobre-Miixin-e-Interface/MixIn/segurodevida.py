from tributavelMixIn import TributavelMixIn


class SegurodeVida(TributavelMixIn):
    def __init__(self, titular, valordoSeguro, numero):
        self._titular = titular
        self._saldo = valordoSeguro
        self._numero = numero
        self._taxa = 5

    @property
    def taxa(self):
        return self._taxa
    @taxa.setter
    def taxa(self, valor):
        self._taxa = valor

    def taxa_decimal(self, taxa):
        return taxa/100

    def valor_imposto(self, taxa):
        valor = (self._saldo*self.taxa_decimal(taxa)) + 34
        return valor

    