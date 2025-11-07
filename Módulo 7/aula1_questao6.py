# Lê a frase e a palavra objetivo
frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

# Transforma tudo em minúsculas para comparar sem erro
frase = frase.lower()
objetivo = objetivo.lower()

# Quebra a frase em palavras
palavras = frase.split()

# Ordena as letras da palavra objetivo (base de comparação)
objetivo_ordenado = sorted(objetivo)

# Lista para guardar os anagramas encontrados
anagramas = []

# Percorre cada palavra da frase
for palavra in palavras:
    # Ignora se o tamanho for diferente
    if len(palavra) == len(objetivo):
        # Se as letras ordenadas forem iguais, é anagrama
        if sorted(palavra) == objetivo_ordenado:
            anagramas.append(palavra)

# Exibe o resultado
print("Anagramas:", anagramas)
