class Promocao:
    def __init__(self, produto):
        self._produto = produto

    def definir_promocao(self):
        self._produto._parcelado = 0
        self._produto._precoDeCompra = self._produto._preco_original
        self._produto._precoDeCompra = self._produto._precoDeCompra * 0.5