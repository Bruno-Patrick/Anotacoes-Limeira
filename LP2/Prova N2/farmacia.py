class Farmacia:
    __slots__ = ['_produtos','_transacoes','_lucro_total','_desconto_total','_produtos_vendidos']
    def __init__(self):
        self._produtos = []
        self._transacoes = []
        self._lucro_total = 0
        self._desconto_total = 0
        self._produtos_vendidos = 0

    @property
    def produtos(self):
        return self._produtos
    @property
    def transacoes(self):
        return self._transacoes
    @property
    def lucro_total(self):
        return self._lucro_total
    @lucro_total.setter
    def lucro_total(self, valor):
        self._lucro_total += valor
    @property
    def desconto_total(self):
        return self._desconto_total
    @desconto_total.setter
    def desconto_total(self, valor):
        self._desconto_total += valor
    @property
    def produtos_vendidos(self):
        return self._produtos_vendidos
    @produtos_vendidos.setter
    def produtos_vendidos(self, valor):
        self._produtos_vendidos += valor

    def cadastrar_produtos(self, produto):
        self.produtos.append(produto)

    def imprimir(self):
        for mov in self.produtos:
            for i in range(0, len(mov.farmacia.transacoes)):
                print(mov.farmacia.transacoes[i])
    
    def situacao_monetaria(self):
        self.lucro_total = 0
        self.desconto_total = 0
        self.produtos_vendidos = 0
        for produtos in self.produtos:
            self.lucro_total += produtos.farmacia.lucro_total
            self.desconto_total += produtos.farmacia.desconto_total
            self.produtos_vendidos += produtos.farmacia.produtos_vendidos
        print(f"\n||———————————————————————————————————————————————————||")
        print(f"||Total de Produtos Vendidos || {self.produtos_vendidos:,.0f}                    ||")   
        print(f"||Lucro total da Farmácia    || {self.lucro_total:,.2f}                ||")   
        print(f"||Desconto total da Farmácia || {self.produtos_vendidos:,.2f}                 ||")   
        print(f"||———————————————————————————————————————————————————||\n")
