from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


tem = Jinja2Templates('frontend')

app = FastAPI()

app.mount('/frontend',
    StaticFiles(directory='frontend/'),
    name="front"
)

@app.get('/')
def home_page(request: Request):
    return tem.TemplateResponse('index.html', {'request': request})


@app.get('/despesas')
def despesas_page(request: Request):
    return tem.TemplateResponse('despesas.html', {'request': request})


@app.get('/consultas')
def consultas_page(request: Request):
    return tem.TemplateResponse('consultas.html', {'request': request})