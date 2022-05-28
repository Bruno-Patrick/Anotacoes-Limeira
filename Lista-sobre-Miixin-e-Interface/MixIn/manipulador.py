from tributavelMixIn import TributavelMixIn

class ManipuladorDeTributaveis:
    def calcular_impostos(self, lista_tributaveis):
        total = 0
        for tr in lista_tributaveis:
            if isinstance(tr, TributavelMixIn):
                total += tr.valor_imposto(tr._taxa)
        return print(f"Impostos coletados: R${total:,.2f}")