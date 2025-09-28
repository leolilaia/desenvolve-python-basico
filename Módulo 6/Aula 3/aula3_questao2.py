# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Cria uma nova lista com o nome principal de cada domínio usando fatiamento
dominios = [url[4:-4] for url in urls]

# Exibe o resultado
print("URLs:", urls)
print("dominios:", dominios)
