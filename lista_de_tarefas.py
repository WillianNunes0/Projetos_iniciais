# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# Lista de tarefas
import json
lista_main = []

while True:
    # Salvando em JSON
    with open('lista_de_tarefs.json', 'w' ,encoding='utf8') as arquivo:
        json.dump(
            lista_main,
            arquivo,
                 )

    # Entrada
    print('Digite uma tarefa para adicionar ou um comando')
    Entrada = input('Os comandos são: Listar , Desfazer ou Refazer: ')
    Entrada = Entrada.lower()
    
    # Adicionando tarefas
    if Entrada not in ['listar' ,'desfazer' ,'refazer']:
        lista_main.append(Entrada)

    #listar
    elif Entrada == 'listar':
        for i in lista_main:
            print(i)
        if not lista_main:
            print('nenhuma tarefa na lista')
            continue
    
    # Defazer 
    elif Entrada == 'desfazer':
        if not lista_main:
            print('nenhuma tarefa a ser desfeita lista')
            continue
        backup_refazer = lista_main.pop()
        print(f'tarefa "{backup_refazer}" removida da lista de tarefas')

    # Refazer
    elif Entrada == 'refazer':
        try: 
            lista_main.append(backup_refazer)
        except:
            print('nenhuma ação a ser refeita')
            continue
        if not lista_main:
            print('nenhuma tarefa a ser refeita na lista')
        print(f'tarefa "{backup_refazer}" adicionada a lista de tarefas')



        
    

    
    
    