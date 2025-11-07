# abre o arquivo "estomago.txt" em modo leitura com codificação UTF-8
with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()  # lê todas as linhas em uma lista

# Imprime as primeiras 25 linhas
print("=== PRIMEIRAS 25 LINHAS ===\n")
for i, linha in enumerate(linhas[:25], start=1):
    print(f"{i:02d}: {linha.strip()}")

# Mostra o número total de linhas
num_linhas = len(linhas)
print("\n=== NÚMERO TOTAL DE LINHAS ===")
print(num_linhas)

# Linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print("\n=== LINHA COM MAIOR NÚMERO DE CARACTERES ===")
print(linha_maior.strip())
print(f"(Total de caracteres: {len(linha_maior)})")

# Conta menções aos personagens "Nonato" e "Íria"
import re

texto_completo = "".join(linhas)

# busca insensível a maiúsculas/minúsculas, mas com correspondência exata da palavra
ocorrencias_nonato = len(re.findall(r"\bnonato\b", texto_completo, flags=re.IGNORECASE))
ocorrencias_iria = len(re.findall(r"\bíria\b", texto_completo, flags=re.IGNORECASE))

print("\n=== MENÇÕES AOS PERSONAGENS ===")
print(f"Nonato: {ocorrencias_nonato} vezes")
print(f"Íria: {ocorrencias_iria} vezes")
