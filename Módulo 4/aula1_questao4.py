#Entrada de dados
n = int(input("Quantos números deseja digitar? "))

#inicialização
maior = 0

#Estrutura de repetição
while n > 0:
    x = int(input("Digite um número: "))
        
    if x > maior:
            maior = x

    n = n - 1

#Saída
print("Maior =", maior)