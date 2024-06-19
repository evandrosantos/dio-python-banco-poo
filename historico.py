from transacao import Transacao


class Historico():
    def __init__(self) -> None:
        self._transacoes = list()
    
    def adicionar_transacao(self, transacao: Transacao) -> None:
        self._transacoes.append(transacao)