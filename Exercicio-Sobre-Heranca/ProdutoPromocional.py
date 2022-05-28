from produto import Produto

class ProdutoPromocional(Produto):
    def __init__(self, produto):
        self._produto = produto

    def definePrecoVenda(self):
        self._produto._parcelado = 0
        self._produto._precoDeCompra = self._produto._preco_original
        self._produto._precoDeCompra -= self._produto._precoDeCompra * 0.20