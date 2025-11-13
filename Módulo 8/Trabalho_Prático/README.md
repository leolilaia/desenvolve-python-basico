# Projeto de Software: EcoManager (Trabalho Prático)

Este é o repositório do meu trabalho prático, que implementa um sistema de gerenciamento para uma empresa que idealizei, a **"EcoByte Soluções"**.

## Introdução

### A Minha Empresa: EcoByte Soluções

Para este projeto, pensei em criar uma empresa com um foco em sustentabilidade e tecnologia. Assim nasceu a **EcoByte Soluções**.

A ideia é simples: a EcoByte compra hardware de computador usado (notebooks, peças, etc.), nossa equipe recondiciona esse material (conserta, limpa, melhora) e depois o vendemos por um preço justo. O foco seria ajudar estudantes e pequenas empresas que precisam de equipamentos, mas não podem pagar por um novo.

### Usuários do Sistema

O software que criei, o "EcoManager", é para o controle interno da empresa. Pensei em dois tipos de usuários:

1.  **Gerente (`gerente`):** É o "chefão". Ele tem acesso a tudo. Pode adicionar novos produtos, mudar preços, e o mais importante: pode contratar e demitir, ou seja, **gerenciar os outros usuários** (criar contas, mudar senhas, etc.).
2.  **Técnico (`tecnico`):** É o funcionário que "põe a mão na massa". Ele é responsável por recondicionar os produtos. No sistema, ele pode **ver todo o estoque** e **atualizar a quantidade** (por exemplo, se ele acabou de consertar um notebook, ele adiciona +1 ao estoque; se vendeu um, dá baixa).

### Produtos

O sistema gerencia os **Produtos** da EcoByte. Cada produto tem:
* `id` (um código único)
* `nome` (ex: "Notebook Dell Vostro (Usado)")
* `categoria` (ex: "Notebook", "Peça")
* `preco` (quanto ele custa)
* `quantidade` (quantos temos em estoque)

---

## Implementação

Para construir o EcoManager, usei os conceitos que aprendemos em aula.

### Elemento: Usuários

1.  **Estrutura de Dados (na Memória):**
    * Eu usei uma **Lista de Dicionários** (Ex: `[ {"username": "admin", ...}, ... ]`).
    * **Por quê?** Achei que era a forma mais direta de organizar os dados na memória. Cada usuário é um dicionário, e a lista guarda todos eles. Além disso, essa estrutura funciona perfeitamente com o módulo `csv` do Python para carregar e salvar.

2.  **Estrutura do Arquivo (`usuarios.csv`):**
    * É um arquivo `.csv` simples, usando `;` como separador (padrão comum no Brasil).
    * As colunas são: `username;password_hash;role`
    * **Nota sobre a Senha:** Para não salvar a senha que o usuário digita (o "texto puro"), eu pesquisei e usei as bibliotecas `hashlib` e `getpass`. O `hashlib` cria um "código" (hash SHA-256) da senha, e é esse código que eu salvo no arquivo. O `getpass` faz a senha ficar invisível na hora de digitar no terminal.

3.  **Funcionalidades (CRUD):**
    * **C**reate: `adicionar_usuario()` (só o gerente).
    * **R**ead: `listar_usuarios()` e `fazer_login()`.
    * **U**pdate: `atualizar_usuario()` (mudar role ou senha, só o gerente).
    * **D**elete: `remover_usuario()` (só o gerente).

### Elemento: Produtos

1.  **Estrutura de Dados (na Memória):**
    * Usei a mesma estrutura dos usuários: uma **Lista de Dicionários**.
    * **Por quê?** Pelos mesmos motivos e porque ter os produtos em uma lista simples tornou muito mais fácil fazer as **funções de ordenação** (que eram obrigatórias), tanto por nome quanto por preço. Usei `sorted()` com uma função `lambda` para resolver isso.

2.  **Estrutura do Arquivo (`produtos.csv`):**
    * Também é um `.csv` com `;`.
    * Colunas: `id;nome;categoria;preco;quantidade`

3.  **Funcionalidades (CRUD):**
    * **C**reate: `adicionar_produto()` (só o gerente).
    * **R**ead:
        * `listar_todos_produtos()` (todo mundo vê)
        * `buscar_produto()` (todo mundo vê)
        * `imprimir_por_nome()` (todo mundo vê)
        * `imprimir_por_preco()` (todo mundo vê)
    * **U**pdate:
        * `atualizar_produto_completo()` (o gerente pode mudar tudo).
        * `atualizar_estoque_tecnico()` (o técnico só pode mudar a quantidade).
    * **D**elete: `remover_produto()` (só o gerente).

---

## Conclusão e Dificuldades

Este foi um projeto desafiador, mas muito gratificante.

### 1. Dificuldades Encontradas
A maior "dor de cabeça" foi, sem dúvida, lidar com os **tipos de dados**. O arquivo `.csv` salva *tudo* como texto (string). Mas no meu programa, eu precisava que `preco` fosse um número `float` e `quantidade` fosse um `int`, para poder fazer contas e ordenar corretamente.

Tive que criar funções específicas só para converter esses dados na hora que o programa carrega o arquivo (de *string* para *número*) e depois converter de volta na hora de salvar (de *número* para *string*).

Outro desafio foi separar os menus. Fazer com que o `tecnico` visse um menu limitado e o `gerente` visse o menu completo exigiu bastante uso de `if/else` e funções separadas.

### 2. O que Funcionou Bem
Aprender a usar o módulo `csv` do Python (especialmente o `DictReader` e `DictWriter`) **foi o que salvou o projeto**. Tornou a leitura e a escrita nos arquivos muito mais fácil e organizada do que tentar fazer "na mão" com `.split()`.

Também gostei de ter implementado o **hashing da senha**. Mesmo sendo um projeto de faculdade, foi uma boa prática de segurança.

### 3. O que Faria Diferente
Se eu fosse continuar esse projeto (ou fazer uma "versão 2.0"), eu com certeza **abandonaria os arquivos `.csv` e usaria um banco de dados de verdade**, como o **SQLite**.

O método que usei (carregar tudo na memória, modificar, e depois salvar tudo de volta) funciona para esse trabalho, mas se a EcoByte tivesse 10.000 produtos, o programa ficaria muito lento e correria o risco de perder dados. Com um banco de dados, eu poderia fazer consultas e atualizações de forma muito mais segura e eficiente.