# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
cidades = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1,l2):
    tamanho = min(len(l1),len(l2))
    return [
        (l1[i],l2[i])for i in range(tamanho)
    ]
    
print(zipper(estados,cidades))



