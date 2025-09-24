#Entrada de dados
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

#soma os números
soma = n1 + n2

#Verifica e imprime se a soma é par ou ímpar
if soma % 2 == 0:
    print("A soma é par")
else:
    print("A soma é ímpar")
