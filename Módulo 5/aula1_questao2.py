#Bibliotecas
import random
import math

#Entrada de dados
n = int(input("Digite a quantidade de valores aleatórios a serem gerados: "))

#Geração de números e soma
soma = 0
for _ in range(n):
    valor = random.randint(0, 100)
    print("Valor gerado: ", valor)
    soma += valor

#Cálculo da raiz quadrada da soma
raiz = math.sqrt(soma)

#Saída
print("\nSoma dos valores: ", soma)
print("Raiz quadrada da soma: ", round(raiz, 2))