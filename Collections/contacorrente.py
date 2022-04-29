from tkinter import commondialog


class Conta:
    def __init__(self, codigo, saldo) -> None:
        self._codigo = codigo
        self._saldo = saldo
    
    def deposita(self, saldo):
        self._saldo += 1
    
    def __str__(self) -> str:
        print(f'A Conta de código {self._codigo} possui {self._saldo} de saldo!')

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3