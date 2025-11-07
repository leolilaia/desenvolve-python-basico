# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Define as vogais (maiúsculas e minúsculas)
vogais = "aeiouAEIOU"

# Substitui cada vogal por '*'
frase_modificada = ""
for letra in frase:
    if letra in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += letra

# Exibe o resultado
print("Frase modificada:", frase_modificada)
