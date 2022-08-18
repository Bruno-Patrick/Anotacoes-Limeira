from datetime import date
class Extrato:
    __slots__ = ["__extrato"]
    def __init__(self):
        self.__extrato = []

    @property
    def extrato(self):
        return self.__extrato

    def imprimir(self, numero, cliente):
        today = date.today()
        day = today.strftime("%d/%m/%Y")

        with open(f'trabalho1/extratos/{cliente}/{numero}_+{day}','a') as logger:
            for movimentacoes in self.extrato:
                logger.write(f"{movimentacoes}\n")