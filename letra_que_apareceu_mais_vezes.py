frase = input('Digite o seu texto: ').lower()

letra_atual = ''
qtd_apareceu_mais_vezes = 0
qtd_apareceu_mais_vezes_atual = 0
letra_que_apareceu_mais_vezes = ''
letra_que_apareceu_mais_vezes_atual = ''
i = 0

while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1
print(f'{letra_que_apareceu_mais_vezes} foi a letra de maior recorrência em seu texto (apareceu {qtd_apareceu_mais_vezes})')