import random

# Gera 1 número entre 5 e 20
num_elementos = random.randint(5, 20)

# Cria a lista com num_elementos valores entre 1 e 10 
elementos= [random.randint(1, 10) for _ in range(num_elementos)]


#Calcula a soma e a média da lista
soma = sum(elementos)
media = soma/num_elementos

print(f"Lista de elementos: {elementos}")
print(f"A soma dos valores da lista é: {soma}")
print(f"A média dos valores da lista é: {media}")
