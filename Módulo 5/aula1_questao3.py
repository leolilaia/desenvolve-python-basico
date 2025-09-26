#Biblioteca
import random

#Geração do número aleatório
valor = random.randint(0, 10)

#Adivinhação
while True:
    n = int(input("Adivinhe o número entre 1 e 10: "))
    if n == valor:
        print(f"Correto! O número é {n}")
        break
    elif n > valor:
        print("Muito alto, tente novamente! ")
    elif n < valor:
        print("Muito baixo, tente novamente!")