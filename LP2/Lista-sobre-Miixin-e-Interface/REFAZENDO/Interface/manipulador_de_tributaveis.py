from tributavel_interface import TributavelInterface

class ManipuladorDeTributaveis:

    def calcular_impostos(self, lista):
        total = 0
        for tr in lista:
            if isinstance(tr, TributavelInterface):
                total += tr.valor_imposto()
            else:
                print(f"{tr} não é tributável")
        return print(f"total de impostos coletados: {total:,.2f}")