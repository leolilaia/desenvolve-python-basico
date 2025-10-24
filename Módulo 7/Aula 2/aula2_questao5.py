import random

def embaralhar_palavras(frase):
    palavras = frase.split()  # separa a frase em palavras
    resultado = []

    for palavra in palavras:
        # Se a palavra tiver menos de 4 letras, não precisa embaralhar
        if len(palavra) <= 3:
            resultado.append(palavra)
        else:
            # Mantém o primeiro e o último caractere fixos
            meio = list(palavra[1:-1])
            random.shuffle(meio)  # embaralha as letras internas
            nova_palavra = palavra[0] + ''.join(meio) + palavra[-1]
            resultado.append(nova_palavra)

    # Junta tudo de volta em uma frase
    return ' '.join(resultado)


# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
