import random

def encrypt(nomes: list[str]) -> tuple[list[str], int]:
    '''Criptografa uma lista de strings usando a cifra de César com uma chave
    aleatória entre 1 e 10.'''

    
    # 1. Gere a chave de criptografia aleatória entre 1 e 10
    chave_aleatoria = random.randint(1, 10)
    
    # Defina o intervalo de caracteres visíveis (33 a 126)
    MIN_CHAR = 33
    MAX_CHAR = 126
    INTERVALO_TAMANHO = MAX_CHAR - MIN_CHAR + 1 # O tamanho total do intervalo (94)
    
    nomes_criptografados = []
    
    # 2. Itere sobre cada nome na lista
    for nome in nomes:
        nome_criptografado = ""
        
        # Itere sobre cada caractere do nome
        for char in nome:
            # Obtenha o valor Unicode do caractere
            original_ord = ord(char)
            
            # Verifique se o caractere está no intervalo visível
            if MIN_CHAR <= original_ord <= MAX_CHAR:
                novo_ord = (original_ord - MIN_CHAR + chave_aleatoria) % INTERVALO_TAMANHO + MIN_CHAR
                
                # Converta o novo valor Unicode de volta para o caractere
                char_criptografado = chr(novo_ord)
            else:
                char_criptografado = char
            
            nome_criptografado += char_criptografado
        
        nomes_criptografados.append(nome_criptografado)
        
    # 3. Retorne a lista de nomes criptografados e a chave
    return nomes_criptografados, chave_aleatoria


nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

# Chamada da função
nomes_cript, chave = encrypt(nomes)

print(f"Lista de Nomes Originais: {nomes}")
print(f"Chave de Criptografia Gerada: {chave}")
print(f"Nomes Criptografados: {nomes_cript}")
