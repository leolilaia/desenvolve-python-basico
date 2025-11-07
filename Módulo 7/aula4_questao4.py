import random
import os 

def carregar_palavras(arquivo="gabarito_forca.txt"):
    """Lê o arquivo de palavras e retorna uma palavra aleatória."""
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            palavras = [linha.strip().lower() for linha in f]
            if not palavras:
                print(f"Erro: O arquivo '{arquivo}' está vazio.")
                return None
            return random.choice(palavras)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        print("Por favor, crie-o com uma palavra por linha.")
        return None

def carregar_estagios_enforcado(arquivo="gabarito_enforcado.txt"):
    """Lê o arquivo com os estágios do enforcado e retorna uma lista."""
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            # Lê o conteúdo todo e divide por linhas em branco (\n\n)
            estagios = f.read().split('\n\n')
            estagios_limpos = [e for e in estagios if e.strip()]
            if len(estagios_limpos) != 7:
                print(f"Aviso: O arquivo '{arquivo}' não parece ter 7 estágios.")
                print("Verifique se cada estágio está separado por UMA linha em branco.")
            return estagios_limpos
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        print("Por favor, crie-o com os desenhos do enforcado.")
        return None

def imprime_enforcado(erros, estagios):
    """Imprime o estágio do enforcado correspondente ao número de erros."""
    if erros < len(estagios):
        print(estagios[erros])
    else:
        # Garante que sempre imprima o último estágio em caso de erro
        print(estagios[-1])

def limpar_tela():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def jogar():
    """Função principal que executa o jogo."""
    
    palavra_secreta = carregar_palavras()
    estagios_enforcado = carregar_estagios_enforcado()

    # Se os arquivos não puderam ser lidos, encerra o jogo.
    if not palavra_secreta or not estagios_enforcado:
        return

    # Inicializa as variáveis do jogo
    letras_descobertas = ['_'] * len(palavra_secreta)
    letras_tentadas = set()
    erros = 0
    max_erros = 6 
    
    limpar_tela()
    print("--- BEM-VINDO AO JOGO DA FORCA! ---")

    while True:
        # 1. Mostra o status atual
        imprime_enforcado(erros, estagios_enforcado)
        print("\nPalavra: " + " ".join(letras_descobertas))
        if letras_tentadas:
            print("Letras tentadas: " + ", ".join(sorted(letras_tentadas)))

        # 2. Verifica condição de vitória
        if "_" not in letras_descobertas:
            print("\nPARABÉNS! Você descobriu a palavra!")
            print(f"A palavra era: {palavra_secreta}")
            break

        # 3. Verifica condição de derrota
        if erros >= max_erros:
            print("\nVOCÊ FOI ENFORCADO!")
            print(f"A palavra secreta era: {palavra_secreta}")
            imprime_enforcado(max_erros, estagios_enforcado)
            break

        # 4. Pede uma letra ao jogador
        tentativa = input("\nDigite uma letra: ").lower().strip()

        # 5. Valida a entrada
        limpar_tela()
        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Entrada inválida. Por favor, digite apenas UMA letra.")
            continue
        
        if tentativa in letras_tentadas:
            print(f"Você já tentou a letra '{tentativa}'. Tente outra.")
            continue

        # 6. Processa a tentativa
        letras_tentadas.add(tentativa)

        if tentativa in palavra_secreta:
            print(f"Bom palpite! A letra '{tentativa}' está na palavra.")
            # Atualiza os underscores
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == tentativa:
                    letras_descobertas[i] = tentativa
        else:
            print(f"Que pena! A letra '{tentativa}' não está na palavra.")
            erros += 1

# --- Inicia o jogo ---
if __name__ == "__main__":
    jogar()