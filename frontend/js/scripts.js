class Cartao {
    constructor() {
        this.nome
        this.bandeira
        this.vencimento
        this.valor
    }
    
    adicionar() {
        alert('Cartão adicionado com sucesso!');
    }

    adicionarDespesa(){
        alert('Despesa adicionada com sucesso!')
    }
}

var cartao = new Cartao();

function add_cartao() {
    nome =  document.getElementById('nome');
    limite =  document.getElementById('limite');
    bandeira =  document.getElementById('bandeira');
    dia_vencimento =  document.getElementById('dia_vencimento');

    fetch('/add-card' , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({
            nome: nome.value,
            limite: limite.value,
            bandeira: bandeira.value,
            dia_vencimento: dia_vencimento.value
        })
    }).then(res => res.json()).then((res) => {
        console.log(res)
    });
}

function add_despesa() {
    valor = document.getElementById('valor');
    desc = document.getElementById('descricao');
    parcelas = document.getElementById('parcelas');
    data =  document.getElementById('data');
    nome_cartao = document.getElementById('cartao');
    categoria = document.getElementById('categoria');

    fetch('/add-despesa' , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({
            valor: valor.value,
            desc: desc.value,
            parcelas: parcelas.value,
            data: data.value,
            nome_cartao: nome_cartao.value,
            categoria: categoria.value
        })
    }).then(res => res.json()).then((res) => {
        console.log(res)
    });
}