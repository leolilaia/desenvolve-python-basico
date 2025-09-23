#Função que permite a entrada do valor em Fahrenheit
F = int(input("Insira um valor em Fahrenheit: "))

#converte o valor de Fahrenheit para Celsius
C = int((F - 32) * (5/9))

#imprime o resultado
print(f"{F} Fahrenheit são {C} graus Celsius.")

