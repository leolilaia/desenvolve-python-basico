# --- Lista de 10 livros para o exercício ---

lista_de_livros = [
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "1997", "263"),
    ("Harry Potter e a Câmara Secreta", "J.K. Rowling", "1998", "287"),
    ("Harry Potter e o Prisioneiro de Azkaban", "J.K. Rowling", "1999", "348"),
    ("A Sociedade do Anel", "J.R.R. Tolkien", "1954", "608"),
    ("As Duas Torres", "J.R.R. Tolkien", "1954", "464"),
    ("O Retorno do Rei", "J.R.R. Tolkien", "1955", "528"),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "1943", "96"),
    ("Um Estudo em Vermelho", "Arthur Conan Doyle", "1887", "176"),
    ("O Signo dos Quatro", "Arthur Conan Doyle", "1890", "176"),
    ("O Cão dos Baskerville", "Arthur Conan Doyle", "1902", "198"),
    ("O Vale do Medo", "Arthur Conan Doyle", "1915", "224")
]

nome_arquivo = "meus_livros.csv"

try:
    # Abre o arquivo no modo 'w' (write - escrita)
    # O encoding='utf-8' garante que acentos (ç, ã, é) sejam salvos corretamente
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        
        # 1. Escreve a linha do cabeçalho
        cabecalho = "Título,Autor,Ano de publicação,Número de páginas\n"
        f.write(cabecalho)
        
        # 2. Escreve cada livro da lista no arquivo
        for livro in lista_de_livros:
            linha = ",".join(livro)
            
            # Escreve a linha do livro e adiciona a quebra de linha
            f.write(linha + "\n")

    print(f"Sucesso! O arquivo '{nome_arquivo}' foi criado.")
    print("Abra-o no Google Sheets ou Excel para ver o resultado.")

except Exception as e:
    print(f"Ocorreu um erro ao tentar escrever o arquivo: {e}")