# Lista de compras

import time 
import os
lista = []
print('Crie a sua lista de compras,')

while True :
    
    # Input
    print('selecione uma opção: ')
    opcao_escolhida = input('[L]istar ,[C]riar ,[A]pagar : ').lower()
    
    # Listar
    if opcao_escolhida == 'l':
        os.system('cls')
        print('Está é sua lista até agora:')
        for indice ,produto in enumerate(lista):
            print(f'{indice}-->{produto}')
        time.sleep(1)
    
    # Criar
    elif opcao_escolhida == 'c':
        os.system('cls')
        produto_acrescentado = input('Produto que deseja acrescentar: ')
        lista.append(produto_acrescentado)


    # Apagar
    elif opcao_escolhida == 'a': 
        os.system('cls')
        try:
            indice_removido = int(input('índice que deseja remover: '))
            del lista[indice_removido]
            print(f'você deletou o indice "{indice_removido}"')
        except:
            print('Porfavor selecione um indice válido! ')
    else:
        print('Digite uma opção válida')
        time.sleep(1)
        os.system('cls')
    