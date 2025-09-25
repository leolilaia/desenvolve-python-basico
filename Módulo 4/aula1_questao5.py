#Leitura da quantidade de respondentes
quantidade = int(input("Digite a quantidade de respondentes: "))

#Iniciaçização
N = 0
idade = 0

#Estrutura de repetição
while N < quantidade:
    idadeN = int(input("Digite a idade de cada respondente: "))
    idade += idadeN
    N+=1

#Calcula a média das idades
idade = idade/N

#Imprime o resultado
print("A média das idades é: ", idade)
