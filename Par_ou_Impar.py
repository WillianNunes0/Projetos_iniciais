

def parouimpar():
    
    # Input
    numero = input('Digite um numero: ')
   
    # Checagem
    try:
        numero = int(numero)
    except ValueError:
        print('Porfavor digite um número válido! ')
        exit()

    # Resultado
    resultado = numero / 2
    if resultado == 0:
        return 'par'
    else:
        return 'impar'



print(parouimpar())



