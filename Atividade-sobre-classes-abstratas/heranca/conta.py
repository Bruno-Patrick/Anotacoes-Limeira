class Conta:
    def __init__(self, n, cli, sal, lim):
        self._numero = n
        self._titular = cli
        self._saldo = sal
        self._limite = lim
        self._transacoes = []
        self._saldo_total = 0

    def __str__(self):
        return f"Titular: {self._titular} | Número da conta: {self._numero}"

    @property
    def saldo(self):
        return self._saldo

    @property
    def saldo_total(self):
        return self._saldo_total

    def sacar(self, valor):
        self._transacoes.append(f"\n<<Saque efetuado>>"+
        f"\nSaldo antigo: {self._saldo}")
        self._saldo -= valor
        self._transacoes.append(f"\nNovo saldo: {self._saldo}")


    def atualiza(self, taxa):
        taxa = taxa/100
        self._transacoes.append(f"\n<<Atualização no saldo>>"+
        f"\nSaldo antigo: {self._saldo}")
        self._saldo -= self._saldo*taxa
        self._transacoes.append(f"\nNovo saldo: {self._saldo}")
        self._saldo_total += self._saldo

    def deposita(self, valor):
        self._transacoes.append(f"\n<<Depósito bancário>>"+
        f"\nSaldo antigo: {self._saldo}")
        self._saldo += valor
        self._transacoes.append(f"\nNovo saldo: {self._saldo}")

    def imprimir_transacoes(self):
        print("#-----------------------------------#")
        print(f"\nTitular: {self._titular} | Nº da conta: {self._numero}")
        for banco in self._transacoes:
            print(banco)
        print("#-----------------------------------#")