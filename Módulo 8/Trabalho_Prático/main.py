import csv
import getpass
import hashlib
import os
import sys
from typing import List, Dict, Set, Tuple, Union

# --- Constantes ---
ARQUIVO_USUARIOS = 'usuarios.csv'
ARQUIVO_PRODUTOS = 'produtos.csv'
ROLES_VALIDAS: Set[str] = {'gerente', 'tecnico'}

# --- Funções de Utilidade (Segurança) ---

def hash_senha(senha: str) -> str:
    """
    Gera um hash SHA-256 para a senha fornecida.

    Entrada:
        senha (str): A senha em texto plano.

    Saída:
        str: O hash da senha em formato hexadecimal.
    """
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_senha(senha_hash_armazenada: str, senha_fornecida: str) -> bool:
    """
    Verifica se a senha fornecida corresponde ao hash armazenado.

    Entradas:
        senha_hash_armazenada (str): O hash salvo no arquivo.
        senha_fornecida (str): A senha em texto plano digitada pelo usuário.

    Saída:
        bool: True se as senhas corresponderem, False caso contrário.
    """
    return senha_hash_armazenada == hash_senha(senha_fornecida)

# --- Funções de Gerenciamento de Arquivos (I/O) ---

def carregar_dados(nome_arquivo: str) -> List[Dict[str, str]]:
    """
    Carrega dados de um arquivo CSV e os retorna como uma lista de dicionários.

    Entrada:
        nome_arquivo (str): O caminho para o arquivo CSV.

    Saída:
        List[Dict[str, str]]: Uma lista de dicionários, onde cada dicionário
                                representa uma linha do CSV. Retorna lista vazia
                                se o arquivo não existir.
    """
    if not os.path.exists(nome_arquivo):
        return []
    
    dados = []
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8', newline='') as f:
            # Usamos ; como delimitador, comum no Brasil
            leitor = csv.DictReader(f, delimiter=';')
            for linha in leitor:
                dados.append(linha)
    except Exception as e:
        print(f"Erro ao carregar o arquivo {nome_arquivo}: {e}")
        return [] # Retorna lista vazia em caso de erro
    return dados

def salvar_dados(nome_arquivo: str, dados: List[Dict[str, str]], cabecalho: List[str]):
    """
    Salva uma lista de dicionários em um arquivo CSV.
    Requer o cabeçalho para garantir a ordem correta das colunas.

    Entradas:
        nome_arquivo (str): O caminho para o arquivo CSV onde os dados serão salvos.
        dados (List[Dict[str, str]]): A lista de dicionários a ser salva.
        cabecalho (List[str]): A lista de nomes de colunas (chaves do dicionário)
                               na ordem correta.
    """
    try:
        with open(nome_arquivo, mode='w', encoding='utf-8', newline='') as f:
            # Usamos ; como delimitador
            escritor = csv.DictWriter(f, fieldnames=cabecalho, delimiter=';')
            escritor.writeheader()
            escritor.writerows(dados)
    except Exception as e:
        print(f"Erro ao salvar os dados em {nome_arquivo}: {e}")

# --- Funções de Autenticação ---

def fazer_login(usuarios: List[Dict[str, str]]) -> Union[Tuple[str, str], None]:
    """
    Solicita ao usuário login e senha e tenta autenticar.
    Dá 3 tentativas antes de encerrar o programa.

    Entrada:
        usuarios (List[Dict[str, str]]): A lista de usuários carregada da memória.

    Saída:
        Union[Tuple[str, str], None]: Uma tupla (username, role) se o login
                                      for bem-sucedido. None se falhar 3 vezes.
    """
    print("--- 💻 Bem-vindo ao EcoManager 💻 ---")
    tentativas = 0
    while tentativas < 3:
        username = input("Usuário: ").strip()
        # getpass esconde a senha enquanto é digitada
        senha = getpass.getpass("Senha: ").strip()

        for usuario in usuarios:
            if usuario['username'] == username:
                if verificar_senha(usuario['password_hash'], senha):
                    print(f"\nLogin bem-sucedido! Bem-vindo(a), {username} ({usuario['role']}).")
                    # Retorna uma tupla com o usuário e sua role
                    return (usuario['username'], usuario['role'])
                else:
                    break # Senha errada, sai do loop de usuários

        tentativas += 1
        print(f"Usuário ou senha inválidos. Tentativas restantes: {3 - tentativas}")
    
    print("Número máximo de tentativas excedido. Encerrando.")
    return None

# --- Funções CRUD: Usuários (Exclusivo Gerente) ---

def adicionar_usuario(usuarios: List[Dict[str, str]]) -> bool:
    """
    (Create) Adiciona um novo usuário à lista de usuários.
    Valida se o username já existe e se a role é válida.

    Entrada:
        usuarios (List[Dict[str, str]]): Lista atual de usuários.

    Saída:
        bool: True se o usuário foi adicionado, False caso contrário.
    """
    print("\n--- Adicionar Novo Usuário ---")
    username = input("Novo username: ").strip()
    
    # Verifica se o usuário já existe
    if any(u['username'] == username for u in usuarios):
        print("Erro: Este username já está em uso.")
        return False

    # Validação da Role (usando o SET)
    role = ""
    while role not in ROLES_VALIDAS:
        role = input(f"Role ({'/'.join(ROLES_VALIDAS)}): ").strip().lower()
        if role not in ROLES_VALIDAS:
            print(f"Role inválida. Escolha uma das opções: {ROLES_VALIDAS}")

    senha = getpass.getpass("Senha: ").strip()
    senha_confirm = getpass.getpass("Confirme a senha: ").strip()

    if senha != senha_confirm:
        print("Erro: As senhas não conferem.")
        return False

    novo_usuario = {
        "username": username,
        "password_hash": hash_senha(senha),
        "role": role
    }
    usuarios.append(novo_usuario)
    print(f"Usuário '{username}' ({role}) criado com sucesso!")
    return True

def listar_usuarios(usuarios: List[Dict[str, str]]):
    """
    (Read) Lista todos os usuários cadastrados (sem a senha).

    Entrada:
        usuarios (List[Dict[str, str]]): Lista atual de usuários.
    """
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
        
    print(f"{'Username':<20} | {'Role':<10}")
    print("-" * 33)
    for usuario in usuarios:
        print(f"{usuario['username']:<20} | {usuario['role']:<10}")

def atualizar_usuario(usuarios: List[Dict[str, str]], usuario_logado: str) -> bool:
    """
    (Update) Atualiza a role ou a senha de um usuário existente.
    Um usuário não pode alterar a si mesmo.

    Entrada:
        usuarios (List[Dict[str, str]]): Lista atual de usuários.
        usuario_logado (str): O username do gerente logado.

    Saída:
        bool: True se a atualização foi bem-sucedida, False caso contrário.
    """
    print("\n--- Atualizar Usuário ---")
    username_alvo = input("Digite o username do usuário a ser atualizado: ").strip()
    
    if username_alvo == usuario_logado:
        print("Erro: Você não pode modificar sua própria conta por este menu.")
        return False
        
    usuario_encontrado = None
    for u in usuarios:
        if u['username'] == username_alvo:
            usuario_encontrado = u
            break
            
    if not usuario_encontrado:
        print("Erro: Usuário não encontrado.")
        return False

    print(f"Usuário encontrado: {username_alvo} (Role: {usuario_encontrado['role']})")
    print("O que deseja atualizar?")
    print("1. Alterar Role")
    print("2. Resetar Senha")
    print("0. Cancelar")
    escolha = input("Opção: ")

    if escolha == '1':
        nova_role = ""
        while nova_role not in ROLES_VALIDAS:
            nova_role = input(f"Nova Role ({'/'.join(ROLES_VALIDAS)}): ").strip().lower()
            if nova_role not in ROLES_VALIDAS:
                print(f"Role inválida. Escolha: {ROLES_VALIDAS}")
        
        usuario_encontrado['role'] = nova_role
        print(f"Role de '{username_alvo}' atualizada para '{nova_role}'.")
        return True
        
    elif escolha == '2':
        nova_senha = getpass.getpass("Nova Senha: ").strip()
        nova_senha_confirm = getpass.getpass("Confirme a Nova Senha: ").strip()
        
        if nova_senha != nova_senha_confirm:
            print("Erro: As senhas não conferem.")
            return False
            
        usuario_encontrado['password_hash'] = hash_senha(nova_senha)
        print(f"Senha de '{username_alvo}' atualizada com sucesso.")
        return True
        
    else:
        print("Atualização cancelada.")
        return False

def remover_usuario(usuarios: List[Dict[str, str]], usuario_logado: str) -> bool:
    """
    (Delete) Remove um usuário da lista.
    Um usuário não pode deletar a si mesmo.

    Entrada:
        usuarios (List[Dict[str, str]]): Lista atual de usuários.
        usuario_logado (str): O username do gerente logado.

    Saída:
        bool: True se a remoção foi bem-sucedida, False caso contrário.
    """
    print("\n--- Remover Usuário ---")
    username_alvo = input("Digite o username do usuário a ser REMOVIDO: ").strip()

    if username_alvo == usuario_logado:
        print("Erro: Você não pode remover sua própria conta.")
        return False
    
    usuario_encontrado = None
    for u in usuarios:
        if u['username'] == username_alvo:
            usuario_encontrado = u
            break
    
    if not usuario_encontrado:
        print("Erro: Usuário não encontrado.")
        return False
        
    confirm = input(f"Tem certeza que deseja remover '{username_alvo}' (Role: {usuario_encontrado['role']})? (s/n): ").lower()
    
    if confirm == 's':
        usuarios.remove(usuario_encontrado)
        print(f"Usuário '{username_alvo}' removido com sucesso.")
        return True
    else:
        print("Remoção cancelada.")
        return False

# --- Funções CRUD: Produtos (Acesso Misto) ---

def _validar_e_converter_produto(produto: Dict[str, str]) -> Union[Dict[str, Union[str, float, int]], None]:
    """
    Função auxiliar para converter campos de string (do CSV)
    para tipos numéricos (float, int) e validar.
    """
    try:
        # Mantém strings que são strings, converte o resto
        produto_convertido = produto.copy()
        produto_convertido['preco'] = float(produto['preco'])
        produto_convertido['quantidade'] = int(produto['quantidade'])
        
        if produto_convertido['preco'] < 0 or produto_convertido['quantidade'] < 0:
            print(f"Aviso: Produto '{produto['nome']}' (ID: {produto['id']}) possui valores negativos e será ignorado.")
            return None
            
        return produto_convertido
    except (ValueError, TypeError, KeyError) as e:
        print(f"Aviso: Erro ao processar produto (ID: {produto.get('id', 'N/A')}). {e}. Ignorando produto.")
        return None

def carregar_e_processar_produtos() -> List[Dict[str, Union[str, float, int]]]:
    """
    Carrega os produtos do CSV e processa (converte tipos de dados).
    """
    produtos_raw = carregar_dados(ARQUIVO_PRODUTOS)
    produtos_processados = []
    for prod in produtos_raw:
        prod_convertido = _validar_e_converter_produto(prod)
        if prod_convertido: # Adiciona apenas se a conversão foi bem-sucedida
            produtos_processados.append(prod_convertido)
    return produtos_processados

def _obter_proximo_id(produtos: List[Dict]) -> str:
    """Gera um novo ID numérico baseado no maior ID existente."""
    if not produtos:
        return "1001" # Começa em 1001
    
    max_id = 0
    for p in produtos:
        try:
            id_num = int(p['id'])
            if id_num > max_id:
                max_id = id_num
        except ValueError:
            continue # Ignora IDs não numéricos
            
    return str(max_id + 1)

def _imprimir_lista_produtos(lista_produtos: List[Dict]):
    """Função auxiliar para imprimir cabeçalho e lista de produtos."""
    if not lista_produtos:
        print("Nenhum produto encontrado.")
        return
        
    print(f"\n{'ID':<5} | {'Nome':<30} | {'Categoria':<15} | {'Preço (R$)':<12} | {'Qtd.':<5}")
    print("-" * 75)
    for p in lista_produtos:
        # Formata o preço para ter 2 casas decimais
        preco_formatado = f"{p['preco']:.2f}"
        print(f"{p['id']:<5} | {p['nome']:<30} | {p['categoria']:<15} | {preco_formatado:<12} | {p['quantidade']:<5}")


# (Create) - Gerente
def adicionar_produto(produtos: List[Dict]):
    """
    (Create) Adiciona um novo produto ao estoque.
    """
    print("\n--- Adicionar Novo Produto ---")
    try:
        nome = input("Nome do produto: ").strip()
        categoria = input("Categoria (ex: Notebook, Desktop, Peça): ").strip()
        preco = float(input("Preço (ex: 1250.50): "))
        quantidade = int(input("Quantidade em estoque: "))
        
        if preco < 0 or quantidade < 0:
            print("Erro: Preço e quantidade não podem ser negativos.")
            return

        novo_id = _obter_proximo_id(produtos)
        novo_produto = {
            "id": novo_id,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        }
        produtos.append(novo_produto)
        print(f"Produto '{nome}' (ID: {novo_id}) adicionado com sucesso!")
        
    except ValueError:
        print("Erro: Entrada inválida para preço ou quantidade. Use apenas números.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# (Read) - Todos
def listar_todos_produtos(produtos: List[Dict]):
    """
    (Read) Imprime todos os produtos.
    """
    print("\n--- Estoque Completo (EcoByte) ---")
    _imprimir_lista_produtos(produtos)

# (Read - Específico) - Todos
def buscar_produto(produtos: List[Dict]):
    """
    (Read) Busca um produto por ID ou Nome.
    """
    print("\n--- Buscar Produto ---")
    termo = input("Digite o ID ou parte do nome do produto: ").strip().lower()
    
    if not termo:
        print("Busca cancelada.")
        return

    resultados = []
    for p in produtos:
        # Busca por ID exato ou nome parcial (case-insensitive)
        if p['id'] == termo or termo in p['nome'].lower():
            resultados.append(p)
            
    if not resultados:
        print(f"Nenhum produto encontrado com o termo '{termo}'.")
    else:
        print(f"Resultados da busca por '{termo}':")
        _imprimir_lista_produtos(resultados)

# (Read - Específico) - Todos
def imprimir_por_nome(produtos: List[Dict]):
    """
    (Read) Imprime todos os produtos ordenados por nome (A-Z).
    """
    print("\n--- Estoque (Ordenado por Nome) ---")
    # Usa uma função lambda como chave de ordenação
    produtos_ordenados = sorted(produtos, key=lambda p: p['nome'].lower())
    _imprimir_lista_produtos(produtos_ordenados)

# (Read - Específico) - Todos
def imprimir_por_preco(produtos: List[Dict]):
    """
    (Read) Imprime todos os produtos ordenados por preço (Mais barato > Mais caro).
    """
    print("\n--- Estoque (Ordenado por Preço) ---")
    # Usa uma função lambda como chave de ordenação
    produtos_ordenados = sorted(produtos, key=lambda p: p['preco'])
    _imprimir_lista_produtos(produtos_ordenados)

# (Update) - Gerente
def atualizar_produto_completo(produtos: List[Dict]):
    """
    (Update) Permite ao Gerente atualizar qualquer campo de um produto.
    """
    print("\n--- Atualizar Produto (Gerente) ---")
    id_alvo = input("Digite o ID do produto a ser atualizado: ").strip()
    
    produto_encontrado = None
    for p in produtos:
        if p['id'] == id_alvo:
            produto_encontrado = p
            break
            
    if not produto_encontrado:
        print("Erro: Produto não encontrado.")
        return

    print("Produto encontrado:")
    _imprimir_lista_produtos([produto_encontrado])
    print("\nDeixe em branco para manter o valor atual.")
    
    try:
        # Atualiza os campos
        nome_novo = input(f"Nome ({produto_encontrado['nome']}): ").strip()
        if nome_novo:
            produto_encontrado['nome'] = nome_novo
            
        cat_nova = input(f"Categoria ({produto_encontrado['categoria']}): ").strip()
        if cat_nova:
            produto_encontrado['categoria'] = cat_nova

        preco_novo_str = input(f"Preço ({produto_encontrado['preco']:.2f}): ").strip()
        if preco_novo_str:
            preco_novo = float(preco_novo_str)
            if preco_novo < 0:
                print("Preço não pode ser negativo. Mantendo o original.")
            else:
                produto_encontrado['preco'] = preco_novo
                
        qtd_nova_str = input(f"Quantidade ({produto_encontrado['quantidade']}): ").strip()
        if qtd_nova_str:
            qtd_nova = int(qtd_nova_str)
            if qtd_nova < 0:
                print("Quantidade não pode ser negativa. Mantendo a original.")
            else:
                produto_encontrado['quantidade'] = qtd_nova

        print("Produto atualizado com sucesso!")
        _imprimir_lista_produtos([produto_encontrado])
        
    except ValueError:
        print("Erro: Entrada numérica inválida. A atualização foi cancelada.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# (Update) - Técnico (Limitado)
def atualizar_estoque_tecnico(produtos: List[Dict]):
    """
    (Update) Permite ao Técnico apenas adicionar ou remover unidades do estoque
    (simulando recondicionamento ou venda/descarte).
    """
    print("\n--- Atualizar Estoque (Técnico) ---")
    id_alvo = input("Digite o ID do produto para ajustar o estoque: ").strip()
    
    produto_encontrado = None
    for p in produtos:
        if p['id'] == id_alvo:
            produto_encontrado = p
            break
            
    if not produto_encontrado:
        print("Erro: Produto não encontrado.")
        return
        
    print("Produto encontrado:")
    _imprimir_lista_produtos([produto_encontrado])
    
    try:
        # O técnico não "define" a quantidade, ele "ajusta"
        ajuste_str = input("Valor do ajuste (ex: +5 se recondicionou 5, -1 se vendeu 1): ").strip()
        if not ajuste_str:
            print("Nenhum ajuste feito.")
            return

        ajuste = int(ajuste_str)
        
        nova_quantidade = produto_encontrado['quantidade'] + ajuste
        
        if nova_quantidade < 0:
            print(f"Erro: Ajuste de {ajuste} deixaria o estoque negativo ({nova_quantidade}).")
            print(f"Estoque atual: {produto_encontrado['quantidade']}. Operação cancelada.")
        else:
            produto_encontrado['quantidade'] = nova_quantidade
            print("Estoque atualizado com sucesso!")
            _imprimir_lista_produtos([produto_encontrado])

    except ValueError:
        print("Erro: Entrada inválida. Use um número inteiro (ex: 5, -2).")

# (Delete) - Gerente
def remover_produto(produtos: List[Dict]):
    """
    (Delete) Remove um produto do estoque.
    """
    print("\n--- Remover Produto ---")
    id_alvo = input("Digite o ID do produto a ser REMOVIDO: ").strip()
    
    produto_encontrado = None
    for p in produtos:
        if p['id'] == id_alvo:
            produto_encontrado = p
            break
            
    if not produto_encontrado:
        print("Erro: Produto não encontrado.")
        return
        
    print("Produto selecionado para remoção:")
    _imprimir_lista_produtos([produto_encontrado])
    
    confirm = input(f"Tem certeza que deseja remover '{produto_encontrado['nome']}' (ID: {id_alvo})? (s/n): ").lower()
    
    if confirm == 's':
        produtos.remove(produto_encontrado) # Remove o dicionário da lista
        print("Produto removido com sucesso.")
    else:
        print("Remoção cancelada.")

# --- Menus por Role ---

def menu_tecnico(produtos: List[Dict], usuario_logado: str):
    """
    Menu de operações para o nível de permissão 'tecnico'.
    """
    print(f"\n--- Menu Técnico [Usuário: {usuario_logado}] ---")
    
    while True:
        print("\n[ Menu de Produtos ]")
        print("1. Listar todos os produtos (Estoque)")
        print("2. Buscar produto (por ID ou Nome)")
        print("3. Listar produtos por Nome (A-Z)")
        print("4. Listar produtos por Preço (Barato > Caro)")
        print("5. Atualizar estoque (Registrar entrada/saída)")
        print("0. Fazer Logout")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            listar_todos_produtos(produtos)
        elif escolha == '2':
            buscar_produto(produtos)
        elif escolha == '3':
            imprimir_por_nome(produtos)
        elif escolha == '4':
            imprimir_por_preco(produtos)
        elif escolha == '5':
            # (Update) - Acesso limitado
            atualizar_estoque_tecnico(produtos)
        elif escolha == '0':
            print("Fazendo logout...")
            break # Sai do loop while
        else:
            print("Opção inválida. Tente novamente.")

def menu_gerente(usuarios: List[Dict], produtos: List[Dict], usuario_logado: str):
    """
    Menu de operações para o nível de permissão 'gerente'.
    """
    print(f"\n--- Menu Gerencial [Usuário: {usuario_logado}] ---")
    
    while True:
        print("\n[ Gerenciamento de Produtos ]")
        print("1. Listar todos os produtos (Estoque)")
        print("2. Buscar produto (por ID ou Nome)")
        print("3. Listar produtos por Nome (A-Z)")
        print("4. Listar produtos por Preço (Barato > Caro)")
        print("5. (C) Adicionar novo produto")
        print("6. (U) Atualizar produto (Detalhado)")
        print("7. (D) Remover produto")
        
        print("\n[ Gerenciamento de Usuários ]")
        print("8. (R) Listar todos os usuários")
        print("9. (C) Adicionar novo usuário")
        print("10. (U) Atualizar usuário (Role/Senha)")
        print("11. (D) Remover usuário")
        
        print("\n" + "=" * 30)
        print("0. Fazer Logout (Salvar e Sair)")
        
        escolha = input("Escolha uma opção: ").strip()
        
        # Bloco Produtos
        if escolha == '1':
            listar_todos_produtos(produtos)
        elif escolha == '2':
            buscar_produto(produtos)
        elif escolha == '3':
            imprimir_por_nome(produtos)
        elif escolha == '4':
            imprimir_por_preco(produtos)
        elif escolha == '5':
            adicionar_produto(produtos) # Create
        elif escolha == '6':
            atualizar_produto_completo(produtos) # Update
        elif escolha == '7':
            remover_produto(produtos) # Delete
        
        # Bloco Usuários
        elif escolha == '8':
            listar_usuarios(usuarios) # Read
        elif escolha == '9':
            adicionar_usuario(usuarios) # Create
        elif escolha == '10':
            atualizar_usuario(usuarios, usuario_logado) # Update
        elif escolha == '11':
            remover_usuario(usuarios, usuario_logado) # Delete
            
        # Saída
        elif escolha == '0':
            print("Fazendo logout...")
            break # Sai do loop while
        else:
            print("Opção inválida. Tente novamente.")


# --- Função Principal (Main) ---

def main():
    """
    Função principal que orquestra o programa.
    """
    # 1. Carregar dados na inicialização
    # Usamos list() para garantir que temos uma cópia mutável
    usuarios_db = list(carregar_dados(ARQUIVO_USUARIOS))
    
    # Produtos precisam de conversão de tipo
    produtos_db = carregar_e_processar_produtos()

    # 2. Autenticação
    # A função login retorna uma tupla (username, role)
    info_login = fazer_login(usuarios_db)
    
    if not info_login:
        sys.exit(0) # Encerra se o login falhar

    # Desempacota a tupla
    usuario_logado, role_logado = info_login
    
    # 3. Direcionamento por Role
    try:
        if role_logado == 'gerente':
            menu_gerente(usuarios_db, produtos_db, usuario_logado)
        elif role_logado == 'tecnico':
            menu_tecnico(produtos_db, usuario_logado)
        else:
            print("Erro: Role desconhecida. Contate o administrador.")
            
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")
    finally:
        # 4. Salvar dados ao sair (Logout ou Erro)
        print("Salvando dados antes de encerrar...")
        
        # Prepara produtos para salvar (converte numérico para string)
        produtos_para_salvar = []
        for p in produtos_db:
            prod_str = p.copy()
            prod_str['preco'] = str(p['preco'])
            prod_str['quantidade'] = str(p['quantidade'])
            produtos_para_salvar.append(prod_str)
            
        salvar_dados(ARQUIVO_USUARIOS, usuarios_db, ['username', 'password_hash', 'role'])
        salvar_dados(ARQUIVO_PRODUTOS, produtos_para_salvar, ['id', 'nome', 'categoria', 'preco', 'quantidade'])
        
        print("Dados salvos. Até logo!")

# Ponto de entrada do script
if __name__ == "__main__":
    main()