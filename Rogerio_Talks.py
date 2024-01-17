# Rogério Talks

import time

inicio_manha = 5
termino_manha = 11
inicio_tarde = 13
termino_tarde = 18
inicio_noite = 19
termino_noite = 23
inicio_madruga = 0
termino_madruga = 4

print('"Um bebâdo se aproxima"')
time.sleep(1)
nome = input('Qual o seu nome Netflixo ? ')
time.sleep(1)
print(f'hmmm que nome bosta hein {nome}')
time.sleep(1)
horas = input('Desculpe a grosseria ,o álcool já me subiu a cabeça poderia informar-me as horas por obsequio: ')

try:
    horas_int = int(horas)
except:
    time.sleep(1)
    print('Desculpe ,suas palavras fogem do meu entendimento "use numeros inteiros ex:12"')
    time.sleep(1)
    print('"O bebâbo vai embora"')
    exit()

# Manhã
if inicio_manha<=horas_int<=termino_manha:
    print(f'bom dia {nome}')
    time.sleep(1)
    print('"O bebâbo vai embora"')
# Meio-Dia
elif horas_int == 12:
    time.sleep(0.5)
    print('que legal ,já pode almossar ? ')
    time.sleep(1)
    ralmossar = input('"Sim ou não" ')
    if ralmossar in ['Sim', 'S', 'sim', 's', 'já', 'ja', 'claro' ,'pode']:
        time.sleep(1)
        print('obrigado :)')
        time.sleep(1)
        print('"O bebâbo vai embora"')
    else :
        time.sleep(1)
        print('"O bebâdo joga uma marmitex em sua cara ,você se engasga com os restos e morre"')
# Tarde
elif inicio_tarde<=horas_int<=termino_tarde:
    time.sleep(1)
    print(f'boa tarde {nome}')
    time.sleep(1)
    print('"O bebâbo vai embora"')
# Noite
elif inicio_noite<=horas_int<=termino_noite:
    print(f'boa noite {nome}')
    time.sleep(1)
    print('"O bebâbo vai embora"')
# Madruga
elif inicio_madruga<=horas_int<=termino_madruga:
    time.sleep(1)
    print(f'Está tarde não acha {nome} ?')
    time.sleep(1)
    rmadruga = input('"Sim ou Não ?" ')
    if rmadruga in ['Sim', 'S', 'sim', 's', 'já', 'ja', 'esta' ,'está']:
        time.sleep(1)
        print('Rogério "O bebâdo" dorme na calçada')
        time.sleep(1)
        print('"Você vai embora"')
        exit()
    else:
        print('"O bebâdo discorda de sua afirmação e fica irritado"')
        time.sleep(1)
        print('"Ele o bate com uma garrafa da whisky e você fica desacordado"')
        exit()
elif horas_int == 24:
    print('"não existe hora 24 seu burro !"')

...
        