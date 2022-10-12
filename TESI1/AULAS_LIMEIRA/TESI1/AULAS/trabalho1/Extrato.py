from datetime import date
import os, io
class Extrato:
    __slots__ = ["__extrato"]
    def __init__(self):
        self.__extrato = []

    @property
    def extrato(self):
        return self.__extrato

    def imprimir(self, numero):
        today = date.today()
        day = today.strftime("%d_%m_%Y")
        diretorio = os.path.dirname(__file__)
        with io.open(f'{diretorio}\extratos\Conta_{numero}_{day}.txt','a', encoding="utf-8") as logger:
            for movimentacoes in self.extrato:
                logger.write(f"{movimentacoes}\n")
