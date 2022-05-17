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


function add_cartao() {
    var nome =  document.getElementById('nome');
    var limite =  document.getElementById('limite');
    var bandeira =  document.getElementById('bandeira');
    var dia_vencimento =  document.getElementById('dia_vencimento');

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

    alert('Cartão adicionado com sucesso!');
}

function remove_cartao(nome) {
    fetch(`/remove-card?nome=${nome}`, {method: 'DELETE'});
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

    alert('Despesa adicionada com sucesso!')
}

function list_despesas(){
    data_ini = document.getElementById('data_ini');
    data_fim = document.getElementById('data_fim');

    fetch('/list-despesas' , {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({
            data_ini: data_ini.value,
            data_fim: data_fim.value
        })
    }).then(res => res.json()).then((res) => {
        console.log(res)
    });

}