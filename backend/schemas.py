from pydantic import BaseModel
from datetime import date
from uuid import uuid1

class Cartao(BaseModel):
    nome: str
    bandeira: str
    dia_vencimento: int
    limite: float
    lembrete: bool = True

    def __eq__(self, outro) -> bool:
        return self.nome == outro.nome

class Despesa(BaseModel):
    id: str = uuid1()
    desc: str
    valor: float
    categoria: str # TODO: transformar em enum
    parcelas: int
    nome_cartao: str
    data: date
