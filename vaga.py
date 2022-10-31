#criar lista/dicionário de vagas

credenciados = {
    '1': {
        'a': {
            'G1': 'XXX-1111',
            'G2': '',
            'G3': '',
        },
        'b': {
            'B1': 'XXX-2222',
            'B2': '',
        },
        'c': {
            'A1': '',
            'A2': '',
            'A3': '',
        }
    }
}

def selecionar_vaga(escolhaShopping, escolhaLoja): # a função pode receber zero ou mais parâmetros
    escolhaVaga = 0
    while escolhaVaga not in credenciados[escolhaShopping][escolhaLoja]:
        print(credenciados[escolhaShopping][escolhaLoja])
        escolhaVaga = input('Selecione a vaga: ')
        if escolhaVaga in credenciados[escolhaShopping][escolhaLoja].keys():
            print(credenciados[escolhaShopping][escolhaLoja][escolhaVaga])
        elif escolhaVaga not in credenciados[escolhaShopping][escolhaLoja]:
            print("Comando inválido. Escolha um comando correspondente.")
    return escolhaVaga