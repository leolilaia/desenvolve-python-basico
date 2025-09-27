# Função para ler uma lista do usuário
def ler_lista(n, numero_lista):
    lista = []
    print(f"Digite os {n} elementos da lista {numero_lista}:")
    for i in range(n):
        elemento = int(input())
        lista.append(elemento)
    return lista

# Recebe o tamanho das listas
n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = ler_lista(n1, 1)

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = ler_lista(n2, 2)

# Cria a lista intercalada
intercalada = []
min_len = min(len(lista1), len(lista2))

# Intercala até o fim da menor lista
for i in range(min_len):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i])

# Adiciona os elementos restantes da maior lista
if len(lista1) > min_len:
    intercalada.extend(lista1[min_len:])
elif len(lista2) > min_len:
    intercalada.extend(lista2[min_len:])

# Saída
print("Lista intercalada:", ' '.join(map(str, intercalada)))
