# Entrada de dados
N = int(input())  # número de experimentos

coelhos = 0
ratos = 0
sapos = 0

# Leitura dos experimentos
for _ in range(N):
    quantia, tipo = input().split()
    quantia = int(quantia)

    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

# Total de cobaias
total = coelhos + ratos + sapos

# Percentuais
perc_coelhos = (coelhos / total) * 100
perc_ratos = (ratos / total) * 100
perc_sapos = (sapos / total) * 100

# Saída
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f} %")
print(f"Percentual de ratos: {perc_ratos:.2f} %")
print(f"Percentual de sapos: {perc_sapos:.2f} %")
