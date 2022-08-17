from Cliente import Cliente

class Banco:
    __slots__ = ["__nome", "__numero", "__contas",
     "__juros", "__desconto"]

    def __init__(self, numero, nome):
        self.__nome = nome
        self.__numero = numero
        self.__contas = []

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def contas(self):
        return self.__contas
    def add_conta(self, conta):
        self.__contas.append(conta)

    @property
    def juros(self):
        return self.__juros
    @juros.setter
    def juros(self, value):
        self.__juros = value

    @property
    def desconto(self):
        return self.__desconto
    @desconto.setter
    def desconto(self, value):
        self.__desconto = value

    """
    def remove_conta(self, conta):
        try:
            self.__contas.remove(conta)
        except:
            print(f"Conta não encontrada!")
    """