# Solicita o nome ao usuário
nome = input("Digite seu nome: ")

# Exibe o nome em formato de escada
for i in range(1, len(nome) + 1):
    print(nome[:i])
