from produto import Produto
from ProdutoParcelado import ProdutoParcelado
from ProdutoPromocional import ProdutoPromocional
from promocao import Promocao

##########Objetos da Classe##########
banana = Produto('banana',10,3)
banana_promocao = ProdutoPromocional(banana)
banana_promocao50 = Promocao(banana)
banana_parcelada = ProdutoParcelado(banana)
#####################################
banana.vendeProduto(10)
banana.vendeProduto(9)
banana_promocao.definePrecoVenda()
banana.vendeProduto(8)
banana.vendeProduto(7)
banana_promocao50.definir_promocao()
banana.extrato()
banana.vendeProduto(2)
banana.vendeProduto(5)
banana.vendeProduto(5)
banana.compraProduto(5)
banana.compraProduto(1)
banana.definePrecoVenda(16)
banana.compraProduto(15)
banana.vendeProduto(15)
banana.compraProduto(16)
banana_parcelada.definePrecoVenda(2)
print(banana._parcelado)
banana.vendeProduto(16)
banana._historico.imprime()