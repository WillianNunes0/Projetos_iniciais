# Palavra Secreta
import os

palavra_secreta = 'abacaxi'
letras_acertadas = ''
tentativas = 0

while True:
    

    tentativas =+ 1

    letra_digitada = input('Digite uma letra: ')
    

    if len(letra_digitada) > 1:
        print('digite apenas uma letra')
        continue
    
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'     
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabens você acertou a palavra secreta')
        print(f'Você teve {tentativas} tentativas')
        break




    
    