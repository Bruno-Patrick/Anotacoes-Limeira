from tributavelInterface import TributavelInterface

class ManipuladorDeTributaveis:
    def calcular_impostos(self, lista_tributaveis):
        total = 0
        for tr in lista_tributaveis:
            if isinstance(tr, TributavelInterface):
                total += tr.valor_imposto(tr._taxa)
            else:
                print(f"Conta N° {tr._numero} | Titular: {tr._titular} não é tributável")
        return print(f"Impostos coletados: R${total:,.2f}")