# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respsostas_certas = 0


for pergunta in perguntas:
    
    print('Pergunta: ', pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
     print(f'{i}) {opcao}')
    
    print()
    escolha_do_usuario = input('Escolha uma opção: ')
    
    escolha_do_usuario_int = 0
    qtd_opcoes = len(opcoes)
    
    if escolha_do_usuario.isdigit():
       escolha_do_usuario_int = int(escolha_do_usuario)
    else:
       print('Digite um Número Válido')
       break

    if escolha_do_usuario_int >= 0 and escolha_do_usuario_int < qtd_opcoes:
        if opcoes[escolha_do_usuario_int] == pergunta['Resposta']:
           print('Você acertou ✅')
           respsostas_certas += 1
        else:
            print('Você errou ❌')
    else:
       print('Você digitou uma opção inexistente')
       break

print(f'Você acertou {respsostas_certas} peguntas de 3 perguntas')
