# Lê o número digitado pelo usuário
numero = input("Digite o número: ")

# Verifica a quantidade de dígitos
if len(numero) == 8:
    # Adiciona o 9 na frente
    numero = "9" + numero
elif len(numero) == 9:
    # Se já tem 9 dígitos, verifica se começa com 9
    if numero[0] != "9":
        print("Número inválido: o primeiro dígito deve ser 9.")
        exit()
else:
    print("Número inválido: deve ter 8 ou 9 dígitos.")
    exit()

# Adiciona o separador "-" após o quinto dígito
numero_formatado = numero[:5] + "-" + numero[5:]

# Exibe o número completo
print("Número completo:", numero_formatado)
