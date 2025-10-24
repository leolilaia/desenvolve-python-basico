# Lê a frase digitada pelo usuário
frase = input("Digite uma frase: ")

# Define as vogais
vogais = "aeiouAEIOU"

# Lista para armazenar os índices
indices = []

# Percorre a string letra por letra
for i in range(len(frase)):
    if frase[i] in vogais:
        indices.append(i)

# Exibe os resultados
print("Quantidade de vogais: ", len(indices))
print("Índices: ", indices)