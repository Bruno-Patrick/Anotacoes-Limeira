from contaPoupanca import ContaPoupanca

class ManipuladorDeTributaveis:

    def calcular_impostos(self, lista):
        total = 0
        for tr in lista:
            if isinstance(tr, ContaPoupanca):
                pass
            else:
                total += tr.valor_imposto()
        return print(f"total de impostos coletados: {total:,.2f}")