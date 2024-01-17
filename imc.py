# Calculadora IMC (Índice de Massa Corpórea)

altura = float(input("digite sua altura em m: "))
peso = int(input("digite seu peso em kg: "))
imc = peso / altura**2

linha_1 = f'Você tem {altura:.2f} metros de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.4f}'

print(linha_1)
print(linha_2)
print(linha_3)