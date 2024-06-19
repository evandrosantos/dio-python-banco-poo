from abc import ABC
from conta import Conta


class Transacao(ABC):
    @classmethod
    def registrar_conta(self, conta:Conta):
        pass
        