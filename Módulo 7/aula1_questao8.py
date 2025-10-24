import re

def calcular_digito_verificador(digitos: str) -> int:
    """Calcula um dígito verificador (DV) de CPF com base em uma sequência
    de dígitos de entrada."""
    soma = 0
    multiplicadores = range(len(digitos) + 1, 1, -1)
    
    # Usamos zip para parear cada dígito com seu multiplicador
    for digito_str, multiplicador in zip(digitos, multiplicadores):
        soma += int(digito_str) * multiplicador
        
    # Agora, aplicamos a regra do resto
    resto = soma % 11
    
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validar_cpf():
    """Função principal que solicita um CPF, calcula os dígitos verificadores
    e imprime "Válido" ou "Inválido"."""
    
    # 1. Solicita o CPF ao usuário
    cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
    
    # 2. Limpa o CPF, removendo todos os caracteres não numéricos
    cpf_limpo = re.sub(r'[^0-9]', '', cpf_usuario)
    
    # 3. Verifica se o CPF limpo tem exatamente 11 dígitos
    if len(cpf_limpo) != 11:
        print("Inválido")
        return

    # 4. Separa a base de cálculo e os dígitos informados pelo usuário
    base_calculo_9_digitos = cpf_limpo[:9]
    digitos_verificadores_informados = cpf_limpo[9:]
    
    # 5. Calcula o DV1 usando os 9 primeiros dígitos
    dv1_calculado = calcular_digito_verificador(base_calculo_9_digitos)
     
    # 6. A base para o DV2 são os 9 dígitos + o DV1 que acabamos de calcular
    base_calculo_10_digitos = base_calculo_9_digitos + str(dv1_calculado)
    
    # 7. Calcula o DV2
    dv2_calculado = calcular_digito_verificador(base_calculo_10_digitos)
    
    # 8. Formata os dígitos calculados como uma string (ex: "35")
    digitos_verificadores_calculados = f"{dv1_calculado}{dv2_calculado}"
    
    # 9. Compara os dígitos informados com os calculados
    if digitos_verificadores_informados == digitos_verificadores_calculados:
        print("Válido")
    else:
        print("Inválido")

# --- Executa o programa ---
validar_cpf()