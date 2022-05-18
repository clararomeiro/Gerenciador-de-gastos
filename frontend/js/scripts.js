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
    window.location.reload();
}

function remove_cartao(nome) {
    if (!confirm('Remover este cartão apagará também todas as despesas associadas ao cartão, proceguir?'))
        return;
    fetch(`/remove-card?nome=${nome}`, {method: 'DELETE'});
    window.location.reload();
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

function atualizar_consulta(){
    var url = '/consultas?';
    var param = [];
    
    if (cartao.value !== "Todos")
        param.push('cartao=' + cartao.value);

    if (data_ini.value)
        param.push('data_ini=' + data_ini.value);

    if (data_fim.value)
        param.push('data_fim=' + data_fim.value);
    
    url += param.join('&');

    window.location.assign(url);
}