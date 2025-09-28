numeros = []

print("Digite números inteiros (digite 'fim' para encerrar):")

# Leitura dos valores
while True:
    valor = input("Número: ")
    if valor.lower() == "fim":
        break
   
    numeros.append(int(valor))

# Verifica se há pelo menos 4 valores
if len(numeros) < 4:
    print("\nVocê deve digitar pelo menos 4 números!")
else:
    print("\n--- Resultados ---")
    print("Lista original:", numeros)
    print("3 primeiros elementos:", numeros[:3])
    print("2 últimos elementos:", numeros[-2:])
    print("Lista invertida:", numeros[::-1])
    print("Elementos de índice par:", numeros[::2])
    print("Elementos de índice ímpar:", numeros[1::2])
