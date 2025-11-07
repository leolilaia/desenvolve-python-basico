import re  # para usar expressões regulares

# Lê o conteúdo do arquivo "frase.txt"
with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Usa regex para manter apenas palavras (letras e acentos)
palavras = re.findall(r"[A-Za-zÀ-ÿ]+", conteudo)

# Salva cada palavra em uma nova linha no arquivo "palavras.txt"
with open("palavras.txt", "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Lê e imprime o conteúdo de "palavras.txt"
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
