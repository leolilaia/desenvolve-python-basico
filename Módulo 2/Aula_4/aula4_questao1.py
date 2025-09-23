#função que permite a entrada para o valor do comprimento
comprimento = int(input("Insira o comprimento do lote: "))

#função que permite a entrada para o valor da largura
largura = int(input("Insira a largura do lote: "))

#função que permite a entrada para o valor do preço do metro quadrado
preco_m2 = float(input("Insira o preço do metro quadrado: "))

# caulcula a área do terreno
area_m2 = comprimento * largura  

#calcula o valor do terreno
preco_total = preco_m2 * area_m2

#imprime o resultado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")

