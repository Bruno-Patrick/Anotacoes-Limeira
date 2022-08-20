class Banco:
    __slots__ = ["__nome", "__numero", "__contas",
     "__juros", "__desconto"]

    def __init__(self, numero, nome):
        self.__nome = nome
        self.__numero = numero
        self.__contas = []
        self.__juros = 1.5
        self.__desconto = 0.20

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
        conta.__juros = self.__juros
        conta.__desconto = self.__desconto
        self.__contas.append(conta)

    @property
    def desconto(self):
        return self.__desconto
    @desconto.setter
    def desconto(self, value):
        self.__desconto = value
        self.fixar_desconto(self.__desconto)

    @property
    def juros(self):
        return self.__juros
    @juros.setter
    def juros(self, value):
        self.__juros = value
        self.fixar_juros(self.__juros)

    @property
    def desconto(self):
        return self.__desconto
    @desconto.setter
    def desconto(self, value):
        self.__desconto = value

    def fixar_juros(self, value):
        for conta in self.contas:
            conta.__juros = value
    def fixar_desconto(self,value):
        for conta in self.contas:
            conta.__desconto = value

    def remover(self, cliente):
        for conta in self.contas:
            if cliente.cpf == conta.cliente.cpf:
                return print(f"Cliente vinculado à uma conta. Impossível removê-lo!")
            else:
                del cliente