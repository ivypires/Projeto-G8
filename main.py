from shopping import selecionar_shopping
from loja import escolher_loja
from vaga import selecionar_vaga

escolhaShopping = selecionar_shopping()
escolhaLoja = escolher_loja(escolhaShopping)
vaga = selecionar_vaga(escolhaShopping, escolhaLoja)

print(f"Sua vaga é a {vaga}")
