from pydantic import BaseModel
from datetime import datetime as date

class Cartao(BaseModel):
    nome: str
    bandeira: str
    dia_vencimento: int
    limite: float
    lembrete: bool = True

    def __eq__(self, outro) -> bool:
        return self.nome == outro.nome

class Despesa(BaseModel):
    nome: str
    desc: str
    valor: float
    categoria: str # TODO: transformar em enum
    parcelas: int
    id_cartao: int
    data: date

    def __eq__(self, outro) -> bool:
        return self.nome == outro.nome
