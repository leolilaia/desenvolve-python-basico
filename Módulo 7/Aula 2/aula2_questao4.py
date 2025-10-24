def validador_senha(senha):
    # Verifica se tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Verifica se contém pelo menos uma letra maiúscula
    tem_maiuscula = any(c.isupper() for c in senha)

    # Verifica se contém pelo menos uma letra minúscula
    tem_minuscula = any(c.islower() for c in senha)

    # Verifica se contém pelo menos um número
    tem_numero = any(c.isdigit() for c in senha)

    # Verifica se contém pelo menos um caractere especial
    caracteres_especiais = "@#$%&*!_-+="
    tem_especial = any(c in caracteres_especiais for c in senha)

    # Retorna True apenas se todas as condições forem satisfeitas
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial


# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
