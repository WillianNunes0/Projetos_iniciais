# Calculadora - Simples

import os
print('Bem vindo a calculadora')

while True :
    

    # Input do usuario
    
    numero1 =  input ('Digite um número: ')
    numero2 =  input ('Digite outro número: ')
    operador = input ('Digite um operador apenas(+-/*) : ')

    # Checando se o Numero é válido
    
    n1_float = 0
    n2_float = 0

    try:
         n1_float = float(numero1)
         n2_float = float(numero2) 
    except:
        print('Porfavor digite um número válido')
        continue
    
    
    # Checando se o Operador é válido

    operadores_validos = '+-/*'

    if len(operador) > 1:
        print('Porfavor digite apenas um operador')
        continue 
    elif operador not in operadores_validos:
        print('Porfavor digite um operador válido')
        continue

    # Operações
    
    if operador == '-':
        os.system('cls')
        print(f'O valor de {n1_float} - {n2_float} é: {n1_float - n2_float}')
    elif operador == '+':
        os.system('cls')
        print(f'O valor de {n1_float} + {n2_float} é: {n1_float + n2_float}')
    elif operador == '/':
        try:
            os.system('cls')
            print(f'O valor de {n1_float} ÷ {n2_float} é: {n1_float / n2_float}')
        except:
            os.system('cls')
            print('não existe divisão por 0')
            continue
    elif operador == '*':
        os.system('cls')
        print(f'O valor de {n1_float} * {n2_float} é: {n1_float * n2_float}')

    # Sair da calculadora
    
    sair = input('deseja fechar a calculadora ? ')
    sair = sair.lower()
    sair = sair.startswith('s')
    if sair:
         break  

print('você fechou a calculadora')