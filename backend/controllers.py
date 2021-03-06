from datetime import datetime as date
from .schemas import Cartao, Despesa
from dataclasses import dataclass, field

@dataclass
class Controlador:
    lembrete: int = 2
    cartoes: list[Cartao] = field(default_factory=list)
    despesas: list[Despesa] = field(default_factory=list)

    def adicionar_cartao(self, cartao: Cartao):
        assert cartao not in self.cartoes, 'O cartão já existe no sistema (nomes devem ser únicos)'
        self.cartoes.append(cartao)

    def remover_cartao(self, nome: str):
        try:
            result = next(cartao for cartao in self.cartoes if cartao.nome == nome)
            self.despesas = [d for d in self.despesas if d.nome_cartao != nome]
        except StopIteration:
            raise KeyError('nome não encontrado')
        self.cartoes.remove(result)


    def adicionar_despesa(self, despesa: Despesa): 
        self.despesas.append(despesa)

    def remover_despesa(self, nome: str):
        try:
            result = next(despesa for despesa in self.despesas if despesa.nome == nome)
        except StopIteration:
            raise KeyError('despesa (nome) não encontrado')
        self.despesas.remove(result)

    def gerar_relatorio(self):
        pass # TODO

    def pesquisar_despesa(self, id: int) -> Despesa:
        pass # TODO

    def prazo_lembrete(self, dias_antes: int):
        self.lembrete = dias_antes

    def listar_despesas(self,
        nome_cartao: str | None = None,
        data_inicio: date = date.min,
        data_fim: date = date.max
    ):
        return [despesa for despesa in self.despesas if
            data_inicio < despesa.data < data_fim and
            (True if nome_cartao is None else despesa.nome_cartao == nome_cartao)
        ]
        

    def gerar_grafico():
        pass

