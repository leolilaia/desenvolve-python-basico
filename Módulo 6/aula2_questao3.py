import random

# Gera duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Cria a lista de interseção sem duplicatas
intersecao = sorted(list(set(lista1) & set(lista2)))

# Função para contar ocorrências
def contar_ocorrencias(lista, elementos):
    return {x: lista.count(x) for x in elementos}

# Contagem de ocorrências na lista1 e lista2
contagem_lista1 = contar_ocorrencias(lista1, intersecao)
contagem_lista2 = contar_ocorrencias(lista2, intersecao)

# Saída
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção ordenada:", intersecao)
print("Quantidade de vezes que cada elemento aparece em lista1:", contagem_lista1)
print("Quantidade de vezes que cada elemento aparece em lista2:", contagem_lista2)
