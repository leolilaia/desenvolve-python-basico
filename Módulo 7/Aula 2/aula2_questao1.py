# Solicita a data de nascimento
data = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Separa dia, mês e ano
dia, mes, ano = data.split("/")

# Lista com os meses por extenso
meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Converte o mês para o nome correspondente
mes_extenso = meses[int(mes) - 1]

# Exibe a data formatada
print(f"Você nasceu em {int(dia)} de {mes_extenso.capitalize()} de {ano}.")
