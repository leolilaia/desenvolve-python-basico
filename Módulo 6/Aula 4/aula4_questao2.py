import string

#Solicita a frase ao usuário
frase_original = input("Digite uma frase: ")

#Define o conjunto de caracteres para filtragem
VOGAIS = "aeiou"
TODAS_LETRAS = set(string.ascii_lowercase)
CONSOANTES_SET = TODAS_LETRAS - set(VOGAIS)


## Geração das Listas Usando Compreensão

#Lista de Vogais (ordenada)
vogais_lista = [char.lower() for char in frase_original if char.lower() in VOGAIS]
#Ordena a lista
vogais_lista.sort()

#Lista de Consoantes
consoantes_lista = [char for char in frase_original if char.lower() in CONSOANTES_SET]


#Resultados
print("-" * 40)
print(f"Frase digitada: {frase_original}")
print("-" * 40)
print(f"Vogais (ordenadas): {vogais_lista}")
print(f"Consoantes: {consoantes_lista}")
