#Biblioteca
import math

#Entrada de dados
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

#Cáculo da diferença absoluta
diferenca = abs(n1 - n2)

#Arredondamento para duas casas decimais
resultado = round(diferenca, 2)

#Saída
print(f"A diferença absoluta entre esses números é: {resultado}")

