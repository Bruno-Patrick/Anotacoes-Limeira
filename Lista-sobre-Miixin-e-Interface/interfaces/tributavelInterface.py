import abc


class TributavelInterface(abc.ABC):
    """Classe que contém operações de um objeto tributável As
    subclasses concretas devem sobrescrever o método valor_imposto.
    """
    @abc.abstractmethod
    def valor_imposto(self, taxa):
        """Calcula o imposto que se sujeitará sobre determinada conta"""
        pass