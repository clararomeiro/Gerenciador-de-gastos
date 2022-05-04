# Gerenciador-de-gastos
Repositório criado para o projeto da disciplina engenharia de software.


## Backend

Após a instalação do python é recomendável criar um ambiente virtual, que pode ser feito da seguinte forma


**Windows**

    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r requirements.txt

**Linux**

    python -m venv .venv
    source .venv/bin/activate   
    pip install -r requirements.txt


### Teste

    python test.py

### Iniciando servidor
    uvicorn --port 8000 --reload backend.main:app

Agora é só acessar o link http://localhost:8000
