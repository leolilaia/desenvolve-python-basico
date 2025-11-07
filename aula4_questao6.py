import csv

arquivo_csv = 'spotify-2023.csv'
codificacao = 'latin-1'

# --- 1. Imprimir as cinco primeiras linhas ---
print(f"--- Lendo as 5 primeiras linhas de '{arquivo_csv}' ---")
try:
    with open(arquivo_csv, 'r', encoding=codificacao) as f:
        for i in range(5):
            linha_bruta = f.readline()
            if not linha_bruta: # Caso o arquivo tenha menos de 5 linhas
                break
            print(linha_bruta.strip())
except FileNotFoundError:
    print(f"\nERRO: O arquivo '{arquivo_csv}' não foi encontrado.")
    print("Por favor, baixe o arquivo do Kaggle e salve-o na mesma pasta.")
    exit() 
except Exception as e:
    print(f"Ocorreu um erro ao ler as primeiras linhas: {e}")
    exit()

# --- 2. Processamento principal do arquivo ---
print("\n--- Processando o arquivo... ---")

# Dicionário para guardar a música mais tocada de cada ano
top_musicas_por_ano = {}

anos_desejados = range(2012, 2023) 

try:
    with open(arquivo_csv, 'r', encoding=codificacao) as f:
        
        reader = csv.reader(f)
        
        # Pula a linha do cabeçalho
        try:
            cabecalho = next(reader)
        except StopIteration:
            print("Erro: O arquivo CSV está vazio.")
            exit()

        # Encontra o índice (número) de cada coluna que nos interessa
        try:
            idx_track = cabecalho.index('track_name')
            idx_artist = cabecalho.index('artist(s)_name')
            idx_year = cabecalho.index('released_year')
            idx_streams = cabecalho.index('streams')
        except ValueError as e:
            print(f"Erro: Não foi possível encontrar uma coluna necessária no cabeçalho: {e}")
            print("Verifique se os nomes das colunas estão corretos.")
            exit()

        # Itera por todas as linhas de dados do arquivo
        for linha in reader:
            try:
                if len(linha) <= max(idx_track, idx_artist, idx_year, idx_streams):
                    continue 
                ano = int(linha[idx_year])
                num_streams = int(linha[idx_streams])
                
            except (ValueError, TypeError):
        
                continue 
            
            # Verifica se o ano está no intervalo desejado
            if ano in anos_desejados:
                nome_musica = linha[idx_track]
                artista = linha[idx_artist]

                # Verifica se é a música mais tocada desse ano até agora
                if ano not in top_musicas_por_ano:
                    # Se for a primeira música que encontramos para este ano
                    top_musicas_por_ano[ano] = [nome_musica, artista, num_streams]
                else:
                    # Compara com o recorde atual do ano
                    streams_atuais = top_musicas_por_ano[ano][2]
                    if num_streams > streams_atuais:
                        # Se for maior, substitui
                        top_musicas_por_ano[ano] = [nome_musica, artista, num_streams]

except Exception as e:
    print(f"Ocorreu um erro inesperado durante o processamento do CSV: {e}")
    exit()

# --- 3. Formatação da Saída Final ---
print("\n--- MÚSICAS MAIS TOCADAS DE CADA ANO (2012-2022) ---")

lista_final = []

# Ordena o dicionário por ano para imprimir em ordem
for ano in sorted(top_musicas_por_ano.keys()):
    dados_musica = top_musicas_por_ano[ano] 
    
    nome_musica = dados_musica[0]
    artista = dados_musica[1]
    streams = dados_musica[2]
    
    # Adiciona na lista final no formato exato pedido
    lista_final.append([nome_musica, artista, ano, streams])

# Imprime a lista final formatada
if not lista_final:
    print("Nenhuma música correspondente ao intervalo 2012-2022 foi encontrada.")
else:
    for item in lista_final:
        print(item)
