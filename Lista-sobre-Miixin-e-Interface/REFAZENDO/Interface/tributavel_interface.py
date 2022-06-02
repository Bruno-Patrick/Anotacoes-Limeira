import abc


class TributavelInterface(abc.ABC):
    """Classe que definirá outros objetos que serão tributáveis"""
    @abc.abstractmethod
    def valor_imposto(self):
        """Método que cálcuara, quando adequado às particularidades da classe,
        o valor do imposto a ser pago pela conta"""
        pass