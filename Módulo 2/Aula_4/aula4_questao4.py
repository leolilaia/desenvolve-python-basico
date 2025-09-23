# Lê o valor inteiro em reais
valor = int(input())

# Calcula quantas notas de 100 cabem
notas100 = valor // 100
valor = valor % 100  # sobra

# Calcula quantas notas de 50 cabem
notas50 = valor // 50
valor = valor % 50

# Calcula quantas notas de 20 cabem
notas20 = valor // 20
valor = valor % 20

# Calcula quantas notas de 10 cabem
notas10 = valor // 10
valor = valor % 10

# Calcula quantas notas de 5 cabem
notas5 = valor // 5
valor = valor % 5

# Calcula quantas notas de 2 cabem
notas2 = valor // 2
valor = valor % 2

# O que sobrar é nota de 1
notas1 = valor

# Exibe o resultado formatado
print(f"{notas100} nota(s) de R$100,00")
print(f"{notas50} nota(s) de R$50,00")
print(f"{notas20} nota(s) de R$20,00")
print(f"{notas10} nota(s) de R$10,00")
print(f"{notas5} nota(s) de R$5,00")
print(f"{notas2} nota(s) de R$2,00")
print(f"{notas1} nota(s) de R$1,00")
