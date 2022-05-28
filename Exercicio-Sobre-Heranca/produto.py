from extrato import Historico


class Produto:
    def __init__(self, nome = "", precoDeCompra = 0, quantidadeEstoque = 0):
        self._nome = nome
        self._precoDeCompra = precoDeCompra
        self._quantidadeEstoque = quantidadeEstoque
        self._preco_original = precoDeCompra
        self._parcelado = 0
        self._parcelas = 0
        self._historico = Historico()

    def extrato(self):
        return print(f"{self._nome} | {self._precoDeCompra} | {self._quantidadeEstoque} | {self._parcelado} \n")

    def valor_promocao(self):
        promocao = (100*self._precoDeCompra)/self._preco_original
        return promocao

    def definePrecoVenda(self, valor):
        self._parcelado = 0
        self._precoDeCompra = valor

    def vendeProduto(self, valor):
        if (valor < self._precoDeCompra) or (self._quantidadeEstoque <= 0):
            return print("A quantia é insuficiente ou não há estoque disponivel! \n")
        else:
            if self._parcelado == 1:
                self._quantidadeEstoque -= 1
                self._historico.transacoes.append(f'Venda de 1 {self._nome} ' +
                f' parcelado em {self._parcelas}x por R${self._precoDeCompra} cada parcela')
                return print("Venda efetuada com sucesso! \n")
                
            if (self._precoDeCompra < self._preco_original) and self._parcelado == 0:
                self._quantidadeEstoque -= 1
                self._historico.transacoes.append(f'Venda de 1 {self._nome} ' +
                f'com {self.valor_promocao()}% de desconto por R${self._precoDeCompra}')
                return print("Venda efetuada com sucesso! \n")
            else:
                self._quantidadeEstoque -= 1
                self._historico.transacoes.append(f'Venda de 1 {self._nome} por R${self._precoDeCompra}')
                return print("Venda efetuada com sucesso! \n")


    def compraProduto(self, valor):
        if valor < self._precoDeCompra:
            return print("A quantia é insuficiente! \n")
        else:
            if self._precoDeCompra < self._preco_original and self._parcelado == 0:
                self._quantidadeEstoque -= 1
                self._historico.transacoes.append(f'Compra de 1 {self._nome} ' +
                f'com {self.valor_promocao()}% de desconto por R${self._precoDeCompra}')
                return print("Venda efetuada com sucesso! \n")

            elif self._parcelado == 1:
                self._quantidadeEstoque -= 1
                self._historico.transacoes.append(f'Compra de 1 {self._nome} ' +
                f' parcelado em {self._parcelas}x por R${self._precoDeCompra} cada parcela')

            else:
                self._quantidadeEstoque += 1
                self._historico.transacoes.append(f'Compra de 1 {self._nome} por R${self._precoDeCompra}')
                return print("Compra efetuada com sucesso! \n")
