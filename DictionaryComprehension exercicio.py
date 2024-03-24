# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10% V
# Gere novos_produtos por deep copy (cópia profunda) V 
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [
    {
    'nome': produto['nome'],
    'preco' : round(produto['preco']*1.10,2) 
    }
    for produto 
    in produtos
]

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(key = lambda x:x['nome'], reverse=True)

produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco.sort(key=lambda x:x['preco'])

for i in produtos_ordenados_por_preco:
    print(i)

