from datetime import datetime
from app.controllers import Controlador
from app.models import Cartao, Despesa


def main():
    cont = Controlador()
    cartao = Cartao(
        id=10,
        nome='cartao1',
        bandeira='bandeira',
        dia_vencimento=10,
        limite=200.0,
        lembrete=False
    )

    despesa = Despesa(
        id = 0,
        nome = 'bla',
        desc = 'blabla',
        valor = 15.0,
        categoria = 'pi',
        parcelas = 3,
        id_cartao = 10,
        data = datetime.now()
    )
    cont.adicionar_cartao(cartao)
    cont.adicionar_despesa(despesa)

    print('Cartões:', cont.cartoes)
    print('Despesas:', cont.despesas)

if __name__ == '__main__':
    main()



