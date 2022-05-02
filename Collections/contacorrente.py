from abc import ABCMeta, abstractmethod
class Conta(abstractmethod):
    def __init__(self, codigo, saldo) -> None:
        self._codigo = codigo
        self._saldo = saldo
    
    def deposita(self, saldo):
        self._saldo += 1
    
    def __str__(self) -> str:
        print(f'A Conta de código {self._codigo} possui {self._saldo} de saldo!')

    @abstractmethod
    def passa_o_mes(self):
        raise NotImplementedError
class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaSalario:
    def __init__(self, codigo) -> None:
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, other): # utilizado para comparar o que está vindo como parâmetro ao invés do objeto inteiro.
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo
    
    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
            self._codigo < other._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self) -> str:
        return "(>> Código {} | Saldo {}<<)".format(self._codigo, self._saldo)
