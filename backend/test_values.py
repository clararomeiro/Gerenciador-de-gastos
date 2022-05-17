from backend.controllers import Controlador
from backend.schemas import Cartao, Despesa
from datetime import date

def adicionar_info(system: Controlador):
    system.adicionar_cartao(Cartao(
        nome='gabriel',
        bandeira='Visa',
        dia_vencimento=2,
        limite=1000.0
    ))
    system.adicionar_despesa(Despesa(
        desc='Notebook',
        valor=3180.0,
        categoria='Entretenimento',
        parcelas=8,
        nome_cartao='gabriel',
        data=date(2021, 1, 29)
    ))
    system.adicionar_despesa(Despesa(
        desc='Hamburguer',
        valor=15.0,
        categoria='Alimentação',
        parcelas=1,
        nome_cartao='gabriel',
        data=date(2021, 8, 10)
    ))
    system.adicionar_despesa(Despesa(
        desc='Pizza de calabresa',
        valor=32.8,
        categoria='Alimentação',
        parcelas=1,
        nome_cartao='gabriel',
        data=date(2022, 5, 15)
    ))

    # ============================================================
    system.adicionar_cartao(Cartao(
        nome='clara',
        bandeira='Mastercard',
        dia_vencimento=6,
        limite=6000.0
    ))
    system.adicionar_despesa(Despesa(
        desc='Smartphone',
        valor=2000.0,
        categoria='Outro',
        parcelas=10,
        nome_cartao='clara',
        data=date(2021, 3, 1)
    ))
    system.adicionar_despesa(Despesa(
        desc='PC Gamer',
        valor=5020.0,
        categoria='Outro',
        parcelas=12,
        nome_cartao='clara',
        data=date(2021, 3, 1)
    ))
    # ============================================================
    system.adicionar_cartao(Cartao(
        nome='aldenir',
        bandeira='Elo',
        dia_vencimento=9,
        limite=5000.0
    ))
    system.adicionar_despesa(Despesa(
        desc='Sapato novo',
        valor=120.0,
        categoria='Outro',
        parcelas=2,
        nome_cartao='aldenir',
        data=date.today()
    ))
    system.adicionar_cartao(Cartao(
        nome='ggdesu',
        bandeira='Hipercard',
        dia_vencimento=12,
        limite=20000.0
    ))
    # ============================================================
    system.adicionar_despesa(Despesa(
        desc='gadget china',
        valor=80.0,
        categoria='Entretenimento',
        parcelas=2,
        nome_cartao='ggdesu',
        data=date(2021, 12, 1)
    ))
    system.adicionar_despesa(Despesa(
        desc='gadget china',
        valor=70.0,
        categoria='Entretenimento',
        parcelas=1,
        nome_cartao='ggdesu',
        data=date(2022, 1, 1)
    ))
    system.adicionar_despesa(Despesa(
        desc='fone de ouvido',
        valor=189.0,
        categoria='Entretenimento',
        parcelas=3,
        nome_cartao='ggdesu',
        data=date(2022, 2, 1)
    ))
    system.adicionar_despesa(Despesa(
        desc='pen drive',
        valor=110.0,
        categoria='Entretenimento',
        parcelas=2,
        nome_cartao='ggdesu',
        data=date(2022, 3, 1)
    ))
    system.adicionar_despesa(Despesa(
        desc='camera',
        valor=400.0,
        categoria='Entretenimento',
        parcelas=5,
        nome_cartao='ggdesu',
        data=date(2022, 4, 1)
    ))
    system.adicionar_despesa(Despesa(
        desc='pulseiras',
        valor=40.0,
        categoria='Entretenimento',
        parcelas=1,
        nome_cartao='ggdesu',
        data=date(2022, 5, 1)
    ))
    