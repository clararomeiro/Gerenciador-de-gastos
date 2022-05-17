from io import BytesIO
import matplotlib.pyplot as plt
import base64

from backend.schemas import Despesa


def show_image(despesas: list[Despesa]) -> str:
    info = BytesIO()
    plt.figure(figsize=(10,4))
    plt.gca().yaxis.set_major_formatter('R${x:1.2f}')
    cartoes_disponiveis = list({d.nome_cartao for d in despesas})
    for cartao in cartoes_disponiveis:
        desp = [(d.data, d.valor) for d in despesas if d.nome_cartao == cartao]
        plt.plot(*zip(*desp),  linewidth=3)
    plt.legend(cartoes_disponiveis)
    plt.savefig(info,  format='jpeg')
    info.seek(0)
    return base64.b64encode(info.read()).decode()