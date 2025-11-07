import os

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Define o nome do arquivo
nome_arquivo = "frase.txt"

# Abre o arquivo no mesmo diretório do script e escreve a frase
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Obtém o caminho completo do arquivo salvo
caminho_completo = os.path.abspath(nome_arquivo)

# Exibe o caminho completo
print(f"Frase salva em {caminho_completo}")
