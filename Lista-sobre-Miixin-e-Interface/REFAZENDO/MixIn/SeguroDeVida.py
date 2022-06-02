from tributavelMixIn import TributavelMixin


class SeguroDeVida(TributavelMixin):

    def __init__(self, numero, valor, conta):
        self._numero = numero
        self._valor = valor
        self._conta = conta #Irá comter o titular

    def valor_imposto(self):
        self._conta._extrato._transacoes.append(f"\n#< Cálculo de Imposto do Seguro de Vida #>")
        imposto = 34 + self._valor*0.05
        self._conta.sacar(imposto)
        return imposto
