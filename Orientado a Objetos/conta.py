class Conta():
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo do {self.__titular} é {self.__saldo} real(is)')

    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        self.__saldo -= valor
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f'Saque de {valor} real(is) realizado com sucesso!')
        else:
            print('Valor de saque indisponível! Verifique se o valor está correto e tente novamente.')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco(self):
        return "001"

    @staticmethod
    def codigos_bancos(self):
        return {'BB': '001', 'Caixa':'104', 'Bradesco':'237'}

pass