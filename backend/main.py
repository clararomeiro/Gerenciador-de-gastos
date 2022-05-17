from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from backend.schemas import Cartao, Despesa
from backend.controllers import Controlador

from datetime import datetime as date

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
def consultas_page(request: Request):
    return tem.TemplateResponse('consultas.html', {
        'request': request,
        'despesas': system.despesas
    })


@app.post('/add-card')
def add_cartao(cartao: Cartao):
    system.adicionar_cartao(cartao)

@app.post('/add-despesa')
def add_despesa(despesa: Despesa):
    system.adicionar_despesa(despesa)
    

@app.get('/list-despesas')
def list_despesas(data_inicio: date, data_fim:date):
    return tem.TemplateResponse('consultas.html', {
        'request': request,
        'despesas': system.listar_despesas(data_inicio, data_fim)
    })