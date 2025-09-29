# Lista de todos os números pares entre 20 e 50
pares = [n for n in range(20, 51) if n % 2 == 0]

#Lista dos quadrados dos valores de 1 a 10
lista = [1, 2, 3, 4, 5,6 ,7 ,8 , 9, 10]
quadrados = [x ** 2 for x in lista]

# Lista dos números de 1 a 100 divisíveis por 7
div = [n for n in range(1, 101) if n % 7 == 0]

#Lista de paridade 
paridade = [
   "par" if n % 2 == 0 else "ímpar"
    for n in range(0, 30, 3)
]

#Resultados
print(f"1. Números Pares (20 a 50): {pares}")
print(f"\n2. Quadrados dos Números (1 a 9): {quadrados}")
print(f"\n3. Números divisíveis por 7: {div}")
print(f"Lista de paridade: {paridade}")