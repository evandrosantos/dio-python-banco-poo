from cliente import Cliente
from deposito import Deposito
from historico import Historico
from saque import Saque

class Conta():
    AGENCIA = "0001"
    
    def __init__(self,  numero: int, cliente: Cliente) -> None:
        self._saldo = 0.0
        self._numero = numero
        self._agencia = Conta.AGENCIA
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int) -> Conta:
        return cls(numero, cliente)
    
    
    def sacar(self, valor: float) -> bool:
        saque_efetuado = False
        
        if valor <= 0:
            print("Valor inválido")
        elif valor > self._saldo:
            print("Saldo insuficiente para relizar essa transação")
        else:
            self._saldo -= valor
            self._historico.adicionar_transacao(Saque(valor))
            saque_efetuado =  True
        
        return saque_efetuado
    

    def depositar(self, valor: float) -> bool:
        deposito_efetuado = False
        
        if valor <= 0:
            print("Valor inválido")
        else:
            self._saldo += valor
            self._historico.adicionar_transacao(Deposito(valor))
            deposito_efetuado =  True
        
        return deposito_efetuado

 