# Validador de cpf


# Primeiro digito do cpf

contador_regressivo_1 = 10
etapa_p1 = 0


cpf_do_usuario = input('Digite o CPF: ')\
    .replace('.' ,'')\
    .replace('-' ,'')\
    .replace(' ' ,'')\

teste_repetividade = cpf_do_usuario \
== cpf_do_usuario[0] * len(cpf_do_usuario) 

if teste_repetividade:
    print('Porfavor não envie dados repetidos')
    exit()

cpf_9dig = cpf_do_usuario[:9]

for digito in cpf_9dig:
    etapa_p1 += ( int(digito) * contador_regressivo_1 )
    contador_regressivo_1 -= 1

etapa_p2 = etapa_p1 * 10

etapa_p3 = etapa_p2 % 11

digito1 = (0 if etapa_p3 > 9 else etapa_p3)


# Segundo digito do cpf

contador_regressivo_2 = 11
etapa_s1 = 0

cpf_10dig = cpf_9dig + str(digito1)


for digito in cpf_10dig:
    etapa_s1 += ( int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1

etapa_s2 = etapa_s1 * 10

etapa_s3 = etapa_s2 % 11

digito2 = (0 if etapa_s3 > 9 else etapa_s3)

# Verificando se o cpf é válido

novo_cpf = f'{cpf_9dig}{digito1}{digito2}'

if novo_cpf == cpf_do_usuario:
    print(f'"{cpf_do_usuario}" é um CPF válido')
else:
    print(f'"{cpf_do_usuario}" não é um CPF válido')