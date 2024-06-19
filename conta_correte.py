from cliente import Cliente
from conta import Conta


class ContaCorrente(Conta):
    LIMITE = 500.0
    LIMITE_SAQUES = 3
    
    def __init__(self, saldo: float, numero: int, cliente: Cliente) -> None:
        super().__init__(saldo, numero, cliente)
        self._limite = ContaCorrente.LIMITE
        self._limite_saques = ContaCorrente.LIMITE_SAQUES
        