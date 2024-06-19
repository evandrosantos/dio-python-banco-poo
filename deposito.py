from abc import ABCMeta
from conta import Conta
from transacao import Transacao


class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor
    
    def registrar(self, conta:Conta):
        conta.depositar(self._valor)