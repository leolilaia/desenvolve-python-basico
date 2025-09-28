import random

#Cria a lista com 20 números aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:", lista)

#Encontrar o intervalo com maior número de valores negativos consecutivos
maior_inicio = maior_fim = 0
inicio = 0

for i in range(len(lista)):
    if lista[i] < 0:
        #se o número for negativo, continua o intervalo
        continue
    else:
        #quando encontra um número não negativo, verifica o tamanho do intervalo anterior
        fim = i
        negativos = lista[inicio:fim]
        if len(negativos) > 0 and all(x < 0 for x in negativos):
            if (fim - inicio) > (maior_fim - maior_inicio):
                maior_inicio, maior_fim = inicio, fim
        inicio = i + 1

#trata o caso de o intervalo negativo ir até o fim da lista
if inicio < len(lista) and all(x < 0 for x in lista[inicio:]):
    if (len(lista) - inicio) > (maior_fim - maior_inicio):
        maior_inicio, maior_fim = inicio, len(lista)

#Deleta o intervalo com mais números negativos
if maior_fim > maior_inicio:
    del lista[maior_inicio:maior_fim]

#Exibe o resultado
print("Lista editada:", lista)
