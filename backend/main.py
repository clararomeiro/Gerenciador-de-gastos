from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from backend.schemas import Cartao
from backend.controllers import Controlador

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
    return tem.TemplateResponse('despesas.html', {'request': request})


@app.get('/consultas')
def consultas_page(request: Request):
    return tem.TemplateResponse('consultas.html', {'request': request})


@app.post('/add-card')
def add_cartao(cartao: Cartao):
    system.adicionar_cartao(cartao)
    