#Entrada de dados
distancia = int(input("Digite a distância(em km): "))
peso = int(input("Digite o peso(em kg): "))

#Calcula o frete
if distancia <= 100:
    frete = 1 * peso
elif distancia <= 300:
    frete = 1.50 * peso
else:
    frete = 2 * peso

#Adiciona a taxa se o peso for maior que 10 kg
    if peso > 10:
        frete += 10

#Imprime o resultado
print("O valor do frete é: R$", frete)