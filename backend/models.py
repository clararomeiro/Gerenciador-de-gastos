from pydantic import BaseModel
from datetime import datetime as date

class Cartao(BaseModel):
    id: int
    nome: str
    bandeira: str
    dia_vencimento: int
    limite: float
    lembrete: bool

class Despesa(BaseModel):
    id: int
    nome: str
    desc: str
    valor: float
    categoria: str # TODO: transformar em enum
    parcelas: int
    id_cartao: int
    data: date
