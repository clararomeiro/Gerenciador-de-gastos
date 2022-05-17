from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from backend.schemas import Cartao, Despesa
from backend.controllers import Controlador
from datetime import date


system = Controlador()

tem = Jinja2Templates('frontend')

app = FastAPI()

app.mount('/frontend',
    StaticFiles(directory='frontend/'),
    name="static"
)

@app.get('/')
def home_page(request: Request):
    return tem.TemplateResponse('cartoes.html', {
        'request': request,
        'cartoes': system.cartoes
    })


@app.get('/despesas')
def despesas_page(request: Request):
    return tem.TemplateResponse('despesas.html', {
        'request': request,
        'cartoes': system.cartoes
    })


@app.get('/consultas')
def consultas_page(request: Request,
    cartao: str | None = None,
    data_ini: date = date.min,
    data_fim: date = date.max
):
    despesas = system.listar_despesas(cartao, data_ini, data_fim)
    return tem.TemplateResponse('consultas.html', {
        'request': request,
        'cartoes': system.cartoes,
        'despesas': despesas
    })


@app.post('/add-card')
def add_cartao(cartao: Cartao):
    system.adicionar_cartao(cartao)


@app.delete('/remove-card')
def remove_cartao(nome: str):
    system.remover_cartao(nome)
    return 'removido com sucesso'


@app.post('/add-despesa')
def add_despesa(despesa: Despesa):
    system.adicionar_despesa(despesa)


@app.get('/list-despesas', response_model=list[Despesa])
def listar_despesas(
    nome_cartao: str | None = None,
    data_inicio: date = date.min,
    data_fim: date = date.max
) -> list[Despesa]:
    return system.listar_despesas(nome_cartao, data_inicio, data_fim)


