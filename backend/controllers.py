from datetime import datetime as date
from .models import Cartao, Despesa
from dataclasses import dataclass, field

@dataclass
class Controlador:
    lembrete: int = 2
    cartoes: list[Cartao] = field(default_factory=list)
    despesas: list[Despesa] = field(default_factory=list)

    def adicionar_cartao(self, cartao: Cartao):
        if cartao.id in (c.id for c in self.cartoes):
            raise ValueError('Esse id de cartão já existe')
        self.cartoes.append(cartao)

    def remover_cartao(self, id: int):
        try:
            result = next(cartao for cartao in self.cartoes if cartao.id == id)
        except StopIteration:
            raise KeyError('id não encontrado')
        self.cartoes.remove(result)

    def adicionar_despesa(self, despesa: Despesa):
        if despesa.id in (d.id for d in self.despesas):
            raise ValueError('Esse id de despesa já existe')

        if despesa.id_cartao not in (c.id for c in self.cartoes): 
            raise ValueError('Esse id de cartão não existe')

        self.despesas.append(despesa)

    def remover_despesa(self, id: int):
        try:
            result = next(despesa for despesa in self.despesas if despesa.id == id)
        except StopIteration:
            raise KeyError('id não encontrado')
        self.despesas.remove(result)

    def gerar_relatorio(self):
        pass # TODO

    def pesquisar_despesa(self, id: int) -> Despesa:
        pass # TODO

    def prazo_lembrete(self, dias_antes: int):
        self.lembrete = dias_antes

    def listar_despesas(self, data_inicio:date = None, data_fim:date = None):
        return [despesa for despesa in self.despesas if data_inicio < despesa.data < data_fim]

    def gerar_grafico():
        pass

