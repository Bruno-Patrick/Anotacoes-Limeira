import abc
from datetime import date, datetime
from IncentivoFiscal_Interface import InterfaceIncentivoFiscal
from ICMS_Mixin import ICMSMixin
from farmacia import Farmacia


class Produto(abc.ABC):
    __slots__ = ["_codigo", "_descricao", "_preco", "_vencimento"]
    def __init__(self, codigo=0000, descricao='None', preco=0.00, vencimento='00/00/0000'):
        self._codigo = codigo
        self._descricao = descricao
        self._preco = preco
        self._vencimento = vencimento
        self._farmacia = Farmacia()

    @property
    def codigo(self):
        return self._codigo
    @property
    def descricao(self):
        return self._descricao
    @property
    def preco(self):
        return self._preco
    @property
    def vencimento(self):
        return self._vencimento
    @property
    def farmacia(self):
        return self._farmacia
    @property
    def data(self):
        hora = datetime.now()
        hora = hora.strftime('%d/%m/%Y %H:%M')
        return f'{hora}'

    @abc.abstractmethod
    def margem_lucro(self):
        pass
    @abc.abstractmethod
    def comprar(self, valor):
        pass


    
class Generico(Produto, InterfaceIncentivoFiscal):
    def margem_lucro(self):
        return self._preco*0.20

    def incentivo_fiscal(self):
        return self._preco*0.10

    def comprar(self, valor):
        valorFinal = self.preco + self.margem_lucro() - self.incentivo_fiscal()
        if (valor < valorFinal):
            print(f'R${valor:,.2f} é insuficiente para comprar o {self.descricao}')
        else:
            self.farmacia.desconto_total += self.incentivo_fiscal()
            self.farmacia.lucro_total += valorFinal
            self.farmacia.produtos_vendidos += 1

            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')
            self.farmacia.transacoes.append(f"|| [Codigo: {self.codigo}]   [Descrição:"+
            f' {self.descricao}]   [Preço: {valorFinal:,.2f}]   [Vencimento: {self.vencimento}] ||')
            self.farmacia.transacoes.append(f"||        {self.descricao} comprada em {self.data}"+
            "                                        ||")
            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')


class Referencia(Produto, ICMSMixin):
    def margem_lucro(self):
        return self._preco*0.50

    def ICMS(self):
        return super().ICMS()
    
    def comprar(self, valor):
        valorFinal = self.preco + self.margem_lucro() + self.ICMS()
        if (valor < valorFinal):
            return print(f'{valor:,.2f} é insuficiente para comprar o {self.descricao}')
        else:
            self.farmacia.lucro_total += valorFinal
            self.farmacia.produtos_vendidos += 1

            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')
            self.farmacia.transacoes.append(f"|| [Codigo: {self.codigo}]   [Descrição:"+
            f' {self.descricao}]   [Preço: {valorFinal:,.2f}]   [Vencimento: {self.vencimento}] ||')
            self.farmacia.transacoes.append(f"||        {self.descricao} comprada em {self.data}"+
            "                                        ||")
            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')

class Similar(Produto, ICMSMixin):
    def margem_lucro(self):
        return self.preco*0.40
    
    def ICMS(self):
        return super().ICMS()
    
    def comprar(self, valor):
        valorFinal = self.preco + self.margem_lucro() + self.ICMS()
        if (valor < valorFinal):
            return print(f'{valor:,.2f} é insuficiente para comprar o {self.descricao}')
        else:
            self.farmacia.lucro_total += valorFinal
            self.farmacia.produtos_vendidos += 1

            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')
            self.farmacia.transacoes.append(f"|| [Codigo: {self.codigo}]   [Descrição:"+
            f' {self.descricao}]   [Preço: {valorFinal:,.2f}]   [Vencimento: {self.vencimento}] ||')
            self.farmacia.transacoes.append(f"||        {self.descricao} comprada em {self.data}"+
            "                                        ||")
            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')

class Beleza(Produto):
    def margem_lucro(self):
        return self._preco * 0.70

    def comprar(self, valor):
        valorFinal = self.preco + self.margem_lucro()
        if (valor < valorFinal):
            return print(f'{valor:,.2f} é insuficiente para comprar o {self.descricao}')
        else:
            self.farmacia.lucro_total += valorFinal
            self.farmacia.produtos_vendidos += 1

            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')
            self.farmacia.transacoes.append(f"|| [Codigo: {self.codigo}]   [Descrição:"+
            f' {self.descricao}]   [Preço: {valorFinal:,.2f}]   [Vencimento: {self.vencimento}] ||')
            self.farmacia.transacoes.append(f"||        {self.descricao} comprada em {self.data}"+
            "                                        ||")
            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')

class Higiene(Produto):
    def margem_lucro(self):
        return self._preco * 0.30

    def comprar(self, valor):
        valorFinal = self.preco + self.margem_lucro()
        if (valor < valorFinal):
            return print(f'{valor:,.2f} é insuficiente para comprar o {self.descricao}')
        else:
            self.farmacia.lucro_total += valorFinal
            self.farmacia.produtos_vendidos += 1

            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')
            self.farmacia.transacoes.append(f"|| [Codigo: {self.codigo}]   [Descrição:"+
            f' {self.descricao}]   [Preço: {valorFinal:,.2f}]   [Vencimento: {self.vencimento}] ||')
            self.farmacia.transacoes.append(f"||        {self.descricao} comprada em {self.data}"+
            "                                        ||")
            self.farmacia.transacoes.append(f"||—————————————————————————————————"
            '————————————————————————————————————————————————————||')  
