# Numero Par ou Impár

numero = input('digite um numero : ')
try:
    numero_int = int(numero)
except:
    print('por favor, digite um numero inteiro :)')
    exit()
    
resultado = numero_int % 2
if resultado != 0:
    print(f'{numero_int} é um número impár')
else:
    print(f'{numero_int} é um número par')