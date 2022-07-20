from produto import Produto


class ProdutoParcelado(Produto):
    def __init__(self, produto):
        self._produto = produto

    def definePrecoVenda(self, parcelas):
        self._produto._parcelado = 1
        self._produto._parcelas = parcelas
        self._produto._precoDeCompra = self._produto._preco_original
        juros = parcelas * 0.05
        self._produto._precoDeCompra += juros
        self._produto._precoDeCompra = self._produto._precoDeCompra/parcelas