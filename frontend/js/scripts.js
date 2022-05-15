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