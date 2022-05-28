class Cliente:
    __slots__ = ['__endereco','__CPF','__idade']
    def __init__(self, e, cpf, i):
        # self.__nome = n
        self.__endereco = e
        self.__CPF = cpf
        self.__idade = i

    def converter_cpf(self):
        CPF = []
        CPF = list(self.__CPF)
        for i in range(0,11):
            CPF[i] = int(CPF[i])
        return CPF

    def calcula_digito(self, valor, key):
        CPF = self.converter_cpf()
        KEY = key
        SOMA = 0
        for i in range(0,valor):
            SOMA += CPF[i]*KEY
            KEY -= 1
        MOD = SOMA%11
        if MOD < 2:
            valorDigito = 0
            return valorDigito
        else:
            valorDigito = 11-MOD
            return valorDigito
    
    def verifica_cpf(self):
        PD = self.calcula_digito(9,10)
        SD = self.calcula_digito(10,11)
        CPF = self.converter_cpf()

        if PD == CPF[9] and SD == CPF[10]:
            print("CPF VÁLIDO")
        else:
            print("CPF INVÁLIDO")