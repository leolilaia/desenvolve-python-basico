import string  # para remover pontuação facilmente

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')

    # Verifica se o usuário deseja encerrar
    if frase.lower() == "fim":
        break

    # Remove espaços e pontuações, e converte para minúsculas
    frase_limpa = frase.lower()
    frase_limpa = "".join(ch for ch in frase_limpa if ch.isalnum())  # mantém apenas letras e números

    # Verifica se é palíndromo
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é palíndromo\n')
    else:
        print(f'"{frase}" não é palíndromo\n')
